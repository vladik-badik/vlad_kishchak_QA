import pytest
import requests

url = "https://gorest.co.in/public/v2/users/"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer 44fce7ff7128750b3b76796296aee2ee02db8e8b0b00a2ee5a8800be74a99a66"
}

@pytest.fixture
def create_user():
    data = {
        "name": "Testqwerty123",
        "gender": "male",
        "email": "mailforspam1992120312@test.com",
        "status": "active"
    }
    response = requests.post(url=url, headers=headers, json=data)
    assert response.status_code == 201
    user_id = response.json().get("id")
    assert user_id is not None
    print("New user ID:", user_id)
    yield user_id

    delete_response = requests.delete(url=url + str(user_id), headers=headers)
    assert delete_response.status_code == 204
    print("User", user_id, "deleted.")

def test_post_article_request(create_user):
    user_id = create_user
    endpoint = "/posts"
    text = {
        'title': 'Test',
        'body': 'Hi my name is Goivany Georgio, but everybody calls me Georgio'
    }
    response = requests.post(url=url + str(user_id) + endpoint, headers=headers, json=text)
    assert response.status_code == 201
    assert len(response.json()) > 0
    print("Success")
    print(response.json())

