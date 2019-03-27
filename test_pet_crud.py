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
	assert response.json()['name']==pet_name, "Expected pet name to be {} but received {}".format(pet_name,response.json()['name'])

def test_get_pet():
	print("Getting pet..."+str(pet_id))
	response=petstore_queries.get_pet_by_id(pet_id)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)
	assert response.json()['name']==pet_name, "Expected pet name to be {} but received {}".format(pet_name,response.json()['name'])

def test_update_pet():
	new_pet_name = fake.name()
	print("Updating pet..."+str(pet_id)+" "+str(new_pet_name))
	response=petstore_queries.update_pet(pet_id,new_pet_name)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)
	assert response.json()['name']==new_pet_name, "Expected pet name to be {} but received {}".format(new_pet_name,response.json()['name'])

def test_delete_pet():
	print("Deleting pet..."+str(pet_id))
	response=petstore_queries.delete_pet(pet_id)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)

def test_get_deleted_pet():
	print("Getting pet..."+str(pet_id))
	response=petstore_queries.get_pet_by_id(pet_id)
	assert response.status_code==404, "Expected status 404 but received {}".format(response.status_code)