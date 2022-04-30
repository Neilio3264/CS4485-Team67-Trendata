# CS4485-Team67-Trendata

The main code is located in the branch `yiwei-poc`. This can be located at: https://github.com/Neilio3264/CS4485-Team67-Trendata/tree/yiwei-poc

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
