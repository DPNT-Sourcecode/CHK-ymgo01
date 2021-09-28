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
    '''Count how many instances of each sku we see
    '''
    sku_count = {}
    for sku in skus:
        if sku in sku_count:
            sku_count[sku] += 1
        else:
            sku_count[sku] = 1


def calc_total_cost_per_item(item_to_quantity_map: Dict[int, str]) -> Dict[int, str]:
    '''for each unique sku, calculate the total cost of that sku
    '''
    summed_items = {}
    for sku, quantity in item_to_quantity_map.items():
        item = SKU_TO_ITEM[sku]
        if item.special_deal:
            summed_items[sku] = handle_special_deal_items(item, quantity)
        else:
            summed_items[sku] = item.unit_price * quantity
    return summed_items

def handle_special_deal_items(item: Item, quantity: int) -> int:
    '''Calculate the special offer prices
    '''
    special_deal = item.special_deal
    split_prices = divmod(quantity, special_deal.quantity)
    special_price_cost = split_prices[0] * special_deal.offer_price
    regular_price_cost = split_prices[1] * item.unit_price
    return special_price_cost + regular_price_cost

def calc_total_cost(total_cost_per_item: Dict[str, int]) -> int:
    '''Sum up all the prices from our list of skus
    '''
    return(sum([cost for cost in total_cost_per_item.values()]))


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    if not skus_valid(skus):
        return INVALID_SKUS
    item_to_quantity_map = count_each_item(skus)
    total_cost_per_item = calc_total_cost_per_item(item_to_quantity_map)
    total_cost = calc_total_cost(total_cost_per_item)
    return total_cost





