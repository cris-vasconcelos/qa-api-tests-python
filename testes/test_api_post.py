import requests

def test_criar_usuario(base_url):
    dados_usuario = {
    "name": "Maria Cristina",
    "username": "maria_cristina",
    "email": "maria.cristina@example.com"
}
    response = requests.post(
        f"{base_url}/users/",
        json=dados_usuario
    )
    assert response.status_code == 201
    dados = response.json()
    assert dados["name"] == "Maria Cristina"
    assert dados["username"] == "maria_cristina"
    assert dados["email"] == "maria.cristina@example.com"