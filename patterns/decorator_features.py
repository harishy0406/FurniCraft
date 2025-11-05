# Simple decorator example: wrap a product dict and add extras

def add_warranty(product, years=2, cost=20):
    p = product.copy()
    p['desc'] = p.get('desc','') + f" + {years}-year warranty"
    p['price'] = p.get('price',0) + cost
    p['id'] = p.get('id') + f"_w{years}"
    return p


def add_cushion(product, cost=15):
    p = product.copy()
    p['desc'] = p.get('desc','') + " + Cushions"
    p['price'] = p.get('price',0) + cost
    p['id'] = p.get('id') + "_cush"
    return p