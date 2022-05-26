# Setting up the project 

## 1. Create project directory and cd into it FASTAPI folder 
mkdir FASTAPI AND cd FASTAPI 

## 2. Install the virtual environment 
pip install virtualenv

## 3. Create the virtual environment 
python3 -m venv virtualenv
# virtualenv is the name of virtual env
# OR 
virtualenv name_of_environment 

## 4. To activate the virtual environment 
source name_of_environment/bin/activate 

## 5. You can confirm you’re in the virtual environment by checking the location of your Python interpreter:
which python
## It should be in the env directory:

## 6. To get out of virtual environment 
deactivate



# Installing dependencies 

## To check softwares currently installed 
pip list

## To upgrade pip
pip install --upgrade pip

## To install fastapi
pip install fastapi

## To install web server uvicorn 
pip install uvicorn  

## To run app without reloading the server 
uvicorn main:app --reload

## To assess the documentation
http://127.0.0.1:8000/docs 
/docs

