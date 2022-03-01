import pytest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))
from app import app


@pytest.fixture(scope='module')
def test_app():
    return app.test_client()
