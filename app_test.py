from nose.tools import assert_true
import requests
import string
import random

BASE_URL = "http://localhost:5000"

def id_generator(size=7, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

TEST_NAME ="TestUser "+ id_generator()

class NewAddressBook(): 
    def __init__(self, value):
        self.value = value

def test_open():
    response = requests.get('%s/' % (BASE_URL))
    assert_true(response.ok)

def test_add_new_person_missing_parameter():
    "Test adding a new person with missing parameter"
    payload = {'name': TEST_NAME, 'address': 'Test Adress'}
    response = requests.post('%s/address-books' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)
    assert_true('request items cannot be left blank' in response.json()['errorMessage'])

def test_add_new_person_invalid_name():
    "Test adding a new person with invalid name"
    payload = {'name': "TEST_NAME 123", 'address': 'Test Adress', 'phone': '0905123913129'}
    response = requests.post('%s/address-books' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)
    assert_true("'name' is invalid" in response.json()['errorMessage'])


def test_add_new_person_invalid_phone():
    "Test adding a new person with invalid phone"
    payload = {'name': TEST_NAME, 'address': 'Test Adress', 'phone': '09051213129'}
    response = requests.post('%s/address-books' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)
    assert_true("'phone' is invalid" in response.json()['errorMessage'])

def test_add_new_person_invalid_email():
    "Test adding a new person with invalid email"
    payload = {'name': TEST_NAME, 'address': 'Test Adress', 'phone': '0905123913129', 'email':'testt@testt'}
    response = requests.post('%s/address-books' % (BASE_URL), json=payload)
    assert_true(response.status_code == 400)
    assert_true("'email' is invalid" in response.json()['errorMessage'])

def test_add_new_person():
    "Test adding a new person"
    payload = {'name': TEST_NAME, 'address': 'Test Adress', 'phone': '0905123913129'}
    response = requests.post('%s/address-books' % (BASE_URL), json=payload)
    assert_true(response.status_code == 201)

def test_get_person():
    "Test getting the person"
    response = requests.get('%s/address-books/%s' % (BASE_URL,TEST_NAME) )
    assert_true(response.status_code == 200)

def test_update_person():
    "Test updating the person"
    payload = {'email':'testt@testt.com'}
    response = requests.put('%s/address-books/%s' % (BASE_URL,TEST_NAME) , json=payload)
    assert_true(response.status_code == 200)

def test_delete_person():
    "Test deleting the person"
    response = requests.delete('%s/address-books/%s' % (BASE_URL,TEST_NAME) )
    assert_true(response.status_code == 204)