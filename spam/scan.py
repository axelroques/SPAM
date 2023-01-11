
from collections import Counter
from .bitmap import Bitmap


def scan(C):
    """
    Single database scan.

    Returns:
        - Vertical bitmap representation
    """

    # Get scanpath content
    counters = []
    for scanpath in C:
        counters.append(Counter(scanpath))
    counter = sum(counters, Counter())
    # print(counter)

    # Build bitmaps for each item
    total_items = sum(counter.values())
    bitmaps = [
        Bitmap(id, label, C=C, support=count/total_items)
        for id, (label, count)
        in enumerate(sorted(counter.items()))
    ]

    return bitmaps
