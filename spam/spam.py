
from .dfs_pruning import DFS_Pruning
from .tree import Tree
from .scan import scan

import pandas as pd


class SPAM:

    def __init__(self, C, min_sup) -> None:
        """
        Inputs:
            - C = list of scanpaths 
            - min_sup = minimum support threshold
        """

        # Input parameters
        self.C = C
        self.min_sup = min_sup

        # First scan of C
        self.item_bitmaps = self._scan()
        self.frequent_items_indices = self._get_frequent_items()

        # Initialize tree data structure
        self.tree = Tree()

        # print(self.item_bitmaps)
        # print('frequent_items_indices =', self.frequent_items_indices)

    def process(self):
        """
        SPAM core function.
        """

        # Build the tree structure
        for item_index in self.frequent_items_indices:

            # Initial items for S_n and I_n
            S_0 = [
                self.item_bitmaps[index] for index in self.frequent_items_indices
            ]
            I_0 = [
                self.item_bitmaps[index] for index in self.frequent_items_indices
                if index > item_index
            ]

            # Depth-first search with pruning
            DFS_Pruning(
                self.tree,
                '∅',
                self.item_bitmaps[item_index],
                S_0, I_0,
                self.min_sup
            )

        return

    def results(self):
        """
        Return results in a pandas DataFrame format.
        Results are sorted by descending support values.
        """

        data = {
            'Sequence': [],
            'Support': []
        }

        for node in self.tree.nodes[1:]:
            data['Sequence'].append(node.sequence)
            data['Support'].append(node.object.support)

        return pd.DataFrame(
            data=data
        ).sort_values(by='Support', ascending=False)

    def _scan(self):
        """
        Single database scan.
        """
        return scan(self.C)

    def _get_frequent_items(self):
        """
        Get indices of frequent items.
        """

        frequent_items_indices = [
            item.id
            for item in self.item_bitmaps
            if item.support >= self.min_sup
        ]

        return frequent_items_indices
