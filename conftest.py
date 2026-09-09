#fixture - Uma fixture é uma forma de preparar algo que os 
# testes precisam e depois disponibilizar isso para eles.
import pytest
from config import BASE_URL

@pytest.fixture
def base_url():
    return BASE_URL
