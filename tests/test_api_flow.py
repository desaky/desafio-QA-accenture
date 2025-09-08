import pytest
import requests
import uuid

BASE_URL = "https://demoqa.com"
USERNAME = f"user_{uuid.uuid4().hex[:6]}"
PASSWORD = "Password123!"

@pytest.fixture(scope="session")
def user_data():
    return {"userName": USERNAME, "password": PASSWORD}

def test_create_user(user_data):
    res = requests.post(f"{BASE_URL}/Account/v1/User", json=user_data)
    assert res.status_code in (201, 200), f"create user failed: {res.status_code} {res.text}"
    pytest.user_id = res.json().get("userID")
    assert pytest.user_id, "userID não retornado"

def test_generate_token(user_data):
    res = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=user_data)
    assert res.status_code == 200, f"generate token failed: {res.status_code} {res.text}"
    pytest.token = res.json().get("token")
    assert pytest.token, "token não retornado"

def test_authorize(user_data):
    res = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=user_data)
    assert res.status_code == 200
    assert res.json() is True

def test_list_books():
    res = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert res.status_code == 200
    books = res.json().get("books", [])
    assert len(books) > 0
    pytest.books = books

def test_add_books_to_user():
    selected = pytest.books[:2]
    isbns = [{"isbn": b["isbn"]} for b in selected]
    headers = {"Authorization": f"Bearer {pytest.token}"}
    body = {"userId": pytest.user_id, "collectionOfIsbns": isbns}
    res = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=body, headers=headers)
    assert res.status_code in (201, 200), f"add books failed: {res.status_code} {res.text}"

def test_get_user_details():
    headers = {"Authorization": f"Bearer {pytest.token}"}
    res = requests.get(f"{BASE_URL}/Account/v1/User/{pytest.user_id}", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert "books" in data
    assert len(data["books"]) >= 2
