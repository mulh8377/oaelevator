from oaelevator.elevator import ElevatorService
import pytest


def test_elevator_init():
    assert isinstance(ElevatorService(10), ElevatorService)
    assert ElevatorService(10).current_floor == 10
    assert ElevatorService.TRAVEL_TIME == 10


def test_elevator_travel_cost():
    import random

    const_val = random.randint(1, 60)
    assert (
        ElevatorService.travel_cost(const_val) / const_val
        == ElevatorService.TRAVEL_TIME
    )


def test_empty_calc_distance():
    assert ElevatorService(1).calculate_distance([]) == 0


@pytest.mark.parametrize("floors_to_visit", [[2, 3], [5, 6]])
def test_simple_calc_distance(floors_to_visit):
    ElevatorService(4).calculate_distance(floors_to_visit) == 2


@pytest.mark.parametrize("floors_to_visit", [[2, 3, 5, 6]])
def test_get_travel_queues(floors_to_visit):
    up, down = ElevatorService(4).get_travel_queues(floors_to_visit)
    assert up == [5, 6]
    assert down == [3, 2]


def test_elevator_no_dist_traveled():
    total_dist, floors_in_order = ElevatorService(1)([])
    assert total_dist == 0
    assert floors_in_order == [1]


@pytest.mark.parametrize("starting_floor, to_visit", [(1, [4, 3, 2])])
def test_elevator_ascending_travel(starting_floor, to_visit):
    total_dist, floors_in_order = ElevatorService(starting_floor)(to_visit)
    assert total_dist == 30
    assert floors_in_order == [1, 2, 3, 4]


@pytest.mark.parametrize("starting_floor, to_visit", [(4, [3, 1, 2])])
def test_elevator_descending_travel(starting_floor, to_visit):
    total_dist, floors_in_order = ElevatorService(starting_floor)(to_visit)
    assert total_dist == 30
    assert floors_in_order == [4, 3, 2, 1]


@pytest.mark.parametrize("starting_floor, to_visit", [(10, [1, 2, 11, 12])])
def test_elevator_up_and_down(starting_floor, to_visit):
    total_dist, floors_in_order = ElevatorService(starting_floor)(to_visit)
    assert total_dist > 0
    assert floors_in_order == [10, 11, 12, 2, 1]
