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

Se consumen tres endpoints para superar el mínimo de 100 registros:

| Endpoint | Descripción | Registros |
|---|---|---|
| `/api/characters` | Personajes del universo Dragon Ball | 58 |
| `/api/planets` | Planetas del universo Dragon Ball | 20 |
| `/api/transformations` | Transformaciones de los personajes | 43 |
| | **Total insertado en MongoDB** | **121** |

El EDA se realiza únicamente sobre los **personajes**, que son los registros con información más completa (raza, género, afiliación, ki).

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

Descarga personajes, planetas y transformaciones (121 registros en total) y los guarda en:
- Base de datos: `taller4_db`
- Colección: `raw_data`

### 3. Ejecutar el análisis

```bash
jupyter notebook analisis.ipynb
```

Abre el notebook y ejecuta todas las celdas con `Cell > Run All`.

---

## Resultados del EDA

El análisis se realiza sobre los 58 personajes y genera **3 gráficos** y **5 insights**:

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
