import requests
import pytest

@pytest.mark.parametrize("user_id, status_esperado,nome_esperado",
    [
    (1, 200,"Leanne Graham"), 
     (999,404,None)
    ]
)

def test_consultar_usuario(user_id, status_esperado,nome_esperado,base_url):
    response = requests.get(
         f"{base_url}/users/{user_id}"

         #dados = response.json=()
    )

    assert response.status_code == status_esperado

    if status_esperado == 200:
        dados = response.json()
        assert dados["name"] == nome_esperado
    
    
