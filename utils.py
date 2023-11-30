from pipe import Pipe


@Pipe
def flat_map(iterable, f):
    ys = []
    for x in iterable:
        ys.extend(f(x))
    return ys
