
import numpy as np


class Bitmap:

    def __init__(self, id, label, representation=None, C=None, support=None) -> None:

        self.id = id
        self.label = label

        # Bitmap representation
        if representation:
            self.representation = representation
        elif C:
            self.representation = self._compute_bitmap_representation(C, label)
        else:
            raise RuntimeError('Unable to produce a bitmap representation.')

        # Support computation
        if support:
            self.support = support
        else:
            self.support = self._compute_support(self.representation)

    def I_step(self, bitmap):
        """
        I_step process.

        Basically an AND logical operation between two bitmaps.
        """

        extended_representation = {
            key: repr1 & repr2
            for (key, repr1), (_, repr2)
            in zip(
                self.representation.items(),
                bitmap.representation.items()
            )
        }

        return Bitmap(
            id=None, label=self.label+bitmap.label,
            representation=extended_representation
        )

    def S_step(self, bitmap):
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
            for _, representation in self.representation.items()
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
                bitmap.representation.items()
            )
        }

        return Bitmap(
            id=None, label=self.label+bitmap.label,
            representation=extended_representation
        )

    @ staticmethod
    def _compute_bitmap_representation(C, label):
        """
        Generate bitmap representation.
        """
        return {
            f'S_{i}': np.where(C[i] == label, 1, 0)
            for i in range(len(C))
        }

    @ staticmethod
    def _compute_support(representation):
        """
        Compute support as the number of non zero elements in the representation.
        """
        return sum([np.sum(bitmap) for _, bitmap in representation.items()])

    def __repr__(self) -> str:
        return f'Bitmap: id={self.id}, label={self.label}, bitmap={self.representation}'
