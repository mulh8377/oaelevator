"""Module that contains logic for an elevator
traversing a 1d path."""


class ElevatorService:
    """Elevator Service."""

    # no unit given, maybe seconds?
    TRAVEL_TIME = 10

    def __init__(self, start: int) -> None:
        self.current_floor = start

    @staticmethod
    def travel_cost(total_distance: int) -> int:
        return total_distance * ElevatorService.TRAVEL_TIME

    def calculate_distance(self, floors: list[int]) -> int:
        """
        Args: floors: list[int]

        Returns: total_distance
        """
        if len(floors) == 0:
            return 0

        # since we sort the queues in up & down order,
        # based off the current floor -- we can find the
        # distance using the last index.
        return abs(floors[-1] - self.current_floor)

    def get_travel_queues(self, floors: list[int]) -> tuple[list[int], list[int]]:
        """Cleans duplicate floors & returns sorted
        up & down queues for distance calculations &
        ordered floor traversal.

        Args: floors: list[int]

        Returns: tuple[list[int], list[int]]
        """

        # remove redundant floors by casting to a set.
        floors_to_visit = set(floors)

        # setup up & down queues
        up_queue, down_queue = [], []

        for floor in floors_to_visit:
            if self.current_floor < floor:
                up_queue.append(floor)
            elif self.current_floor > floor:
                down_queue.append(floor)
            else:
                # we are already at this floor, ignore.
                pass

        # need to check the len(s), python will cast to
        # NoneType if a list is empty.
        if len(up_queue) > 0:
            up_queue.sort()
        if len(down_queue) > 0:
            # sort in descending order,
            down_queue.sort(reverse=True)

        return up_queue, down_queue

    def __call__(self, v_floors: list[int]) -> tuple[int, list[int]]:
        """Callable that encapsulates some basic cleaning, distance traveled,
        and returns the expected output [travel_cost, list(floors_visited)]

        Args: v_floors: list[int]

        Returns: tuple[int, list[int]]
        """
        floors_visited = [self.current_floor]

        if len(v_floors) == 0:
            # we are idle, return 0 & current_floor
            return (0, floors_visited)

        up_queue, down_queue = self.get_travel_queues(v_floors)

        up_q_cost, down_q_cost = (
            self.calculate_distance(up_queue),
            self.calculate_distance(down_queue),
        )

        if up_q_cost & down_q_cost == 0:
            total_dist = max(up_q_cost, down_q_cost)
        else:
            total_dist = abs(up_queue[-1] - down_queue[-1]) + min(
                up_q_cost, down_q_cost
            )

        # always go in the direction of the shortest distance first.
        if up_q_cost <= down_q_cost:
            floors_visited.extend(up_queue)
            floors_visited.extend(down_queue)
        else:
            floors_visited.extend(down_queue)
            floors_visited.extend(up_queue)

        # save state of floor at the last stop.
        self.current_floor = floors_visited[-1]

        return (
            ElevatorService.travel_cost(total_distance=total_dist),
            floors_visited,
        )
