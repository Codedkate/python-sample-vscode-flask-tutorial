
from hello_app.webapp import app


def test_mock():
    assert True


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_about_page():
    client = app.test_client()
    response = client.get("/about/")
    assert response.status_code == 200


def test_hello_page():
    client = app.test_client()
    response = client.get("/hello/Catherine")
    assert response.status_code == 200
    assert b"Catherine" in response.data
