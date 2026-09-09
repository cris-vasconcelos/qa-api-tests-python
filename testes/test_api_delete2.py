import requests
import pytest

@pytest.mark.parametrize("user_id",
    [ 
        1
    ]
)
def test_delete(base_url,user_id):
    response = requests.delete(
        f"{base_url}/users/1"
    )

    assert response.status_code == 200
    