import pytest
import json
from app import app

@pytest.fixture
def client():
    """Crear un cliente de prueba para la aplicación Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Probar que la página principal carga correctamente"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Pilataxi AI Application' in response.data

def test_health_endpoint(client):
    """Probar el endpoint de health check"""
    response = client.get('/health')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['version'] == '1.0.5'
    assert data['service'] == 'pilataxi-ai-app'

def test_info_endpoint(client):
    """Probar el endpoint de información"""
    response = client.get('/api/info')
    assert response.status_code == 200

    data = json.loads(response.data)
    assert data['name'] == 'Pilataxi AI Application'
    assert data['version'] == '1.0.5'
    assert 'endpoints' in data

def test_process_endpoint_success(client):
    """Probar el procesamiento de texto exitoso"""
    response = client.post('/api/process',
                           data=json.dumps({'text': 'Este es un texto de prueba excelente'}),
                           content_type='application/json')

    assert response.status_code == 200

    data = json.loads(response.data)
    assert data['success'] is True
    assert 'result' in data

def test_process_endpoint_no_text(client):
    """Probar el endpoint sin proporcionar texto"""
    response = client.post('/api/process',
                           data=json.dumps({}),
                           content_type='application/json')

    assert response.status_code == 400

    data = json.loads(response.data)
    assert data['success'] is False
    assert 'error' in data

def test_process_endpoint_empty_text(client):
    """Probar el endpoint con texto vacío"""
    response = client.post('/api/process',
                           data=json.dumps({'text': '   '}),
                           content_type='application/json')

    assert response.status_code == 400

    data = json.loads(response.data)
    assert data['success'] is False

def test_process_positive_sentiment(client):
    """Probar detección de sentimiento positivo"""
    response = client.post('/api/process',
                           data=json.dumps({'text': 'Este día es excelente y maravilloso'}),
                           content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'positivo' in data['result'].lower()

def test_process_negative_sentiment(client):
    """Probar detección de sentimiento negativo"""
    response = client.post('/api/process',
                           data=json.dumps({'text': 'Este día es terrible y horrible'}),
                           content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'negativo' in data['result'].lower()

def test_process_neutral_sentiment(client):
    """Probar detección de sentimiento neutral"""
    response = client.post('/api/process',
                           data=json.dumps({'text': 'El cielo es azul'}),
                           content_type='application/json')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] is True
