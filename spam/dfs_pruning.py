
from .support import compute_support


def DFS_Pruning(s, S_n, I_n, min_sup):
    """
    Depth-first seach with pruning.

    Inputs:
        - s = bitmap representation of the current sequence
        - S_n = S-step candidate list
        - I_n = I-step candidate list
        - min_sup = minimum support threshold
    """

    # Initialize empty children's S_n and I_n lists
    S_temp = []
    I_temp = []

    # Populate S_temp with the frequent items i in S_n
    # if the sequence-extension of the current sequence
    # s with i is frequent
    for item in S_n:

        # Compute support of the sequence-extension
        s_extended, support = compute_support(
            s, item, extension_type='S'
        )

        if support >= min_sup:
            S_temp.append((s_extended, item))

    # With S_temp now computed, generate new children nodes
    for s_extended, item in S_temp:

        I_children = [
            j for j in S_temp if j.id >= item.id
        ]

        # Continue tree exploration with the new updated sequence
        DFS_Pruning(s_extended, S_temp, I_children, min_sup)

    # Populate I_temp with the frequent items i in I_n
    # if the itemset-extension of the current sequence
    # s with i is frequent
    for item in I_n:

        # Compute support of the itemset-extension
        s_extended, support = compute_support(
            s, item, extension_type='I'
        )

        if support >= min_sup:
            I_temp.append((s_extended, item))

    # With I_temp now computed, generate new children nodes
    for s_extended, item in I_temp:

        I_children = [
            j for j in I_temp if j.id >= item.id
        ]

        # Continue tree exploration with the new updated sequence
        DFS_Pruning(s_extended, S_temp, I_children, min_sup)

    return
