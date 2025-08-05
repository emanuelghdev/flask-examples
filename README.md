# Ejemplos de proyectos Flask

Este repositorio incluye una colección de proyectos y ejemplos prácticos desarrollados con Flask, diseñados para aprender y experimentar diferentes patrones de diseño, arquitecturas y funcionalidades comunes en APIs RESTful y microservicios.

## 📦 `API RESTful/`

Una API RESTful desarrollada con Flask de gestión de tareas, con documentación Swagger automática.

### Ejecutar:

```bash
cd API RESTful
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Por defecto, la API se ejecutará en http://localhost:5000

<div align="center">
    <img src="docs/img/API RESTful chart.png" width="80%" alt="API RESTful architecture chart"/>
    <img src="docs/img/API RESTful example.png" width="80%" alt="API RESTful json example"/>
</div>

---

## 📦 `microservicios/`

Pequeño sistema compuesto por 5 microservicios en Flask, orquestados con Docker Compose.

### Ejecutar:

```bash
cd microservicios
docker-compose up --build
```

Los servicios quedarán disponibles en los puertos:

- municipio: http://localhost:5000

- geo: http://localhost:5001

- meteo: http://localhost:5002

- demo: http://localhost:5003

- orquestación: http://localhost:5004

<div align="center">
    <img src="docs/img/Microservicio example.png" width="80%" alt="Microservicio json example"/>
</div>