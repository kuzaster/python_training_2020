def cache(times: int):
    d_cacher = {}

    def wrapper(func):
        def func_cache(*args):
            if times > 0:
                if args not in d_cacher:
                    value = func(*args)
                    d_cacher[args] = [value, 0]
                    return value
                elif d_cacher[args][1] < times:
                    d_cacher[args][1] += 1
                    return d_cacher[args][0]
                else:
                    value = func(*args)
                    d_cacher[args] = [value, 0]
                    return value
            return func(*args)

        return func_cache

    return wrapper
