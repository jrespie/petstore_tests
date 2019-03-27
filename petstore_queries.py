import requests

BASE_URL="https://petstore.swagger.io/v2"

def get_pet_by_id(pet_id):
	return requests.get(BASE_URL+"/pet/"+str(pet_id))

def create_pet(pet_id,pet_name):
	petInfo={
		"id": pet_id,
		"name": pet_name,
		"status": "available"
	}
	return requests.post(BASE_URL+"/pet",json=petInfo)

def update_pet(pet_id,new_pet_name):
	petInfo={
		"id": pet_id,
		"name": new_pet_name
	}
	return requests.put(BASE_URL+"/pet",json=petInfo)