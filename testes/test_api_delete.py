import requests


def test_deletar_usuario(base_url):
    response = requests.delete(
        f"{base_url}/users/1"
    )
    assert response.status_code == 200