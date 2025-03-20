from functools import wraps
import random
from oaelevator.elevator import ElevatorService

large_q_floors_to_visit = [random.randint(1, 2000) for _ in range(1000)]

pick_start_l = random.randint(1, 2000)

small_q_floors_to_visit = [random.randint(1, 20) for _ in range(10)]

pick_start_s = random.randint(1, 20)


def timeit(N=100_000):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time

            start_time = time.perf_counter()

            for _ in range(N):
                _ = func(*args, **kwargs)

            end_time = time.perf_counter() - start_time
            return end_time / N

        return wrapper

    return decorator


@timeit()
def large_floors_to_visit():
    return ElevatorService(pick_start_l)(large_q_floors_to_visit)


@timeit()
def small_floors_to_visit():
    return ElevatorService(pick_start_s)(small_q_floors_to_visit)


def main():
    avg_for_big_n = large_floors_to_visit()
    avg_for_small_n = small_floors_to_visit()

    print("optimization, large_n, small_n")
    print(f"reduced_iters, {avg_for_big_n}, {avg_for_small_n}")


if __name__ == "__main__":
    main()
