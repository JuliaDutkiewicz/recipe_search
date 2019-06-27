# Recipe search
A simple Django application for retriving recipes from [```TheMealDB API```](https://www.themealdb.com/api.php)
</br>The App is available at http://stormy-waters-60581.herokuapp.com

# Table of Contents
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Running on localhost](#running-on-localhost)
    - [Running using Docker Images](#running-using-docker-images)
- [Deployment](#deployment)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
```
Python 3.6
```

### Running on localhost
1. Install all the requirements
```
$  pip install -r requirements.txt
```
2. Apply the migrations
```
$  python manage.py migrate
```
3. Run the application
```
$ python manage.py runserver
```
3. Open a web browser (default host port: 8000)
    ```URL:```http://localhost:8000
    </br> Users are enabled to search a dataset of recipes.
    The main feature is filtering recipes by ingredients.

### Running using Docker Images
1. Use the following commands
```
$ docker-compose build
$ docker-compose up
```
2. Open a web browser (default host port: 8000)
    ```URL:```http://localhost:8000
    </br> Users are enabled to search a dataset of recipes.
    The main feature is filtering recipes by ingredients.

## Deployment
Remember to set ```DEBUG = False``` in settings.py file.

Use the following commands
```
$  heroku stack:set container
$  git push heroku master
$  heroku open
```
