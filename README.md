# Welcome to the Tests training
##Demos
###Unit performance tests using timeit
***
###Integration performance tests using locust
For the purpose of this demo we will test a simple REST API hosted locally in a docker image

####Prerequisites:
* Docker installed https://docs.docker.com/docker-for-windows/install/
* Check if docker is properly installed
```
docker run "hello-world"
```
* Retrieve swaggerapi/petstore docker image
```
docker pull swaggerapi/petstore
```
* Run the container and check it is correctly serving the API at http://localhost:8080
```
docker run -d -e SWAGGER_HOST=http://localhost -e SWAGGER_BASE_PATH=/v2 -p 8080:8080 swaggerapi/petstore
```

####Configure locust
Open locust_files\my_locust_file.py

Run locust
```locust -f locust_files/my_locust_file.py --host http://localhost:8080```

Optionaly an actual online rest API can be tested `https://petstore.swagger.io/`
***
## Pytest tutorial
### Prerequisites

First install the requirements

`pip install requirements.txt`

The development requirements

`pip install requirements_dev.txt`

## Work to do
Run the tests

`pytest`

### 1st exercise
Open stringlib_test.py and add the missing tests

### 2nd exercise
