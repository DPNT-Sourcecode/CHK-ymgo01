from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple, Optional

INVALID_SKUS = -1

deal = namedtuple("SpecialOffer", ["quantity", "offer_price"])

@dataclass
class Item:
    sku: str
    unit_price: int
    special_deal: Optional[NamedTuple]


SKU_TO_ITEM = {
    "A": Item("A", 50, deal(3, 130)),
    "B": Item("B", 50, deal(3, 130)),
    "C": Item("C", 50),
    "D": Item("D", 50),
}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    pass


