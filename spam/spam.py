
from .dfs_pruning import DFS_Pruning
from .scan import scan


def SPAM(C, min_sup):
    """
    SPAM core function.

    Inputs:
        - C = numpy array of size N x l containing N scanpaths 
        of length l
        - min_sup = minimum support threshold
    """

    # Single database scan
    bitmap, frequent_items_indices = scan(C)

    # Build the tree structure
    for item_index in frequent_items_indices:

        # Initial items for S_n and I_n
        S_0 = bitmap[frequent_items_indices]
        I_0 = bitmap[frequent_items_indices >= item_index]

        # Depth-first search with pruning
        DFS_Pruning(bitmap[item_index], S_0, I_0, min_sup)

    return
