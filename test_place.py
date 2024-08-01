"""(Incomplete) Tests for Place class."""
from place import Place


def run_tests():
    """Test Place class."""

    # Test empty place (defaults)
    print("Test empty place:")
    default_place = Place()
    print(default_place)
    assert default_place.name == ""
    assert default_place.country == ""
    assert default_place.priority == 0
    assert not default_place.is_visited

    # Test initial-value place
    print("Test initial-value place:")
    new_place = Place("Malagar", "Spain", 1, False)
    # TODO: Write tests to show this initialisation works
    assert new_place.name == "Malagar"
    assert new_place.country == "Spain"
    assert new_place.priority == 1
    assert not new_place.is_visited
    assert str(new_place) == "Malagar in Spain with 1 is unvisited"
    print(new_place)

    # TODO: Add more tests, as appropriate, for each method
    """Test places csv file"""
    another_new_place = Place("Roman", "Italy", 12, 'n')
    assert another_new_place.name == "Roman"
    assert another_new_place.country == "Italy"
    assert another_new_place.priority == 12
    assert not another_new_place.is_visited
    assert str(another_new_place) == "Roman in Italy with 12 is unvisited"
    print(another_new_place)

    """Test Mark Unvisited Function"""
    print("\nTest Mark Unvisited Function")
    new_place.mark_unvisited()
    assert not new_place.is_visited
    print(new_place)

    """Test Mark Visited Function"""
    print("\nTest Mark Visited Function")
    new_place.mark_visited()
    assert new_place.is_visited
    print(new_place)

    """Test is important"""
    print("\nTest is_important Function")
    print(f"{default_place.is_important()}\n{new_place.is_important()}\n{another_new_place.is_important()}")


run_tests()
