import pytest
import sys
from pathlib import Path
sys.path.append(str(Path().resolve()))
from app import app


@pytest.fixture(scope='module')
def test_app():
    return app.test_client()
