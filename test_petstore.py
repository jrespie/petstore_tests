import pytest
import petstore_queries
from faker import Faker
import random

pet_id = random.randint(1,9999)
fake = Faker()
pet_name = fake.name()

def test_create_pet():
	response=petstore_queries.create_pet(pet_id,pet_name)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)
	assert response.name==pet_name, "Expected pet name to be {} but received {}".format(pet_name,response.name)

def test_get_pet():
	response=petstore_queries.get_pet_by_id(pet_id)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)
	assert response.name==pet_name, "Expected pet name to be {} but received {}".format(pet_name,response.name)

