
import numpy as np


class Bitmap:

    def __init__(self) -> None:
        pass

    def I_step(self, other):
        """
        I_step process.

        Basically an AND logical operation between two bitmaps.
        """

        extended_representation = {
            key: repr1 & repr2
            for (key, repr1), (_, repr2)
            in zip(
                self.representation.items(),
                other.representation.items()
            )
        }

        new_sequence = self.sequence[:-1] + \
            [self.sequence[-1] + other.sequence[0]]

        return Sequence(
            sequence=new_sequence,
            representation=extended_representation
        )

    def S_step(self, other):
        """
        S_step process.

        Finds k, the index of the first non zero element in
        self's representation.
        Then, create a new transformed representation filled
        with zeros before index k and filled with ones after.
        Finally, perform an AND logical operation between the
        transformed representation and the input bitmap.
        """

        def first_nonzero(arr, axis, invalid_val=-1):
            mask = arr != 0
            return int(np.where(
                mask.any(axis=axis), mask.argmax(axis=axis), invalid_val
            ))

        # Find k
        k_list = [
            first_nonzero(representation, axis=0)
            for representation in self.representation.values()
        ]

        # Compute transformed representation
        transformed_representation = {
            key: np.array([0]*(k+1) + [1]*(len(representation)-(k+1)))
            if k != -1
            else np.zeros(len(representation), dtype=int)
            for k, (key, representation)
            in zip(k_list, self.representation.items())
        }

        # AND logical operator
        extended_representation = {
            key: repr1 & repr2
            for (key, repr1), (_, repr2)
            in zip(
                transformed_representation.items(),
                other.representation.items()
            )
        }

        new_sequence = self.sequence.copy()
        new_sequence.append(other.sequence[0])

        return Sequence(
            sequence=new_sequence,
            representation=extended_representation
        )

    @ staticmethod
    def _compute_support(representation):
        """
        Compute support as the number of non zero elements in the representation.
        """

        total = sum([len(bitmap) for bitmap in representation.values()])

        return sum([np.sum(bitmap)/total for bitmap in representation.values()])

    @staticmethod
    def _get_seq_length(seq):
        """
        Helper function that returns an input sequence's length.
        """
        return sum([len(itemset) for itemset in seq])

    def __lt__(self, other):
        """
        Overload <= operator. 
        Implements a partial order for sequence comparison.
        """

        # If both sequences have the same length, use the lexicographic order
        if self._get_seq_length(self.sequence) == self._get_seq_length(other.sequence):
            return self.sequence < other.sequence

        # Otherise the longest sequence is the greatest
        elif self._get_seq_length(self.sequence) < self._get_seq_length(other.sequence):
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Overload >= operator. 
        Implements a partial order for sequence comparison.
        """

        # If both sequences have the same length, use the lexicographic order
        if self._get_seq_length(self.sequence) == self._get_seq_length(other.sequence):
            return self.sequence > other.sequence

        # Otherise the longest sequence is the greatest
        elif self._get_seq_length(self.sequence) > self._get_seq_length(other.sequence):
            return True
        else:
            return False

    def __repr__(self) -> str:
        """
        Pretty print.
        """
        return f'Sequence: {self.sequence}'


class Item(Bitmap):

    def __init__(self, id, sequence, C) -> None:
        super().__init__()

        self.id = id
        self.sequence = [sequence]

        # Bitmap representation
        self.representation = self._compute_bitmap_representation(C, sequence)

        # Support
        self.support = self._compute_support(self.representation)

    @ staticmethod
    def _compute_bitmap_representation(C, sequence):
        """
        Generate bitmap representation.
        """
        return {
            f'S_{i}': np.where(C[i] == sequence[0], 1, 0)
            for i in range(len(C))
        }


class Sequence(Bitmap):

    def __init__(self, sequence, representation) -> None:
        super().__init__()

        self.sequence = sequence

        # Bitmap representation
        self.representation = representation

        # Support
        self.support = self._compute_support(self.representation)
