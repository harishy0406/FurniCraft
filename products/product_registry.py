import json
from pathlib import Path
from products.base import Product

DATA_PATH = Path(__file__).resolve().parents[1] / 'data' / 'products.json'

# Simple dynamic registry that loads product definitions from JSON and exposes them.

def ensure_data_file():
    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_PATH.exists():
        # write the default content (kept small)
        default = {
            "Modern": {
                "Chair": [{"id": "modern_chair_1", "name": "Modern Chair", "price": 120, "desc": "Sleek and minimal design", "image": "assets/placeholders/MC.jpg"}],
                "Sofa": [{"id": "modern_sofa_1", "name": "Modern Sofa", "price": 300, "desc": "Compact 3-seater with neutral tones", "image": "assets/placeholders/MS.jpg"}],
                "Table": [{"id": "modern_table_1", "name": "Modern Table", "price": 180, "desc": "Glass top table with steel legs", "image": "assets/placeholders/MT.jpg"}]
            },
            "Victorian": {
                "Chair": [{"id": "victorian_chair_1", "name": "Victorian Chair", "price": 200, "desc": "Classic wooden armchair with carvings", "image": "assets/placeholders/VC.jpg"}],
                "Sofa": [{"id": "victorian_sofa_1", "name": "Victorian Sofa", "price": 450, "desc": "Elegant velvet sofa with ornate legs", "image": "assets/placeholders/VS.jpg"}],
                "Table": [{"id": "victorian_table_1", "name": "Victorian Table", "price": 280, "desc": "Solid oak table with antique finish", "image": "assets/placeholders/VT.jpg"}]
            }
        }
        with open(DATA_PATH, 'w') as f:
            json.dump(default, f, indent=2)


def load_products():
    ensure_data_file()
    with open(DATA_PATH, 'r') as f:
        return json.load(f)


def save_products(data):
    ensure_data_file()
    with open(DATA_PATH, 'w') as f:
        json.dump(data, f, indent=2)