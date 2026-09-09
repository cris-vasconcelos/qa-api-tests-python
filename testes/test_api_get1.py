
import requests


def test_consultar_usuario(base_url):
    response = requests.get(
         f"{base_url}/users/1"
    )

    assert response.status_code == 200

    dados = response.json()
    
    assert dados["id"] == 1
    assert dados["name"] == "Leanne Graham"
    assert dados["username"] == "Bret"
    assert dados["email"] == "Sincere@april.biz"

def test_consultar_usuario_inexistente ():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/999"
    )

    assert response.status_code == 404

    