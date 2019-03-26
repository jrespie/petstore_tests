import pytest
import petstore_queries

def test_get_pet():
	response=petstore_queries.get_pet_by_id(0)
	assert response.status_code==200, "Expected status 200 but received {}".format(response.status_code)
