import requests

BASE_URL="https://petstore.swagger.io/v2/pet/"

def get_pet_by_id(pet_id):
	return requests.get(BASE_URL+str(pet_id))

def create_pet(pet_id,pet_name):
	petInfo={
		"id": pet_id,
		"name": pet_name,
		"photoUrls": [
			"string"
		],
		"status": "available"
	}
	return requests.post(BASE_URL,json=petInfo)

def create_pet_without_name(pet_id):
	petInfo={
		"id": pet_id,
		"photoUrls": [
			"string"
		],
		"status": "available"
	}
	return requests.post(BASE_URL,json=petInfo)

def create_pet_without_photo_urls(pet_id,pet_name):
	petInfo={
		"id": pet_id,
		"name": pet_name,
		"status": "available"
	}
	return requests.post(BASE_URL,json=petInfo)

def update_pet(pet_id,new_pet_name):
	petInfo={
		"id": pet_id,
		"name": new_pet_name
	}
	return requests.put(BASE_URL,json=petInfo)

def delete_pet(pet_id):
	return requests.delete(BASE_URL+str(pet_id))