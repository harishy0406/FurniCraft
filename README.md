# FurniCraft — Furniture Company Management System (Streamlit)

## Overview
FurniCraft is a demo project to showcase software reuse and multiple design patterns:
- **Abstract Factory** (core): create families of related products (Chair, Sofa, Table) for different styles (Modern, Victorian).
- **Singleton**: single global shopping cart instance.
- **Strategy**: pluggable pricing/discount strategies.
- **Decorator**: add optional features (warranty, cushions) to products.
- **Prototype**: clone furniture sets for comparison.

The app contains a Landing Page with a background image and a smooth transition to the main UI. There's an Admin panel where you can add new products to categories; these are persisted to `data/products.json`.

## Project structure 

```
furnicraft/
├── main.py                    # Streamlit entrypoint (Landing + Main UI + Admin)
├── factories/
│   ├── abstract_factory.py
│   ├── modern_factory.py
│   └── victorian_factory.py
├── products/
│   ├── base.py
│   └── product_registry.py    # dynamic registry loader/saver
├── patterns/
│   ├── singleton_cart.py
│   ├── strategy_pricing.py
│   ├── decorator_features.py
│   └── prototype_set.py
├── data/
│   └── products.json         # initial products (created at first run if missing)
├── assets/
│   ├── bg/                   # suggested place to store background images
│   └── placeholders/         # placeholder images for products
├── requirements.txt
└── README.md
```

---

## Run Instructions
1. Ensure Python 3.8+ is installed.
2. `python -m venv venv` & activate it.
3. `pip install -r requirements.txt`
4. `streamlit run main.py`


