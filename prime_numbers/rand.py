def park_miller(size: int, seed: int):
    while True:
        result = 0
        for i in range(int(size/32)):
            seed = (16807*seed) % 0x7fffffff
            result += seed << (i * 32)
        yield result

