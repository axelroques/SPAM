

def compute_support(s, item, extension_type):
    """
    Compute support of sequence s extended
    with item using the bitmap representation.

    Parameter 'extension_type' should be a string, either
    'S' or 'I' corresponding to respectively a 
    sequence-extension or an itemset-extension. 
    """

    if extension_type == 'S':
        return S_step_process(s, item)

    elif extension_type == 'I':
        return I_step_process(s, item)

    else:
        raise RuntimeError("'extension_type' parameter should be 'S' or 'I'.")


def S_step_process(s, item):
    """
    Compute support in the S-step process case.
    """

    s_extended = s.S_step(item)
    print('s =', s)
    print('i =', item)
    print('\ts_extended =', s_extended, '\n')

    return s_extended, s_extended.support


def I_step_process(s, item):
    """
    Compute support in the I-step process case.
    """

    s_extended = s.I_step(item)
    print('s =', s)
    print('i =', item)
    print('s_extended =', s_extended)

    return s_extended, s_extended.support
