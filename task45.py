import requests
url = "https://gorest.co.in/public/v2/users/"
headers = {"Accept":"application/json",
           "Content-Type":"application/json",
           "Authorization":"Bearer bf67544e9e62a4b3bcb8ac474e4b737abeb7c8571cb64c743447e40999693a4e"}

def test_post_user_request():
    data = {
        "name":"Testqwerty12",
        "gender":"male",
        "email":"mailforspam@test.com",
        "status":"active"}
    response = requests.post(url = url ,headers = headers, json=data)
    assert response.status_code == 201
    user_id = response.json().get("id")
    assert user_id is not None
    print("New user ID:", user_id)
    print(response.json())
    return user_id
user_id = test_post_user_request()

def test_post_article_request():
    id = str(user_id)
    endpoint = "/posts"
    text={'title': 'Test',
          'body': 'Hi my name is Goivany Georgio, but everybody calls me Georgio'}
    response = requests.post(url= url+id+endpoint, headers = headers , json= text)
    assert response.status_code == 201
    assert len(response.json()) > 0
    print("Success")
    print(response.json())

test_post_article_request()