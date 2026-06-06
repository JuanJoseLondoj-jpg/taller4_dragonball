"""
ingesta.py
----------
Extrae personajes, planetas y transformaciones de la Dragon Ball API
y los almacena en MongoDB tal como llegan (RAW), sin modificación.

Base de datos : taller4_db
Colección     : raw_data
"""

import requests
from pymongo import MongoClient

# ─── Configuración ────────────────────────────────────────────────────────────
MONGO_URI  = "mongodb://localhost:27017/"
DB_NAME    = "taller4_db"
COLLECTION = "raw_data"
PAGE_SIZE  = 50
TARGET_MIN = 100

ENDPOINTS = [
    {"url": "https://dragonball-api.com/api/characters",     "tipo": "character"},
    {"url": "https://dragonball-api.com/api/planets",        "tipo": "planet"},
    {"url": "https://dragonball-api.com/api/transformations","tipo": "transformation"},
]

# ─── Conexión a MongoDB ───────────────────────────────────────────────────────
print("Conectando a MongoDB...")
client     = MongoClient(MONGO_URI)
db         = client[DB_NAME]
collection = db[COLLECTION]

collection.drop()
print(f"Colección '{COLLECTION}' limpiada (o creada nueva).")

# ─── Extracción paginada por endpoint ────────────────────────────────────────
all_records = []

for endpoint in ENDPOINTS:
    url  = endpoint["url"]
    tipo = endpoint["tipo"]
    page = 1
    print(f"\nDescargando {tipo}s desde {url} ...")

    while True:
        params   = {"limit": PAGE_SIZE, "page": page}
        response = requests.get(url, params=params, timeout=15)

        if response.status_code != 200:
            print(f"  Error HTTP {response.status_code} en página {page}. Deteniendo.")
            break

        data = response.json()

        # Algunos endpoints devuelven lista directa, otros con "items"
        if isinstance(data, list):
            items       = data
            total_pages = 1
        else:
            items       = data.get("items", [])
            meta        = data.get("meta", {})
            total_pages = meta.get("totalPages", 1)

        if not items:
            print(f"  Página {page} vacía. Fin de datos.")
            break

        for item in items:
            item["_tipo"] = tipo

        all_records.extend(items)
        print(f"  Página {page}/{total_pages} — acumulados total: {len(all_records)} registros")

        if page >= total_pages:
            break

        page += 1

# ─── Validación de volumen ────────────────────────────────────────────────────
print(f"\nTotal de registros descargados: {len(all_records)}")
if len(all_records) < TARGET_MIN:
    print(f"ADVERTENCIA: se descargaron menos de {TARGET_MIN} registros.")
else:
    print(f"✓ Se superó el mínimo requerido de {TARGET_MIN} registros.")

# ─── Inserción RAW en MongoDB ─────────────────────────────────────────────────
if all_records:
    result = collection.insert_many(all_records)
    print(f"\n✓ Insertados {len(result.inserted_ids)} documentos en '{DB_NAME}.{COLLECTION}'.")
else:
    print("No hay datos para insertar.")

# ─── Verificación final ───────────────────────────────────────────────────────
count = collection.count_documents({})
print(f"✓ Conteo final en MongoDB: {count} documentos.")
print("\nIngesta completada exitosamente.")

client.close()
