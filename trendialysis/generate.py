from akiFlagger import AKIFlagger, generate_toy_data
from randomuser import RandomUser
import pandas as pd
import numpy as np
import googlemaps
from time import sleep

from api.models import Patient, Address, CreatinineHistory, HealthMetrics, Cities, QualityOfLife
from data.HistoryClass import History

import os, django
from trendialysis.settings import GOOGLE_API_KEY
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trendialysis.settings")
django.setup()

# Generate Random User
user_list = RandomUser.generate_users(400, {'nat': 'us'})
# Generate Random Acute Kidney Data
toy = generate_toy_data(num_patients=410, num_encounters_range=(3, 15))
flagger = AKIFlagger()
out = flagger.returnAKIpatients(toy)
out = out.reset_index()

gmaps = googlemaps.Client(key=GOOGLE_API_KEY)

# Read in Kidney Disease Data for Health Info
pd.set_option('display.max_columns', 26)
health_data = pd.read_csv('./data/kidney_disease.csv')
# Preprocess the health data
health_data.rename(columns={'bp': 'Dias_blood_pressure', 
                            'sg': 'ur_specific_gravity',
                            'al':'ur_albumin',
                            'su':'ur_sugar',
                            'rbc':'red_blood_cells',
                            'pc':'ur_pus_cell',
                            'pcc':'ur_ pus_cell clumps',
                            'ba':'ur_bacteria',
                            'bgr':'blood glucose random',
                            'bu':'blood urea',
                            'sc':'serum creatinine',
                            'sod':'sodium',
                            'pot':'potassium',
                            'hemo':'hemoglobin',
                            'pcv':'packed cell volume',
                            'wc':'white blood cell count',
                            'rc':'red blood cell count',
                            'htn':'hypertension',
                            'dm':'diabetes',
                            'cad':'coronary artery disease',
                            'appet':'appetite',
                            'pe':'pedal edema',
                            'ane':'anemia',
                            'classification':'class'}, inplace=True)
health_data.drop(columns=['age', 'serum creatinine'], inplace=True)
health_data.replace({np.nan: None}, inplace=True)
health_data.replace({'\t?': None}, inplace=True)

Patient.objects.all().delete()
# Cities.objects.all().delete()

# # Add the city information
# cities = pd.read_csv('./data/cities.csv')
# cities = cities[cities['Country'] == 'United States']
# # Add Quality of Life for city with population over 100,000 (Only cities which are in our Cities db)
# qol = pd.read_csv('./data/movehubqualityoflife.csv')
# # Generate Tables
# for local in cities.index:
#     city_str = cities['City'][local]
#     city = Cities.objects.create(city=city_str)
#     city.save()
    
#     for i in qol.index:
#         if (city_str.find(qol['City'][i]) != -1):
#             obj = QualityOfLife.objects.create(city=city,
#                                                quality_of_life=qol['Quality of Life'][i],
#                                                purchase_power=qol['Purchase Power'][i],
#                                                healthcare=qol['Health Care'][i],
#                                                pollution=qol['Pollution'][i],
#                                                crime=qol['Crime Rating'][i])
#             obj.save()

for user in user_list:
    # Parse for the street number in the address field
    address = user.get_street()
    address = address.split(' ', 1)
    street_number = address[0]
    street = address[1]
    
    local = user.get_city()
    state = user.get_state()
    zip = user.get_postcode()
    
    full = street_number + ' ' + street + ', ' + local + ', ' + state + ' ' + str(zip) + ', US'

    # Use generated data to create patient_id and creatinine levels
    previous_id = out['patient_id'][0]
    patient_id = 0
    index_del = []
    hist_objs = []
    for data in out.index:
        current_id = out['patient_id'][data]
        if (previous_id != current_id):
            break
        patient_id = current_id
        index_del.append(data)
        
        time = out['time'][data]
        inpatient = out['inpatient'][data]
        creatinine = out['creatinine'][data]
        aki = out['aki'][data]
        
        hist = History(time, inpatient, creatinine, aki)
        hist_objs.append(hist)
    
    out.drop(index=index_del, inplace=True)
    out.reset_index(drop=True, inplace=True)
    
    
    # Calculate distance between all the cities and find nearest to patient
    min = 32000
    cityID = 0
    index = 0
    check_cities = QualityOfLife.objects.all()
    for city in check_cities:
        obj = Cities.objects.filter(id=city.city_id)
        name = obj[0].city
        destination = local + ", " + state
        result = gmaps.distance_matrix(destination, name, mode='driving')
        
        if (result["status"] != 'OK'):
            continue
        result = result["rows"][0]["elements"][0]
        
        if (result["status"] != 'OK'):
            continue
        
        result = result["distance"]["value"]
        result = result / 1000
        if (result < min):
            min = result
            cityID = city.city_id
        sleep(0.3)
    
    # Create Patient Object and add to SQL Table
    obj = Patient.objects.create(patient_id=patient_id,
                                 first_name=user.get_first_name(),
                                 last_name=user.get_last_name(),
                                 age=user.get_age(),
                                 gender=user.get_gender(),
                                 phone=user.get_phone(),
                                 nearest_city=cityID,
                                 city_distance=min)
    obj.save()
    
    # Create Address Object for the Patient created above
    add = Address.objects.create(patient=obj,
                                 location={'raw': full, 
                                           'street_number': street_number, 
                                           'route': street,
                                           'locality': local,
                                           'postal_code': zip,
                                           'state': state,
                                           'country': 'United States',
                                           'country_code': 'US'})
    add.save()
    
    # Add all Patient records into the CreatinineHistory table
    for hist in hist_objs:
        record = CreatinineHistory.objects.create(patient=obj, 
                                                  time=pd.Timestamp.to_pydatetime(hist.time()), 
                                                  inpatient=hist.inpatient(), 
                                                  creatinine=hist.creatinine(), 
                                                  aki=hist.aki())
        record.save()
    
    # Add additional health information to each patient
    health = HealthMetrics.objects.create(patient=obj,
                                          Dias_blood_pressure=health_data['Dias_blood_pressure'][0],
                                          ur_specific_gravity=health_data['ur_specific_gravity'][0],
                                          ur_albumin=health_data['ur_albumin'][0],
                                          ur_sugar=health_data['ur_sugar'][0],
                                          red_blood_cells=health_data['red_blood_cells'][0],
                                          ur_pus_cell=health_data['ur_pus_cell'][0],
                                          ur_pus_cell_Clumps=health_data['ur_ pus_cell clumps'][0],
                                          ur_bacteria=health_data['ur_bacteria'][0],
                                          blood_glucose_random=health_data['blood glucose random'][0],
                                          blood_urea=health_data['blood urea'][0],
                                          sodium=health_data['sodium'][0],
                                          potassium=health_data['potassium'][0],
                                          hemoglobin=health_data['hemoglobin'][0],
                                          packed_cell_volume=health_data['packed cell volume'][0],
                                          white_blood_cell_count=health_data['white blood cell count'][0],
                                          red_blood_cell_count=health_data['red blood cell count'][0],
                                          hypertension=health_data['hypertension'][0],
                                          diabetes=health_data['diabetes'][0],
                                          coronary_artery_disease=health_data['coronary artery disease'][0],
                                          appetite=health_data['appetite'][0],
                                          pedal_edema=health_data['pedal edema'][0],
                                          anemia=health_data['anemia'][0],
                                          classification=health_data['class'][0])
    health.save()
    health_data.drop(index=0, inplace=True)
    health_data.reset_index(drop=True, inplace=True)
