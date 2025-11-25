# 🚀 Pilataxi AI Application - CI/CD Project

[![CI/CD Pipeline](https://github.com/Padme2003/examen-practico-1/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/Padme2003/examen-practico-1/actions/workflows/ci-cd.yml)

Aplicación Flask con IA implementada con un flujo completo de CI/CD usando GitHub Actions, Docker y despliegue automático a VPS.

## 📋 Descripción

Esta aplicación web desarrollada con Flask implementa funcionalidades de análisis de texto con IA. El proyecto demuestra un pipeline completo de integración y entrega continua (CI/CD) que:

- ✅ Ejecuta pruebas automatizadas
- 🐳 Construye imágenes Docker
- 📦 Publica en GitHub Container Registry (GHCR)
- 🚀 Despliega automáticamente a un servidor VPS

## 🌐 Acceso a la Aplicación

La aplicación está desplegada y accesible en:

**URL:** https://pilataxi.byronrm.com

## 🏗️ Arquitectura del Proyecto

```
examen-practico-1/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline CI/CD
├── app.py                      # Aplicación Flask principal
├── test_app.py                 # Pruebas automatizadas
├── requirements.txt            # Dependencias Python
├── Dockerfile                  # Configuración Docker
├── docker-compose.yml          # Stack de deployment
├── .dockerignore              # Archivos excluidos de Docker
├── .gitignore                 # Archivos excluidos de Git
└── README.md                  # Este archivo
```

## 🔧 Tecnologías Utilizadas

- **Backend:** Flask 3.0.0
- **IA/ML:** Transformers, PyTorch
- **Testing:** Pytest
- **Containerización:** Docker
- **CI/CD:** GitHub Actions
- **Registry:** GitHub Container Registry (GHCR)
- **Servidor Web:** Gunicorn
- **Despliegue:** VPS con Docker Compose
- **Proxy Reverso:** Traefik (con SSL/TLS automático)

## 📦 Características de la Aplicación

### Endpoints disponibles:

1. **`GET /`** - Página principal con interfaz web interactiva
2. **`GET /health`** - Health check del servicio
3. **`GET /api/info`** - Información sobre la aplicación
4. **`POST /api/process`** - Procesar texto con IA

### Funcionalidades de IA:

- Análisis de sentimiento (positivo, negativo, neutral)
- Conteo de palabras y caracteres
- Detección de palabras clave emocionales
- Respuestas en tiempo real

## 🚀 Pipeline CI/CD

### Flujo Automático

El pipeline se ejecuta automáticamente en cada push a las ramas configuradas:

1. **Test Stage** 🧪
   - Instalación de dependencias
   - Ejecución de pruebas con pytest
   - Validación de código

2. **Build & Push Stage** 🐳
   - Construcción de imagen Docker
   - Etiquetado: `pilataxi:1.0.5` y `pilataxi:latest`
   - Publicación en GitHub Container Registry

3. **Deploy Stage** 🚀
   - Conexión SSH al VPS
   - Pull de la nueva imagen
   - Actualización del stack Docker
   - Reinicio de servicios

## 🐳 Docker

### Construir imagen localmente

```bash
docker build -t pilataxi:1.0.5 .
```

### Ejecutar localmente

```bash
docker run -p 5000:5000 pilataxi:1.0.5
```

### Usar docker-compose

```bash
docker compose up -d
```

## 🧪 Pruebas

### Ejecutar pruebas localmente

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests
pytest test_app.py -v
```

### Cobertura de pruebas

Las pruebas incluyen:
- ✅ Validación de endpoints
- ✅ Health checks
- ✅ Procesamiento de IA
- ✅ Detección de sentimientos
- ✅ Manejo de errores

## 📊 Imagen en GitHub Packages

La imagen Docker está disponible en GitHub Container Registry:

```bash
docker pull ghcr.io/padme2003/pilataxi:1.0.5
```

**Detalles de la imagen:**
- Nombre: `pilataxi`
- Versión: `1.0.5`
- Registry: GitHub Container Registry (GHCR)
- Base: Python 3.11-slim

## 🔐 Configuración de Secrets

Para que el pipeline funcione correctamente, configurar los siguientes secrets en GitHub:

- `VPS_HOST` - IP o dominio del servidor VPS
- `VPS_USERNAME` - Usuario SSH del VPS
- `VPS_SSH_KEY` - Llave privada SSH para autenticación
- `VPS_PORT` - Puerto SSH (opcional, default: 22)

## 🌍 Despliegue en VPS

### Requisitos del VPS

- Docker instalado
- Docker Compose instalado
- Red Traefik configurada (`traefik-network`)
- Directorio del proyecto: `/opt/pilataxi`

### Configuración del Stack

El archivo `docker-compose.yml` incluye:
- Etiquetas de Traefik para routing automático
- SSL/TLS con Let's Encrypt
- Configuración de red compartida
- Health checks

### Subdominio

El servicio está configurado para ser accesible en:
- **Dominio:** pilataxi.byronrm.com
- **Protocolo:** HTTPS (certificado automático)
- **Puerto:** 443 (HTTPS estándar)

## 📈 Monitoreo

### Verificar estado del servicio

```bash
# Health check
curl https://pilataxi.byronrm.com/health

# Información de la aplicación
curl https://pilataxi.byronrm.com/api/info
```

### Logs en el VPS

```bash
# Ver logs del contenedor
docker logs pilataxi-app

# Seguir logs en tiempo real
docker logs -f pilataxi-app
```

## 👨‍💻 Desarrollo Local

### Setup inicial

```bash
# Clonar repositorio
git clone https://github.com/Padme2003/examen-practico-1.git
cd examen-practico-1

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python app.py
```

La aplicación estará disponible en: http://localhost:5000

## 📝 Uso de la API

### Ejemplo de request

```bash
curl -X POST https://pilataxi.byronrm.com/api/process \
  -H "Content-Type: application/json" \
  -d '{"text": "Este es un día maravilloso y excelente"}'
```

### Respuesta esperada

```json
{
  "success": true,
  "result": "📊 Análisis de IA completado 😊\n\nTexto analizado: \"Este es un día maravilloso y excelente\"\n\nEstadísticas:\n- Palabras: 6\n- Caracteres: 38\n- Sentimiento detectado: positivo\n- Palabras positivas encontradas: 2\n- Palabras negativas encontradas: 0\n\nConclusión: El texto tiene un tono positivo."
}
```

## 🎯 Rúbrica del Proyecto

### Cumplimiento de requisitos:

- ✅ **[1 pt]** Uso correcto de Git y repositorio
  - Estructura clara del proyecto
  - Commits organizados con mensajes descriptivos
  - Gestión adecuada de ramas

- ✅ **[2 pts]** Imagen publicada en GHCR
  - Pipeline construye la imagen correctamente
  - Etiquetado apropiado (pilataxi:1.0.5)
  - Visible en GitHub Packages

- ✅ **[1 pt]** Pipeline CI funcional
  - Tests ejecutándose automáticamente
  - Build completándose sin errores
  - Validación de código

- ✅ **[6 pts]** Pipeline CD funcional
  - Conexión automática al VPS sin intervención manual
  - Actualización de imagen automática
  - Aplicación ejecutándose correctamente
  - Despliegue completamente automatizado

## 🔄 Workflow de Desarrollo

1. Hacer cambios en el código
2. Commit y push a la rama
3. GitHub Actions ejecuta automáticamente:
   - Tests
   - Build de imagen
   - Push a GHCR
   - Deploy a VPS
4. Verificar en https://pilataxi.byronrm.com

## 📚 Recursos Adicionales

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)

## 👤 Autor

**Pilataxi**
- Proyecto: Examen Práctico CI/CD
- Versión: 1.0.5

## 📄 Licencia

Este proyecto fue desarrollado como parte de un examen práctico de CI/CD.

---

⭐ **Proyecto CI/CD completo con deployment automático** ⭐
