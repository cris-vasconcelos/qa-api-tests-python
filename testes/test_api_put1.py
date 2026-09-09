import requests


def test_atualizar_usuario(base_url):
    dados_usuario = {
        "name": "Cris Atualizada1",
        "username": "cris",
        "email": "cris.atualizada1@example.com"
    }

    response = requests.put(
        f"{base_url}/users/1",
        json=dados_usuario
    )
    
    assert response.status_code == 200      

    dados = response.json()

    assert dados ["id"]==1
    assert dados ["name"] == "Cris Atualizada1"
    assert dados ["username"] == "cris"
    assert dados ["email"] == "cris.atualizada1@example.com"
   


