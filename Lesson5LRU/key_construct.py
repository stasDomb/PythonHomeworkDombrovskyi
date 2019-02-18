
def key_construct(args, kwargs):
    key = args  # read the key. There is a tuple
    if kwargs:
        key += tuple(sorted(kwargs.items()))

    return key
