"""Date:11/Jun/2023
Brief Project Description:Assignment 2 Travel Tracker_class Placecollection
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-QingboTan
"""
from operator import attrgetter
from place import Place

# NAME_INDEX = 0
# COUNTRY_INDEX = 1
# PLACE_INDEX = 2
# VISITED_INDEX = 3


class PlaceCollection:
    """..."""
    NAME = 'name'
    COUNTRY = 'country'
    PRIORITY = 'priority'

    def __init__(self):
        self.places = []
        self.filename = ''

    def __str__(self):
        string = ''
        for i, place in enumerate(self.places, start=1):
            string += (f"{' 'if place.is_visited else'*'}{i}.{place.name:<10} in {place.country:<20}{place.priority:>2}\n")
        if string:
            required = f"You need to visit {self.count_unvisited_places()} cities."
            return string + required
        else:
            return "Collection of places is empty"

    def load_places(self, filename=''):
        """Read csv file & creates the list of cities."""
        self.filename = filename
        with open(filename, 'r') as place_file:
            for line in place_file.readlines():
                self.places.append(Place(*line.rstrip().split(',')))

    def save_places(self, filename=''):
        """Save csv file"""
        self.filename = filename
        with open(filename, "w") as place_file:
            # city_writer = csv.writer(out_file)
            for place in self.places:
                print(place.convert_str_to_csv(), file=place_file)
                # city_writer.writerow(city_data)

    def add_place(self, name):
        """Add places in collection."""
        self.places.append(name)

    def count_unvisited_places(self):
        """Get number of unvisited places"""
        place_number = 0
        for place in self.places:
            if not place.is_visited:
                place_number += 1
        return place_number

    def sort(self, key):
        """Sort names in collection."""
        self.places.sort(key=attrgetter(key, PlaceCollection.NAME))

    def __len__(self):
        return len(self.places)

    def __getitem__(self, key):
        return self.places[key]

    def __iter__(self):
        return iter(self.places)
