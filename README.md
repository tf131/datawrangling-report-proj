# This repository contains a project for the course DMDB / OTH REGENSBURG (PYTHON 3.8)

1. Clone the repository to your local machine and navigate there
1. make sure you are running PYTHON3.8:
'python3.8 -V'
1. on debian based os, install virtualenv driver
`sudo apt-get install python38-venv`
1. create a new PHYTHON3.8 environment, activate it and install all requirements
`python3.8 -m venv ./venv`
1. activate your virtualenv
`source venv/bin/activate`
1. install requirements
`pip install -r requirements.txt`
3. The config file conf.ini has to be adapted:
1.1 Create your own API Keys for: hereapi, google places and geocodio
1.2 Fill in your mongoDB connection string
1. run the main function
