# Pet store API tests
This is a growing demo suite of tests using Python.
It tests a sample pet store API found at [Swagger Pet Store API](http://petstore.swagger.io)

## To run the tests
### Install python and pytest
[Install Python here](https://www.python.org/downloads/)
To install pytest, once you've installed Python:
> pip3 install pytest

### Run the tests
Simply run
> pytest

To kick off the test suite.

## About the tests
There's a couple of test suites
**test_pet_crud.py** will test a basic create-read-update-delete flow for the pets API
**test_create_pet.py** will do some data validation tests on the create pet endpoint