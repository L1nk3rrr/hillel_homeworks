import functools
import requests


def cache(max_limit=64):
    """LFU Cache decorator"""
    if max_limit <= 0:
        raise ValueError("max_limit must be a positive integer")

    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key]['counter'] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)

            # delete element when limit
            if len(deco._cache) >= max_limit:
                del deco._cache[min(deco._cache, key=lambda item: deco._cache[item]['counter'])]

            deco._cache[cache_key] = {'counter': 0, 'content': result}
            return result

        deco._cache = {}  # from python 3.6 dict is ordered
        return deco
    return internal


@cache(max_limit=3)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://gitlab.com')
fetch_url('https://github.com')
fetch_url('https://github.com')
fetch_url('https://gitlab.com')
fetch_url('https://gitlab.com')
fetch_url('https://gitlab.com')
fetch_url('https://github.com')
fetch_url('https://github.com')
fetch_url('https://github.com')
fetch_url('https://uk-ua.facebook.com/')
fetch_url('https://uk-ua.facebook.com/')
fetch_url('https://uk-ua.facebook.com/')
fetch_url('https://uk-ua.facebook.com/')
fetch_url('https://ithillel.ua/')
fetch_url('https://ithillel.ua/')