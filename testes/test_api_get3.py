import requests
import pytest

usuarios = [
    {
        "user_id": 1,
        "status_esperado": 200,
        "nome_esperado": "Leanne Graham"
    },
    
        {
            "user_id":999,
            "status_esperado":404,
            "nome_esperado": None
        }
    ]
@pytest.mark.parametrize("usuario", usuarios)
def test_consultar_usuario(usuario, base_url):
    user_id = usuario["user_id"]
    status_esperado = usuario["status_esperado"]
    nome_esperado = usuario["nome_esperado"]

    response = requests.get(
        f"{base_url}/users/{user_id}"
    )

    assert response.status_code == status_esperado

    if status_esperado == 200:
        dados = response.json()
        assert dados["name"] == nome_esperado