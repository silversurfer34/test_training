# Welcome to the Tests training
##Demos
###Unit performance tests using timeit
For the purpose of this demo we will compare several sort algorithms using timeit
#### Prerequisites:
* Python installed
#### Timeit
timeit will measure the time spent to execute some statements.
We will use repeat method from timeit
```
times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=1)
```
Timeit measure the time spent to run `stmt` executed `number` times.

repeat method runs it `repeat` times and return an array of measured time.

#### Measuring performances
`perfo/perfo.py` contains the code to run and measure the sorting algorithm.

The sorting algorithm are defined in `simple/sort.py`. You can define your own and test it
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

#### Locust
Open locust_files\my_locust_file.py

Run locust
```locust -f locust_files/my_locust_file.py --host http://localhost:8080```

Optionaly an actual online rest API can be tested `https://petstore.swagger.io/`
***
###System test or e2e test with selenium
#### Prerequisites:
* install selenium libraries
  `pip install selenium`
* install selenium web driver https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/
for chrome https://sites.google.com/a/chromium.org/chromedriver/getting-started

* install selenium ide https://www.selenium.dev/selenium-ide/

#### Selenium test with IDE
#### Selenium test from python

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
