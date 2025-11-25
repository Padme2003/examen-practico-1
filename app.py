from flask import Flask, request, jsonify, render_template_string
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# HTML template simple para la interfaz
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pilataxi AI App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .input-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input[type="text"], textarea {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.9);
            color: #333;
            font-size: 16px;
        }
        button {
            width: 100%;
            padding: 15px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            cursor: pointer;
            transition: background 0.3s;
        }
        button:hover {
            background: #45a049;
        }
        .response {
            margin-top: 20px;
            padding: 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 8px;
            min-height: 100px;
        }
        .hidden {
            display: none;
        }
        .version {
            text-align: center;
            margin-top: 20px;
            opacity: 0.8;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 Pilataxi AI Application</h1>
        <p style="text-align: center; margin-bottom: 30px;">
            Aplicación Flask con IA - CI/CD Pipeline
        </p>

        <div class="input-group">
            <label for="userInput">Ingresa tu mensaje:</label>
            <textarea id="userInput" rows="4" placeholder="Escribe algo aquí..."></textarea>
        </div>

        <button onclick="processText()">Procesar con IA</button>

        <div id="response" class="response hidden">
            <h3>Respuesta de IA:</h3>
            <p id="responseText"></p>
        </div>

        <div class="version">
            Versión: 1.0.5 | Pilataxi CI/CD Project
        </div>
    </div>

    <script>
        async function processText() {
            const input = document.getElementById('userInput').value;
            const responseDiv = document.getElementById('response');
            const responseText = document.getElementById('responseText');

            if (!input.trim()) {
                alert('Por favor ingresa un mensaje');
                return;
            }

            responseText.textContent = 'Procesando...';
            responseDiv.classList.remove('hidden');

            try {
                const response = await fetch('/api/process', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ text: input })
                });

                const data = await response.json();

                if (data.success) {
                    responseText.textContent = data.result;
                } else {
                    responseText.textContent = 'Error: ' + data.error;
                }
            } catch (error) {
                responseText.textContent = 'Error al procesar la solicitud: ' + error.message;
            }
        }
    </script>
</body>
</html>
"""

# Simulación simple de procesamiento de IA
def process_with_ai(text):
    """
    Simula procesamiento de IA.
    En producción, aquí se usaría un modelo real de transformers.
    """
    # Análisis de sentimiento simple
    positive_words = ['bueno', 'excelente', 'genial', 'feliz', 'amor', 'maravilloso']
    negative_words = ['malo', 'terrible', 'triste', 'odio', 'horrible', 'pésimo']

    text_lower = text.lower()
    positive_count = sum(word in text_lower for word in positive_words)
    negative_count = sum(word in text_lower for word in negative_words)

    if positive_count > negative_count:
        sentiment = "positivo"
        emoji = "😊"
    elif negative_count > positive_count:
        sentiment = "negativo"
        emoji = "😞"
    else:
        sentiment = "neutral"
        emoji = "😐"

    word_count = len(text.split())
    char_count = len(text)

    response = f"""
    📊 Análisis de IA completado {emoji}

    Texto analizado: "{text}"

    Estadísticas:
    - Palabras: {word_count}
    - Caracteres: {char_count}
    - Sentimiento detectado: {sentiment}
    - Palabras positivas encontradas: {positive_count}
    - Palabras negativas encontradas: {negative_count}

    Conclusión: El texto tiene un tono {sentiment}.
    """

    return response.strip()

@app.route('/')
def home():
    """Página principal de la aplicación"""
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    """Endpoint de health check"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.5',
        'service': 'pilataxi-ai-app'
    }), 200

@app.route('/api/process', methods=['POST'])
def process():
    """Endpoint para procesar texto con IA"""
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'No se proporcionó texto para procesar'
            }), 400

        text = data['text']

        if not text.strip():
            return jsonify({
                'success': False,
                'error': 'El texto está vacío'
            }), 400

        result = process_with_ai(text)

        app.logger.info(f"Texto procesado exitosamente: {text[:50]}...")

        return jsonify({
            'success': True,
            'result': result
        }), 200

    except Exception as e:
        app.logger.error(f"Error al procesar texto: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/info')
def info():
    """Información sobre la aplicación"""
    return jsonify({
        'name': 'Pilataxi AI Application',
        'version': '1.0.5',
        'description': 'Aplicación Flask con IA para CI/CD Pipeline',
        'author': 'Pilataxi',
        'endpoints': {
            '/': 'Página principal',
            '/health': 'Health check',
            '/api/process': 'Procesar texto con IA (POST)',
            '/api/info': 'Información de la aplicación'
        }
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
