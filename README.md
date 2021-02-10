# temperature-app-backend

An API built with Python and Flask to convert temperatures from Celsius to Fahrenheit, or vice-versa. The code in **main.py** is deployed as an HTTP Google Cloud Function (https://us-central1-symmetric-sonar-299910.cloudfunctions.net/convert_temp?base=:base&temp=:temp).

To run locally with Python3:

1. Run `python3 -m venv venv` in project directory to create a virtual environment.

2. Run `source venv/bin/activate` to activate the virtual environment.

3. Run `python3 -m pip install -r requirements.txt`.

4. Run `export FLASK_APP=server.py`.

5. Run `python3 -m flask run`.
