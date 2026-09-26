from src.bus_functions import find_Platform, find_Destination


def test_find_platform():
    assert find_Platform(101) == 1
    assert find_Platform(103) == 3


def test_find_destination():
    assert find_Destination(101) == "Delhi"
    assert find_Destination(105) == "Lucknow"


def test_invalid_bus():
    assert find_Platform(999) == 0
    assert find_Destination(999) == "Not Available"