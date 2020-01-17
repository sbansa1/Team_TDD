# An application created through test driven development

[![pipeline status](https://gitlab.com/sbansa1/restful/badges/master/pipeline.svg)](https://gitlab.com/sbansa1/restful/commits/master)

##Setup
`In your command line`
```bash
$ mkdir flask-dd 
cd flask-tdd-docker
$ mkdir app
$ python3.8 -m venv env
$ source env/bin/activate

```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Flask and Flask-RestPlus.

```bash
Create a new project and install Flask along with Flask-RESTPlus:


$(env) pip install Flask 
$(env) pip install flask-restplus

```
## To start or instantiate an app
```python
"""Make a __init__.py in the app folder"""

from flask import Flask
from flask_restplus import Api, Resource

"""TO instantiate a flask application"""
app = Flask(__name__)
api = Api(app)

"""Make a class to test the endpoint"""

class Hello(Resource):
     def get(self):
       return {"message": "Hello World !"}
      
#Add the resource 
app.add_resource(Hello,"/hello")

```
```python
# Create a manage.py in the root of your application directory. Manage.py aids f the arguments you pass to manage.py as subcommands. 
# It is your tool for executing many Flask-specific tasks -- starting a new app within a project, 
# running the development server, running your tests...etc.
# It is also an extension point where you can access custom commands
# you write yourself that are specific to your apps.


# You must be wondering what the FlaskGroup does. 
# FlaskGroup extends the normal cli with commands related to Flask app.

from flask.cli import FlaskGroup
from app import app

cli = FlaskGroup(app)

"""we see the use of cli further when we create and seed the database"""

if __name__=='__main__':
   cli() 
```

```bash
# Export the flask app by running the server

$(env) export FLASK_APP=app/__init__.py
$(env) python run manage.py #(This will start the flask server)
```
```text
When you run the app you will get the following output
```
```text
Navigate to http://localhost:5000/hello in your browser. You should see:
```
```json5
{"message" : "Hello World!"}
```
```text
Kill the server and make a config.py file in the app directory, 
so that we can define the environment variables to configure our app
```
```python
# config.py

class BaseConfig(object):
    TESTING = False

class DevelopmentConfig(BaseConfig):
     pass

class TestingConfig(BaseConfig):
    TESTING = True 
    
class ProductionConfig(BaseConfig):
     pass
```
```text
Please update the app/__init__.py file to set the development config on
initialization or init.
```
```python

from flask import Flask
from flask_restplus import Api,Resource

# instantiate the Flask app

app = Flask(__name__) 
api = Api(app)

#Set Configuration
app.config.from_object('app.config.DevelopmentConfig')

class Hello(Resource):
     def get(self):
       return {"message": "Hello World !"}
      
#Add the resource 
app.add_resource(Hello,"/hello")
```
```text
Now set the FLASK_ENV=development which will enable the debug mode.
It is very helpful in the development mode because if you make 
any changes to the code it will span the server automatically.
```
```bash
$(env) export FLASK_APP=app/__init__.py
$(env) export FLASK_ENV=development
$(env) python manage.py run
```

```
* Serving Flask app "app/__init__.py" (lazy loading)
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 448-890-901
```
```text
Now, every time you make changes to the code. The server will automatically span up by itself.

Kill the Server and Commit the code on Github.
```
```
#Follow the below directions to commit the code on Github.
# Make Sure you have a Github Account.

# (venv) saurabhs-MacBook-Pro:RestApi saurabhbansal$ git init
# (venv) saurabhs-MacBook-Pro:RestApi saurabhbansal$ git add .
# (venv)saurabhs-MacBook-Pro:RestApi saurabhbansal$ git commit -m "First commit"
# (venv) saurabhs-MacBook-Pro:RestApi saurabhbansal$ git remote add origin {Your Github Repo Url}
# (venv) saurabhs-MacBook-Pro:RestApi saurabhbansal$ git push -u origin master
```

```text
Now we will add a Dockerfile in the root. 
```
```dockerfile
# We are just intructing docker to pull the official base image
FROM python:3.8.0-alpine 

#Sets the working directory inside the docker container
WORKDIR /usr/src/app

#Sets the Environment
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

#We want to copy the requirements.txt file from our app root to 
#the root of the docker container

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

#Add the application 
COPY . . 

CMD python manage.py run -h 0.0.0.0
```

```text
Now let me explain what are we trying to achieve by setting the 
Docker file.

1) Why Alpine based Image?
   - Because the Alpine based image is light weighted. 
   Hence keep our docker image slim. It is indeed a good
   practise to use Alpine based images because
   
   - Storage is expensive it helps us to save on storage costs 
   leading to less hosting costs. 
   - Quicker builds, faster downloads and execution time.
   - Since the image is light-weighted it is deployed easily and at
   a faster pace.
   - More robust and more secure because it is not ladened with 
   numerous packages and libraries.
   
   "FROM" - Keyword which instructs Docker to pull base image.
   
   WORKDIR - Sets the working directory inside the docker container
   
   Note: Depending on the Environment you may want to execute this 
   command
   
   ENV PYHONDONTWRITEBYTECODE 1
   (Dont want the complied source code files i.e. class files
   to be copied to the disk hence it prevents python to write it.
   ENV PYTHONUNBUFFERED 1
   (Prevents python from buffering stdout and stderr)
   
   RUN mkdir -p {path to workdir}{/../../}
   
   COPY ./requirements.txt /usr/src/app/requirements.txt
   or COPY ./requirements.txt .
   
   RUN pip install -r requirements.txt 
   Downloads all the packages and dependencies we need
   for project execution(POM file)
   
   COPY . . (copies or add the entire app from our directory to
   the docker container)
   
   CMD python manage.py run -h 0.0.0.0
   (Executes the FLASK APP inside the docker container simulating
   the Localhost or on the localhost)
   
   Like the .gitignore file, the .dockerignore file lets you exclude 
   specific files and folders from being copied over to the image.
```
```text
WHY USE DOCKER COMPOSE?

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. To learn more about all the features of Compose, see the list of features.

Compose works in all environments: production, staging, development, testing, as well as CI workflows. You can learn more about each case in Common Use Cases.

Using Compose is basically a three-step process:

Define your app’s environment with a Dockerfile so it can be reproduced anywhere.

Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.

Run docker-compose up and Compose starts and runs your entire app.
```
```text
Build a docker-compose.yml file in the application root
```
```bash
version:'3.7'
   
   services:
     users:
       build:
         context: .
         dockerfile: Dockerfile
       volumes: '.:/usr/src/app'
       port:
          - 5001:5000
       enviroment:
        - FLASK_ENV=development
        - APP_SETTINGS=app.config.DevelopmentConfig  
```
```text
The docker-compose file may need some formatting.

Tags :-
Version - decides the structure of the docker-compose file

services - defines the services we want to build.
users: name of the service
build: build the service
context - Either a path to a directory containing a Dockerfile, or a url to a git repository.
dockerfile - Dockerfile in the root which will be initialized to build the service
Volume -the volume is used to mount the code into the container. This is a must for a development environment in order to update the container whenever a change to the source code is made. Without this, you would have to re-build the image each time you make a change to the code.
port - defines the port where the application will be running
enviroment - defines the environemnt of our application

Later we will add more things to the Dockerfile as well as to the
compose file when we build our database.

When your fire the container for the first time it may take a little 
time to set up things but all the subsequent builds will require less time
as docker caches the results.

```
```bash
docker-compose up -d --build

will build the image in the container with all the subsequent 
dependencies.

Want to ensure the proper config was loaded? Add a print statement to __init__.py, right before the route handler, as a quick test:

```
```python
"import sys"
"print(app.config, file=sys.stderr)"
"Then view the Docker logs:"

"$ docker-compose logs"
```

##SET UP POSTGRES SQL

```bash
# To set up postgres

pip install flask-sqlalchemy
pip install psycopg2-binary
pip freeze>requirements.txt
(will updates the requirements.txt file)
```

```python
##Make a config.py file in the app dir
import os  # new


class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # new


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')  # new


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  # new
```

```python

# app/__init__.py

from flask import Flask
from flask_restplus import Api,Resource
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class Hello(Resource):
     def get(self):
       return {"message": "Hello World !"}
      
#Add the resource 
app.add_resource(Hello,"/hello")

```
```python
# Now make a model.py file and make a model class

from app import db

class User(db.Model):
  id = db.Column(db.Integer,primary_key=True,autoincrement=True)
  username = db.Column(db.String(128), nullable=False)
  email_id = db.Column(db.String(128),nullable=False)
  active = db.Column(db.Boolean,default=True,nullable=False)
  
  def __init__(self,username,email_id):
    self.username = username
    self.email_id = email_id

```

```text
Create a folder named as db in your app directory
make a file 

create.sql
CREATE DATABASE users_dev;
CREATE DATABASE users_test;
Create a docker file

```
```dockerfile
#Docker File for PostGres


#Pulls the official Base Image
FROM postgres:12.1-alpine

#Run Create sql on Init
ADD create.sql /docker-entrypoint-initdb.d
```
```text
As,The default postgres user and database are created in the entrypoint with initdb.
Here, we extend the official Postgres image (again, an Alpine-based image) by adding create.sql to the "docker-entrypoint-initdb.d" directory in the container. 
This file will execute on init.

Initialization scripts
If you would like to do additional initialization in an image derived from this one, add one or more *.sql, *.sql.gz, or *.sh scripts under **/docker-entrypoint-initdb.d** (creating the directory if necessary). After the entrypoint calls initdb to create the default postgres user and database, it will run any *.sql files, run any executable *.sh scripts, and source any non-executable 
*.sh scripts found in that directory to do further initialization before starting the service.

```
#update the docker file 
```dockerfile

FROM python:3.8.0-alpine

#Dependencies for postgres running in the container
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

COPY . . 

CMD python manage.py run -h 0.0.0.0


```text
Now we will update the docker-compose.yml file

```

```
```bash
version : '3.7'

services:
    users:
       build:
         context: . 
            dockerfile: Dockerfile
            entrypoint: ['/usr/src/app/entrypoint.sh']
       volume : '.:/usr/src/app'
       port:
         5001:5000
        enviroment:
          - FLASK_APP=app/__init__.py
          - FLASK_ENV=development
          - APP_SETTINGS=app.config.DevelopmentConfig
          - DATABASE_URL="postgresql://postgres:postgres@users-db:5432/users_dev"
          - DATABASE_TEST_URL="postgresql://postgres:postgres@users-db:5432/users_test"
        depends_on:
          - users_db
    users_db:
        build:
          context: ./app/db
            dockerfile:Dockerfile
          expose:
             - 5432
          environment:
             - POSTGRES_USER = postgres 
             - POSTGRES_PASSWORD = postgres

```

## Now why use net cat? 
The netcat utility. Often referred to as a Swiss army knife of networking tools, this versatile command can assist you in monitoring, testing, and sending data across network connections.
 
One of the most common uses for netcat is as a port scanner. so the netcat scans the postgres port if its free or not to check if the instance of postgres server is running or not on that particular port.

Although netcat is probably not the most sophisticated tool for the job (nmap is a better choice in most cases), it can perform simple port scans to easily identify open ports.

We do this by specifying a range of ports to scan, as we did above, along with the -z option to perform a scan instead of attempting to initiate a connection.

For instance, we can scan all ports up to 1000 by issuing this command:

    netcat -z -v domain.com 1-1000

Along with the -z option, we have also specified the -v option to tell netcat to provide more verbose information.
For more information 
```html
<a src="https://www.digitalocean.com/community/tutorials/how-to-use-netcat-to-establish-and-test-tcp-and-udp-connections-on-a-vps"></a>
```
```bash

#!/bin/sh

echo "Initializing post gres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done
## the loop will run until the post gres service is not up and running.

echo "Postgres server started.. ."

python manage.py run -h 0.0.0.0
```
```python
#Please go in the manage.py

from flask.cli import FlaskGroup
from app import app,db

cli = FlaskGroup(app)

@cli.command('recreate_db')
def recreate_db():
  db.drop_all()
  db.create_all()
  db.session.commit()


if __name__=='__main__':
   cli() 
```

#We will follow the TDD(Test Driven Development) process to build our application.
```
What is TDD?
TDD is a development process where we write the test cases first and make sure they fail before writing the functional 
part of an application.

Why TDD? 
Because it helps write a more robust and cleaner code.
```