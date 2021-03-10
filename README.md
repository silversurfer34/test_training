# Welcome to the Tests training  
## Demos  
### Unit performance tests using timeit  
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
### Integration performance tests using locust
For the purpose of this demo we will test a simple REST API hosted locally in a docker image

#### Prerequisites:
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

Optionaly an actual online rest API can be tested  
`https://petstore.swagger.io/`
***
### System test or end to end (e2e) test with selenium
#### Prerequisites:
* install selenium libraries
  `pip install selenium`
* install selenium web driver https://www.selenium.dev/documentation/en/selenium_installation/installing_webdriver_binaries/
for chrome https://sites.google.com/a/chromium.org/chromedriver/getting-started

* install selenium ide https://www.selenium.dev/selenium-ide/

#### Selenium test with IDE
Launch selenium IDE and start recording a search on python.org  
Save the test  
Play the test
#### Selenium test from python
Open and run selenium_test.py  
Demo of ide code generation

## Pytest tutorial
### Prerequisites

* Work in virtual environment
  ```
  python - m venv .venv
  .venv\scripts\activate
  ```
  or (depending on the sytem)
  `source .venv/bin/activate`
* Install the requirements

`pip install requirements.txt`

* Install the development requirements

`pip install requirements_dev.txt`

## Work to do
Run the tests

`pytest tests`

### 1st exercise
Open tests\stringlib_test.py and analyse the code  
Follow the instructions  
Once all done check the test's coverage using this command line
```
pytest tests --cov=simple --cov-report html
```
### 2nd exercise

Use Test Driven Development to code those requirements.  
TDD principles:  
1. Write the test
2. Run the test -> it must fail
3. Code the minimum feature to make the test pass  
   3.1 Check the produced code is fully covered by test
4. Move on to the next requirement
5. At one stage refactor your code to make it simpler/nicer, to remove duplication

Requirements:
- Easy one to start : Write a function that returns "Hello world"
- Create a calculator (a class or a module or a file) with those methods:
  - add to compute the sum of two values 
  - substr to compute the substraction of two values
  - multiply to compute the multiplication of two values
  - divide to compute the division of one value by the other  
  - average to compute the average of a list of values (should not fail with 0 values)
  
Ask if requirements are not clear enough  
Once done, refactor you code to have substr calling add; divide calling multiply; average calling add and divide 

## Integration tests tutorial
### Prerequisites
- Install postman https://www.postman.com/downloads/
- Download swagger file from https://petstore.swagger.io/

## Work to do
Open Postman
Import the swagger file (API definition file)

Launch Find Pets By status
Update it to test the result of the request
In test tabs add :
```
pm.test("Status test", function () {
    pm.response.to.have.status(200);
});
```

Do the same for the Add a new pet query
Duplicate this query and create a negative test (wrong id) with expected 500 code as answer

Open a runner tab, launch the full test suite and check the results  
It can also be done without the GUI, in command line using newman, exmaple using the docker image of newman  
`docker run -v /mnt/d/Projects/test_training/postman:/etc/newman -t postman/newman:ubuntu run "tests.json"`

