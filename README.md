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

```
```text
Now we will update the docker-compose.yml file
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

![TDD](https://miro.medium.com/max/950/1*IbHgZrKYCUSeIbL_PywObQ.png)

```
What is TDD?
TDD is a development process where we write the test cases first and make sure they fail before writing the functional 
part of an application. Reason behind it is that you leads to a more bug free code. The entire process is iterable. 

It is also known as Red-Green-Refactor cycle because you write the test cases and make sure it fails.
Then you write the functional code and refactor it until the test cases pass.

Why TDD? 

Because it helps write a more robust and cleaner code.

TDD acts as a specification and helps the other developers learn about our code 
by looking at the test cases.

It helps the team members provide confidence to make changes to the code because if the test 
cases fail the changes wont be deployed to the production. 

````
(Now what happens when you deploy your code with following a TDD approach)

![TDD not implemented](https://miro.medium.com/max/1300/1*NH3pXnzK5WxWa2mHH1vRZQ.jpeg) 

Surprise Surprise Surprise ! ! ! 
```text

Now we will use pytest over unittest library to write the test cases.

```
Install Pytest
```bash
pip install pytest
```
```text
Make a test folder in your app directory and create the following files:
 - __init__.py
 - conftest.py
 - test_config.py
 - test_hello.py
 - pytest.ini

```
In the conftest.py import pytest. The conftest file sets up the configuration required for testing. 
One thing about pytest it will find the test files only if the test_* or *_test is followed. 
One basic advantage of using pytest overy unitest is that one does not have to set up things again 
and again. 

We can do that by the use of fixtures. Fixtures help us to re use the same test object based on the scope defined.
By default, the default scope is set to function. 

function - once per test function
class - once per test class
module - once per test module
session - once per test session

To execute a test suite we do a set up and tear down if we use unittest lib we need to do it seprately with pytest
we can do that in the same function.

Make sure your files start with the name test_* or end with *_test. now if you are making a test class make sure you class name
begins with the word Test. ?

or if you are defining a function your name should begin with test...


def test_app():
   return ""

Please follow the code below in conftest.py
```python
#conftest.py

import pytest
from app import create_app
from app.extensions import db

@pytest.fixture(scope='module')
def test_app():
  #set up 
  app = create_app()
  app.config.from_object('app.config.TestingConfig')
  with app.app_context():
    yield app #this is where the testing begins and once it tests all the test cases it kills the object which is the tear down phase.

@pytest.fixture(scope="module")
def test_database():
   db.create_all()
   yield db
   db.session.remove()
   db.drop_all()

```
Now the fixtures will be available to the module without having to import them. 
Fixtures acts as an injector inside the test functions.

Now please add pytest==5.3.1 in requirements.txt
or simply run pip>requirements.txt and it will auto update with the latest dependencies


We need to re-build the Docker images since requirements are installed at build time rather than run time:
```bash
docker-compose up -d --build
```
With the containers up and running, run the tests:
```bash
docker-compose exec users -m pytest "app/tests"

```
You should see:

======================================== test session starts ========================================
platform linux -- Python 3.8.0, pytest-5.3.1, py-1.8.0, pluggy-0.13.1
rootdir: /usr/src/app/project/tests, inifile: pytest.ini
collected 0 items

=================================== no tests ran in 0.06 seconds ====================================


# TESTS
let's add a few tests to test_config.py:
```python

import os

def test_development_config(test_app):
  test_app.config.from_object('app.config.DevelopmentConfig')
  assert test_app.config.get('SECRET_KEY') == 'myprecious'
  assert not test_app.config.get('TESTING')
  assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')
 
def test_testing_config(test_app):
   test_app.config.from_object('app.config.TestingConfig')
   assert test_app.config['SECRET_KEY'] == 'myprecious'
   assert not test_app.config['DEVELOPMENT']
   assert not test_app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
   assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_TEST_URL')
   
def test_production_config(test_app):
  test_app.config.from_object('app.config.ProductionConfig')
  assert test_app.config.get('SECRET_KEY') == 'myprecious'
  assert not test_app.config.get('TESTING')
  assert test_app.config['SQLALCHEMY_DATABASE_URI'] == os.environ.get('DATABASE_URL')
  
```
Now run the docker command again 
```bash
docker-compose exec users pytest "app/tests"

```
and you should receive an assertion Error because we will have to add
the secret key in our config.py file.

Now go ahead and add SECRET_KEY='myprecious" to the config.py in the 
BaseConfig class.

RE RUN THE TESTS and IT SHOULD PASS
```bash
docker-compose exec users pytest 'app/tests'
```
So you may have realized that the above tests are unit tests and not the functional tests.

#UNIT TESTING

UNIT TESTING is a level of software testing where individual units/ components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output. In procedural programming, a unit may be an individual program, function, procedure, etc. In object-oriented programming, the smallest unit is a method, which may belong to a base/ super class, abstract class or derived/ child class. (Some treat a module of an application as a unit. This is to be discouraged as there will probably be many individual units within that module.) Unit testing frameworks, drivers, stubs, and mock/ fake objects are used to assist in unit testing.

# FUNCTIONAL TESTS
Functional tests are the test which tests your business logic to see if your code is meeting the business objectives i.e. checks if they meet the requirements specifications.

Writing test cases for functional tests is a bit complicated but you will get a hang of it. 

```python
#test_hello.py
import json

def test_hello(app_test):
   client = app_test.test_client()
   response = client.get("/hello")
   assert response.status_code == 200
   data = json.loads(response.data.decode())
   assert 'hello' in data.get('message')

```
Execute the below command

```bash
docker-compose exec users pytest "app/tests" -k hello 

```
which test will run when we execute the above command?

#Flask-Blueprints

A blueprint is a template for generating a "section" of a web application. You can think of it as a mold:

#Refer to the Image below

![mold](https://i.stack.imgur.com/kd1XW.jpg)

You can take the blueprint and apply it to your application in several places. Each time you apply it the blueprint will create a new version of its structure in the plaster of your application.





This is a simple mold for working with trees - it says that any application that deals with trees should provide access to its leaves, its roots, and its rings (by year). By itself, it is a hollow shell - it cannot route, it cannot respond, until it is impressed upon an application:







Once it is created it may be "impressed" on the application by using the register_blueprint function - this "impresses" the mold of the blueprint on the application at the locations specified by url_prefix.

For more Information follow the link 

![Blueprint](http://exploreflask.com/en/latest/blueprints.html)

# How to define a flask blueprint
```python

from flask import Blueprint

hello = Blueprint('hello',__name__)
"""This is how you define the blueprints"""

```

Now we will use Flask Factory to create and register blueprint. 
# What is FLASK FACTORY?
The Application Factory pattern is an app structure where our app entry point sits atop all other parts of our application, and pieces together the various modules or Blueprints that might make our app.
The reason we use Flask Application Factory as it has something to do with the Flask Application Context which is a
collection of all the modules and python files which wraps them together. 

```python

#app/__init__.py
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
   app = Flask(__name__)
   app_settings  = os.getenv('APP_SETTINGS')
   app.config.from_object(app_settings)
   
   db.init_app(app)
   
   '''you can register the blue print here '''
   
   # Include the from... to prevent circular imports
   #app.register_blueprint(name of blueprint)
   
   return app # which is an app instance.
   
   """you can also structure it better"""
```
```python
#manage.py

from app import create_app
from flask.cli import FlaskGroup

app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__=="__main__":
  cli()

```
```python
#app/api/__init__.py

from flask import Blueprint
from flask_restplus import Api

user_blu = Blueprint('user_blu',__name__)
user_api = Api(user_blu)


```


```python
#app/api/model.py

from app import db

class User(db.Model):
  '''Create user model'''
  __tablename__='users'
  
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(128), nullable=False)
  email_id = db.Column(db.String(128),nullable=False)
  active = db.Column(db.Boolean, default=True,nullable=False)
  
  def __init__(self,*args,**kwargs):
   super(User,self).__init__(*args,**kwargs)

```

Create a view file
```python
from app.api import api_ping_blueprint
from flask_restplus import Resource, fields




class Mock(Resource):
    def get(self):
     return {'message':'Hello world'}
```
```text
We wont proceed with writing the code before writing the test cases first
```

now go in the app/tests/functional

```python
#app/tests/functional
import json

def test_add_user(test_app, test_database):
  """test add user"""
  
  client = test_app.test_client()
  data = dict(username="Saurabh.bnss0123", email="Saurabh.bnss0123@gmail.com")

  resp = client.post('/users',data=json.dumps(data),content_type='application/json')
  assert resp.status_code == 201
  data = json.loads(resp.data.decode())
  assert 'saurabh.bnss0123@gmail.com' in data.get('email')


def test_user_already_exists(test_app, test_database):
    """Duplicate User"""

    user_data = dict(username="Saurabh", email="Saurabh.bnss0123@gmail.com")

    client = test_app.test_client()

    client.post("/users", data=user_data, content_type="application/json")

    response = client.post(
        "/users", data=json.dumps(user_data), content_type="application/json"
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Sorry. That email already exists." in data["message"]
```
Mentioned above are the two cases where in the first case we are adding the user. 
2) we are just chekcing if the user already exists in the second scenario.

```bash
docker-compose exec users pytest "app/tests" 

#you shall see the tests will fail. Now we will go ahead and implement the code.
```
```python

from app.api import api_ping_blueprint
from flask_restplus import Resource, fields
from flask import request

user_model = api_ping_blueprint.model('User',{'id' : fields.Integer(readOnly=True),
                                               'username':fields.String(required=True),
                                                'email':fields.String(required=True)})

class UserResource(Resource):
   def post(self):
    """Post request to handle or add user"""
    
    data = request.get_json()
    
    

```