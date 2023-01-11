
from .dfs_pruning import DFS_Pruning
from .scan import scan


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
                if index >= item_index
            ]

            # Depth-first search with pruning
            DFS_Pruning(self.item_bitmaps[item_index], S_0, I_0, self.min_sup)

        return

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
