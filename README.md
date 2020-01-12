# This repository contains a project for the course DMDB / OTH REGENSBURG (PYTHON 3.8)
Install Python3.8.1 to your local machine
https://www.python.org/downloads/release/python-381/
During installation, make shure to add Python to environment variables.


1. Clone the repository to your local machine and navigate there
1. make sure you are running PYTHON3.8:
'python -V'
1. on debian based os, install virtualenv driver
`sudo apt-get install python38-venv`
1. create a new PHYTHON3.8 environment, activate it and install all requirements
`python -m venv ./venv`
1. activate your virtualenv
debian based: `source venv/bin/activate`
windows: `venv\Scripts\activate`
1. upgrade pip
`python -m pip install --upgrade pip`
1. install requirements
`pip install -r requirements.txt`
3. The config file conf.ini has to be adapted.
1.1. Create your own API Keys for: 
1.1.1. hereapi https://developer.here.com/
1.1.1. google place search https://developers.google.com/places/web-service/search 
1.1.1. geocodio https://www.geocod.io/docs/
1.2. Fill in your mongoDB connection string
1. run the main function
