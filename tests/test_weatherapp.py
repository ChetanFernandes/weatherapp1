import pytest
from unittest.mock import Mock, patch
from app import app as flask_app


def test_index():
    client = flask_app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200


@patch('app.requests.get')
def test_weatherapp(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'name': 'TestCity'}
    mock_get.return_value = mock_response

    client = flask_app.test_client()
    resp = client.post('/weatherapp', data={'city': 'London', 'appid': 'fake', 'units': 'metric'})
    text = resp.get_data(as_text=True)
    assert 'data: TestCity' in text
