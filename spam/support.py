

def compute_support(bitmap, s, item, extension_type):
    """
    Compute support of sequence s extended
    with item using the bitmap representation.

    Parameter 'extension_type' should be a string, either
    'S' or 'I' corresponding to respectively a 
    sequence-extension or an itemset-extension. 
    """

    if extension_type == 'S':
        return S_step_process(bitmap, s, item)

    elif extension_type == 'I':
        return I_step_process(bitmap, s, item)

    else:
        raise RuntimeError("'extension_type' parameter should be 'S' or 'I'.")


def S_step_process(bitmap, s, item):
    """
    Compute support in the S-step process case.
    """
    return support

def I_step_process(bitmap, s, item):
    """
    Compute support in the I-step process case.
    """
    return support