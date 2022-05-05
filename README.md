# CS4485-Team67-Trendata

The main code is located in the branch `yiwei-poc`. This can be located at: https://github.com/Neilio3264/CS4485-Team67-Trendata/tree/yiwei-poc

# Data sources
1. `randomuser.me`: Obtained late March following the talks of first switching to plan B. Can be found at [randomeuser.me](https://randomuser.me/)
2. `akiFlagger`: Obtained early April following the initial research into plan B. Can be found at [akiFlagger.io](https://akiflagger.readthedocs.io/en/latest/)
3. `kidney_disease.csv`: Obtained mid April following the talks of potential plan C. Used to help mimic a complete patient profile. Can be found at [Kaggle](https://www.kaggle.com/code/drt953/classification-clustering-ckd/notebook)
4. `movehub rankings`: Obtained mid April after deciding to map a patient to a local and link the patient to quality of life ratings. Both `cities.csv` and `movehubqualityoflife.csv` were taken from this [Kaggle](https://www.kaggle.com/code/adrianofonseca1000/linearregression-movehubcity/data?select=cities.csv). Only provides cities with over 100,000 population and even less US cities have movehub rankings.

# Setting up the code

If you would like to run and compile, the code requires some setup.

1. Downloading dependencies:
   - Ensure that `python 3` is installed as well as `pip` package manager
   - run `pip install django djangorestframework django-address`
   - cd into **frontend**
     - run `npm install` to download node dependencies
2. Run and compile the code:
   - To run the code, cd into **trendialysis** folder (*The root project folder*)
   - run `python manage.py runserver`
     - If there is an error, remove the files within `api/migrations` (`__init__.py`, `0001_initial.py`, `0002_alter_patient_city_distance.py`)
     - run `python manage.py makemigrations`
     - run `python manage.py migrate`
     - try `python manage.py runserver` once again
   - Navigate the port indicated: `127.0.0.1:8000`
3. Navigate page
   - The homepage will display a simple welcome page. From here navigate to the `Patient Tab`
   - The Patient Tab will display the basic information for all 400 generated patients. Take note of once of these id values
   - The Quality of Life Tab will allow you to input a patient id to then retrieve the patient summary.
     - *If the view does not update after clicking the `Enter` button, refresh the page the view should populate with the new page information.*
   - The Summary Page will show the basic health metrics that have been mapped to the patient. Additionally, it displays the auto-generated akiFlagger data which displays the patient's Acute Kidney Injury classification based on the frequency and magnitude in creatinine levels. This data can be visualized in the chart showcasing the change overtime.