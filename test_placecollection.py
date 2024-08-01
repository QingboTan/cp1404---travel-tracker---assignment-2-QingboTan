"""(Incomplete) Tests for PlaceCollection class."""
from placecollection import PlaceCollection
from place import Place


def run_tests():
    """Test PlaceCollection class."""

    # Test empty PlaceCollection (defaults)
    print("Test empty PlaceCollection:")
    place_collection = PlaceCollection()
    print(place_collection)
    assert not place_collection.places  # an empty list is considered False

    # Test loading places
    print("\nTest loading places:")
    place_collection.load_places('places.csv')
    print(place_collection)
    assert place_collection.places  # assuming CSV file is non-empty, non-empty list is considered True

    # Test adding a new Place with values
    print("\nTest adding new place:")
    place_collection.add_place(Place("Smithfield", "Australia", 5, False))
    print(place_collection)

    # Test sorting places
    print("\nTest sorting - priority:")
    place_collection.sort("priority")
    print(place_collection)

    print("\nTest sorting - name:")
    place_collection.sort("name")
    print(place_collection)

    print("\nTest sorting - country:")
    place_collection.sort("country")
    print(place_collection)

    print("\nTest sorting - is_visited:")
    place_collection.sort("is_visited")
    print(place_collection)

    print("\nTest count_unvisited_places:")
    new_places_collection = PlaceCollection()
    print("Add visited place")
    new_places_collection.add_place(Place("Sichuan", "China", 1, True))
    assert new_places_collection.count_unvisited_places() == 0
    print(new_places_collection)
    print("\nAdd unvisited place")
    new_places_collection.add_place(Place("Suzhou", "China", 4, False))
    assert new_places_collection.count_unvisited_places() == 1
    print(new_places_collection)

    # Test saving places
    print("\nTest saving places:")
    place_collection.sort("name")
    place_collection.save_places("places_collection.csv")
    print(place_collection)


run_tests()
