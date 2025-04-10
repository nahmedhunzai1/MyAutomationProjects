import requests
import random
import json
import string


def generate_random_string(length=100):
    letters = string.ascii_letters  # Generates a string of all letters (both lowercase and uppercase)
    return ''.join(random.choice(letters) for _ in range(length))

random_tag_name = generate_random_string(20)

def generate_random_email(length=100):
    letters = string.ascii_letters  # Generates a string of all letters (both lowercase and uppercase)
    return ''.join(random.choice(letters) for _ in range(length)) + '@abc.com'
random_email = generate_random_email(12)


#base_url :
base_url = "https://uat.api.whoz.co"

#auth_token
# auth_token_production = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5haG1lZCt0ZXN0dXNlcjAxQHRlY2hub2xvZ3lyaXZlcnMuY29tIiwiaWQiOiIxY2MyN2U4NS1jNjU0LTQzZGYtYjY1YS04YWJjMTdlZTAyMzkiLCJ1c2VyUHJvZmlsZUlkIjoiMWNjMjdlODUtYzY1NC00M2RmLWI2NWEtOGFiYzE3ZWUwMjM5IiwicHVycG9zZSI6ImJhc2ljLWp3dCIsImlhdCI6MTcyNzg3NjU5NiwiZXhwIjoxNzI5MTk0MTk2fQ.GphTl1xZc71FZ65BxU46d0ImMiJS4l9K5LfD13FCmSk"

auth_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5haG1lZCt0cjJAdGVjaG5vbG9neXJpdmVycy5jb20iLCJpZCI6IjE5Y2Q3NzhjLTc0YjItNGVkMS1iMjI4LWExOGNjOWY0ODAzNiIsInVzZXJQcm9maWxlSWQiOiIxOWNkNzc4Yy03NGIyLTRlZDEtYjIyOC1hMThjYzlmNDgwMzYiLCJwdXJwb3NlIjoiYmFzaWMtand0IiwiaWF0IjoxNzI4MTYzMTM5LCJleHAiOjE3Mjk0ODA3Mzl9.ESQWjJspTvbIx7_812JF2F9QkoLQHfIlhA4RcZiJKdg"

def get_request():
    url = base_url + "/contacts"
    headers = {"Authorization": auth_token}
    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")

    # Print the response text for debugging
    print("Response Text:", response.text)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print ("Json response body:" , json_str)

def post_request():
    url = base_url + "/contacts/bulk"
    print ("Post URL :" +url)
    headers = {"Authorization": auth_token}
    data = {
        "contacts": [
            {
                "firstName": random_tag_name,
                "lastName": random_tag_name,
                "email": random_email,
                "address": "Street 51, F6-4 Islamabad",
                "phone": "03440512054"
            }
        ],
        "tags": []
    }
    response = requests.post(url, json=data, headers=headers)
    print("The status code is ", response.status_code)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    first_name = json_data[0]['ownerMaintainedContactProfile']['firstName']
    print("The pertty response is", json_str)

    # assert first_name in json_data[0]['ownerMaintainedContactProfile']
    # assert json_data["name"] == random_tag_name

    contact_id = json_data[0]['contactUserProfile']["id"]
    print(contact_id)
    return contact_id


def put_request():
    url = base_url + "/users/profile"
    print("Put URL :" + url)
    headers = {"Authorization": auth_token}
    data = {

        {
            "firstName":random_tag_name ,
            "lastName": random_tag_name,
            "mobileNumber": "0980980980980",
            "profileVisibility": [],
            "address": {
                "country": "Pakistan",
                "city": "Islamabad",
                "state": "Punjab",
                "province": "Punjab",
                "zipCode": "46000"
            },
            "userEmails": []
        }
    }

    response = requests.put(url, json=data, headers=headers)
    print("Status code of the put request is ", response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("Json data of put request", json_str)
    # print("json response body of the put request :", json_str)
    # assert json_data["id"] == contact_id
    # assert json_data["firstName"] == "Nadeem Updated"

#get_request()
#post_request()
# put_request()



