# Setting up the project 

## Create a virtual environment within the FASTAPI folder 
mkdir FASTAPI
cd FASTAPI 

## Install the virtual environment 
pip install virtualenv

## Create the virtual environment 
virtualenv name_of_environment 

## To activate the environment 
source name_of_environment/bin/activate 

## To check softwares currently installed 
pip list


# Installing dependencies 

## To upgrade pip
pip install --upgrade pip

## To install fastapi
pip install fastapi

## To install web server uvicorn 
pip install uvicorn  

## To get out of virtual environment 
deactivate


## To run app without reloading the server 
uvicorn main:app --reload

## To assess the documentation
http://127.0.0.1:8000/docs 
/docs

