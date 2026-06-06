# Taller Unidad 4 — APIs Públicas, MongoDB y EDA
**Curso:** Bases de Datos para Ciencia de Datos — Universidad de Antioquia  
**Docente:** Miguel Ramos García

---

## Descripción del Proyecto

Este proyecto simula un flujo real de Ciencia de Datos en tres fases:

1. **Extracción** de datos desde la Dragon Ball API pública.
2. **Almacenamiento RAW** en MongoDB sin modificar los datos originales.
3. **Análisis Exploratorio (EDA)** con visualizaciones y estadísticas sobre los personajes.

---

## API Utilizada

**Dragon Ball API** — `https://dragonball-api.com`

Provee información sobre personajes del universo Dragon Ball:  
nombre, raza, género, afiliación, poder Ki base y Ki máximo.

Se extraen **más de 100 personajes** mediante paginación automática.

---

## Estructura del Repositorio

```
taller4_dragonball/
├── ingesta.py          # Extracción de la API y carga a MongoDB
├── analisis.ipynb      # Notebook con EDA completo (5 insights + 3 gráficos)
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos excluidos del repositorio
└── README.md           # Este archivo
```

---

## Cómo Ejecutarlo

### 1. Prerrequisitos

- Python 3.10+
- MongoDB instalado y corriendo en `localhost:27017`
- Instalar dependencias:

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la ingesta

```bash
python ingesta.py
```

Esto descargará todos los personajes disponibles (≥100) y los guardará en:  
- Base de datos: `taller4_db`  
- Colección: `raw_data`

### 3. Ejecutar el análisis

```bash
jupyter notebook analisis.ipynb
```

Abre el notebook y ejecuta todas las celdas en orden (`Cell > Run All`).

---

## Resultados del EDA

El análisis genera **3 gráficos** y **5 insights** sobre los personajes:

- Distribución por género (Pie Chart)
- Top 8 razas más frecuentes (Barras)
- Top 6 afiliaciones (Barras horizontales)

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.10+ | Lenguaje principal |
| requests | Consumo de la API REST |
| pymongo | Conexión y operaciones con MongoDB |
| pandas | Manipulación de datos |
| matplotlib / seaborn | Visualizaciones |
| Jupyter Notebook | Entorno de análisis interactivo |
