
PRICE_TABLE = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
}

OFFERS = {
    'A': 130,
    'B': 45
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    item_count_map = {}

    for s in skus:
        if s not in PRICE_TABLE: # also handle case if there is no sku inputted
            return -1

        if s not in item_count_map:
            item_count_map[s] = 1
        else:
            item_count_map[s] += 1
    
    item_count
