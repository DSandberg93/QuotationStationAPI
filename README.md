# Quotation Station API
Quote/funfact api for Quotation Station

## Local setup

First, navigate to the folder containing the api.py file using the command line. Then, activate the environment contained in the `env` folder:

`env\scripts\activate.bat`

Make sure you have installed a version f python that is compatible with `venv` before activating. This project uses python 3.7, so I highly recommend installing this version.

Next, you need to install the project dependencies. This can be done using the following command:

`pip install -r requirements.txt`

Congratulations! You completed the setup and are ready to run the api.

To exit the environment, run the command:

`env\scripts\deactivate.bat`

## Running the api
Before you start the api, make sure you are inside the virtual eviroment mentioned above and that the necessary dependencies are installed in the environment.
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

## Disclamer
The quotes and funfacts provided by this api are not mine. They are meant to be used for a school project and are not monetized in any way. All credit goes to the authors, who are part of the api resonses along with the quotes and funfacts themselves!
