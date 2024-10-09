# Account test

## Contents of this file

 - Introduction
 - Requirements
 - Installation and usage
 - Endpoints

## Introduction

Accounttest is a project to simulate login and different roles permission to users access the resources.

## Requirements

 - Python 3.11+
 - Postgres as database
 - Docker to create the images (optional)

## Installation and usage

To run the project locally, we need to follow some steps:

 - First we need to have python 3.11 installed. You can use the lib pyenv to control different python versions.
 - Is optional and recommended to use a virtualenv with the python 3.11. By doing that, you can isolate you projects environments.
 - Install the projects dependencies inside the SRC directory with run the command `pip install -r dependencies/requirements-dev.txt`.
 - Rename the `.env_sample` file to `.env`.
 - Having a Postgres running locally, create two databases called `accounttest` and `accounttest_test`. If you change the default Postgres port, change the value in the `.env` file.
 - Create the database tables running the migration command inside the src/api dir: `flask db upgrade`
 - Run the project locally with `flask run`
 - If you want to run using Docker, run the command in the project root dir `docker-compose up`. It will build and start an image of the project and a Postgres as well. Make sure you don't have another postgres instance running in the port 5342.
- to run the unit tests and check the coverage, run the command in root dir `make test`

## Endpoints

Now that the project is running locally in the address http://localhost:5000 (or http://localhost:5001 with the docker image), we are going to do requests to interact with the application.

### Requests
- POST /api/v1/token: Pass in the request body two parameters `username` and `password` to authenticate and get the authorization token. You can generate a token for `user` and another one for `admin`
- GET /api/v1/user: With the token generated previously for the `user`, add it to the Authorization header in the following format: `Authorization: Bearer {token}`.
- GET /api/v1/admin: With the token generated previously for the `admin`, add it to the Authorization header in the following format: `Authorization: Bearer {token}`

### In order to ease the tests, there are two json files with the Postman collections used to test the endpoints.

- Go to Postman, on the top left side click the button `Import`. Select the file and proceed. To the same process with the two files.
- In case you run the project in a different port, change its value in the Postman environments section. 

### Responses
- 200: if the request is successfull
- 401: if you try to authenticate with invalid credentials
- 403: if you try to access and endpoint with divergence between the token and endpoint role

