import requests
url = "https://gorest.co.in/public/v2/users"
headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization":"Bearer bf67544e9e62a4b3bcb8ac474e4b737abeb7c8571cb64c743447e40999693a4e"}
def test_post_request():
    # endpoint = "/public/v2/users"
    data = {
        "name":"Test QA",
        "gender":"male",
        "email":"test1@test.com",
        "status":"active"}
    response = requests.post(url = url ,headers = headers, json=data)
    assert response.status_code == 201
    user_id = response.json().get("id")
    assert user_id is not None
    print("New user ID:", user_id)
test_post_request()
