import requests
import pytest

@pytest.mark.parametrize("nome, username, email,user_id,status_esperado",
    [
        ("Cris1", "cris1", "cris1@test.com",1, 200),
        ("Cris2", "cris2", "cris2@test.com",2, 200),
        ("Cris3", "cris3", "cris3@test.com",3, 200),
        ("Cris4", "cris4", "cris4@test.com",999,500)
        
    ]
)
def test_update_user( nome, username, email,user_id,status_esperado,base_url):
    dados_usuario = {
        
        "name": nome,
        "username": username,
        "email": email

            }
    response = requests.put(
        f"{base_url}/users/{user_id}",
        json=dados_usuario
    )

    
    print(response.status_code)
    print(response.text)
    assert response.status_code == status_esperado

    if status_esperado == 200:
        dados_resposta = response.json()

        assert dados_resposta["name"] == nome
        assert dados_resposta["username"] == username
        assert dados_resposta["email"] == email
                         