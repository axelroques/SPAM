
from .support import compute_support


def DFS_Pruning(tree, parent, child, S_n, I_n, min_sup):
    """
    Depth-first seach with pruning.

    Inputs:
        - s = bitmap representation of the current sequence
        - S_n = S-step candidate list
        - I_n = I-step candidate list
        - min_sup = minimum support threshold
    """

    # Store current node
    tree.add_node(child, child.sequence, parent)

    # Initialize empty children's S_n and I_n lists
    S_temp = []
    I_temp = []

    # print('\tCURRENT SEQUENCE =', child)
    # print('\tCURRENT S_n =', S_n)
    # print('\tCURRENT I_n =', I_n)

    # Populate S_temp with the frequent items i in S_n
    # if the sequence-extension of the current sequence
    # s with i is frequent
    for item in S_n:

        # Compute support of the sequence-extension
        support = compute_support(child, item, extension_type='S')
        # print('\tSupport =', support, '\n')

        if support >= min_sup:
            S_temp.append(item)

    # With S_temp now computed, generate new children nodes
    for item in S_temp:

        # print('\n Creating S-children with', item.sequence)

        I_children = [
            j for j in S_temp if j > item
        ]

        # Continue tree exploration with the new updated sequence
        DFS_Pruning(
            tree,
            child,
            child.S_step(item),
            S_temp, I_children,
            min_sup
        )

    # Populate I_temp with the frequent items i in I_n
    # if the itemset-extension of the current sequence
    # s with i is frequent
    for item in I_n:

        # Compute support of the itemset-extension
        support = compute_support(child, item, extension_type='I')
        # print('\tSupport =', support, '\n')

        if support >= min_sup:
            I_temp.append(item)

    # With I_temp now computed, generate new children nodes
    for item in I_temp:

        # print('\n Creating I-children with', item.sequence)

        I_children = [
            j for j in I_temp if j > item
        ]

        # Continue tree exploration with the new updated sequence
        DFS_Pruning(
            tree,
            child,
            child.I_step(item),
            S_temp, I_children,
            min_sup
        )

    return
