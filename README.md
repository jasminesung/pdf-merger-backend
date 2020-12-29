# temperature-app-backend

An API built with Python and Flask to convert temperatures from Celsius to Fahrenheit, or vice-versa. The code in **main.py** is deployed as an HTTP Google Cloud Function (https://us-central1-symmetric-sonar-299910.cloudfunctions.net/convert_temp?base=:base&temp=:temp).

To run locally:

1. Run `pip install -r requirements.txt --no-index --find-links file:///tmp/packages` to install packages (use pip3 if you are using Python3).

2. Run `export FLASK_APP=server.py`.

3. Run `flask run`.