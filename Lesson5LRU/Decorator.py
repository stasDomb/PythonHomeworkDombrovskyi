

import collections
import functools

from key_construct import key_construct


def lru_cache(maxsize=4):
    """LRU cache decorator function"""

    def decorating_function(func):
        cache = collections.OrderedDict()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            key = key_construct(args, kwargs)  # make a key for the dict

            try:
                result = cache.pop(key)  # if we had this key in cache we do next string.
                # And we write in result value by key, and delete the value from cache.
                wrapper.hits += 1  # we increase counter of hits

            except KeyError:  # when we didn't have value by this key we get KeyError
                result = func(*args, **kwargs)
                wrapper.misses += 1  # and we increase the counter of misses

                if len(cache) >= maxsize:  # check of available space in cache
                    cache.popitem()

            cache[key] = result  # after deleting these key and value from cache, now we inserting value again

            return result

        def cache_info():
            """Statistics"""

            print({
                'cache': dict(cache),
                'available_space': maxsize-len(cache),
                'hits': wrapper.hits,
                'misses': wrapper.misses

            })

        def cache_clear():
            """Clear the cache and statistic of cache"""

            cache.clear()  # clearing the cache
            wrapper.hits = wrapper.misses = 0  # set to zero the counters

        # creating 2 counters. hits - for cases when we got from cache some value
        # and misses - when we didn't have needed key
        wrapper.hits = wrapper.misses = 0
        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear

        return wrapper

    return decorating_function


@lru_cache()
def main_func(a, b):
    return a + b


main_func(10, 20)
main_func(5, 2)
main_func(10, 2)


main_func.cache_info()


