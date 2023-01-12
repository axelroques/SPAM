
from collections import Counter
from .bitmap import Item


def scan(C):
    """
    Single database scan.

    Returns a list of item bitmaps
    Note that the items are sorted in lexicographic order.
    """

    # Get scanpath unique items
    items = set().union(*[set(scanpath) for scanpath in C])

    # Build bitmaps for each item
    bitmaps = [
        Item(id=id, sequence=[item], C=C)
        for id, item
        in enumerate(sorted(items))
    ]

    return bitmaps
