#test that the "create pet" endpoint fails when required fields are not specified
#note that these tests fail - the API should throw an error, but instead it still creates an invalid record

import pytest
import petstore_queries
from faker import Faker
import random

pet_id = random.randint(1,9999)
fake = Faker()
pet_name = fake.name()

def test_create_pet_without_name():
	response=petstore_queries.create_pet_without_name(pet_id)
	assert response.status_code==405, "Expected status 405 but received {}".format(response.status_code)

def test_create_pet_without_photo_urls():
	response=petstore_queries.create_pet_without_photo_urls(pet_id,pet_name)
	assert response.status_code==405, "Expected status 405 but received {}".format(response.status_code)