# Quotation Station API
Quote/funfact api for Quotation Station

## Local setup
To setup this project you need to first create a virtual environment named `env`. Keep in mind that this api uses python 3.7 and might not work with other versions. Also, this is a guide for setting up the api on a windows machine.

First, navigate to the folder containing the api.py file using the command line. Then run the following command:

`python3 venv env`

`env` is the name of the environment and should not be changed. If you want to change this name, then remember to update .gitingore.

Next, activate the environment:

`env\scripts\activate.bat`

Next, you need to install the project dependencies. This can be done using the following command:

`pip install -r requirements.txt`

Congratulations! You completed the setup and are ready to run the api.

To exit the environment, run the command:

`env\scripts\deactivate.bat`

## Running the api
To run the api, simply run the following command:

`python3 api.py`

This will start the server and the command line window should display this:

` * Serving Flask app "api" (lazy loading) `

` * Environment: production`

`   WARNING: Do not use the development server in a production environment.`

`   Use a production WSGI server instead.`

` * Debug mode: off`

` * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

This means the server is running properly (on port 5000), and you can begin sending api calls to it.
