from collections import namedtuple
from dataclasses import dataclass
from typing import Optional

@dataclass
class Item:
    sku: str
    unit_price: int
    special_deal: Optional[tuple]

INVALID_SKUS = -1
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    pass

