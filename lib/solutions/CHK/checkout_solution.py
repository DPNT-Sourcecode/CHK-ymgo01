from collections import namedtuple
from dataclasses import dataclass
from typing import Dict, NamedTuple, Optional

INVALID_SKUS = -1

deal = namedtuple("SpecialOffer", ["quantity", "offer_price"])

@dataclass
class Item:
    sku: str
    unit_price: int
    special_deal: Optional[NamedTuple]


SKU_TO_ITEM = {
    "A": Item("A", 50, deal(3, 130)),
    "B": Item("B", 30, deal(2, 45)),
    "C": Item("C", 20),
    "D": Item("D", 15),
}


def skus_valid(skus: str) -> bool:
    '''Determine whether the input is valid
    '''
    return all([sku in SKU_TO_ITEM for sku in skus])


def count_each_item(skus: str) -> Dict[str, int]:
    sku_count = {}
    for sku in skus:
        if sku in sku_count:
            sku_count[sku] += 1
        else:
            sku_count[sku] = 1


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    if not skus_valid(skus):
        return INVALID_SKUS
    item_to_quantity_map = count_each_item(skus)



