from prime_numbers.rand import park_miller
from timeit import default_timer as timer

size = 32
while size <= 4096:
    start = timer()
    number = park_miller(size, 392)
    next(number)
    end = timer()
    print(f"{(end - start):.4f}\n")
    size += size
