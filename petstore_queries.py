import requests

BASE_URL="https://petstore.swagger.io/v2"

def get_pet_by_id(pet_id):
	print("Getting pet..."+str(pet_id))
	return requests.get(BASE_URL+"/pet/"+str(pet_id))