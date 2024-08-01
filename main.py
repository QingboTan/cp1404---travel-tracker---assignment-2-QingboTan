"""
Name:Qingbo Tan
Date:11/Jun/2023
Brief Project Description:Assignment 2 Travel Tracker_Main part
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-QingboTan
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from place import Place
from placecollection import PlaceCollection

FILENAME = "places.csv"
VISITED_COLOR = (1, 1, 1, 0.6)
UNVISITED_COLOR = (0, 1, 0.6, 0.7)


class TravelTrackerApp(App):
    """..."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.places = PlaceCollection()

    def build(self):
        """Build Travel Tracker App"""
        self.title = "TravelTracker"
        self.root = Builder.load_file('app.kv')
        try:
            self.places.load_places(FILENAME)
            self.display_top_label()
            self.display_bottom_label("Welcome to Travel Tracker 2.0")
            # self.sort_place_list("visited")
            self.sort_place_list("is_visited")
        # If places.csv is not found
        except (FileNotFoundError, LookupError):
            self.display_top_label()
            self.display_bottom_label("Welcome to Travel Tracker 2.0")
        return self.root

    def display_top_label(self):
        """display the number of unvisited places"""
        self.root.ids.top_label.text = f"Places to visit {self.places.count_unvisited_places()}"

    def display_bottom_label(self, bottom_label):
        """display the bottom tab"""
        self.root.ids.bottom_label.text = bottom_label

    def sort_place_list(self, key='is_visited'):
        """display the sorting place list"""
        if key.lower() == 'visited':
            key = 'is_visited'
        self.places.sort(key.lower())
        self.root.ids.place_list.clear_widgets()
        place_list = []

        def change_state(button):
            for selected_place in place_list:
                if selected_place.name in button.text:
                    PlaceButton.on_click(self, selected_place)
                    if place.is_visited:
                        self.state = "visited_color"
                        button.background_color = VISITED_COLOR
                    else:
                        self.state = "unvisited_color"
                        button.background_color = UNVISITED_COLOR
                    button.text = str(selected_place)
                    self.sort_place_list(key)

        for place in self.places:
            place_list.append(place)
            if place.is_visited:
                self.state = 'visited_color'
            else:
                self.state = 'unvisited_color'
            self.root.ids.place_list.add_widget(PlaceButton(place=place,
                                                            text=str(place),
                                                            on_press=change_state,
                                                            background_color={"visited_color": VISITED_COLOR,
                                                                              "unvisited_color": UNVISITED_COLOR}
                                                            [self.state]))

    def add_new_place(self, input_name, input_country, input_priority):
        name, country, priority = map(str.strip, (input_name.text, input_country.text, input_priority.text))
        # """check if all the fields are filled"""
        if not name or not country or not priority:
            self.display_bottom_label("All fields must be completed")
            return
        # """check if the input priority is valid"""
        try:
            priority = int(priority)
        except ValueError:
            self.display_bottom_label("Please enter a valid number")
            return
        # """Check the input priority number is greater than 0"""
        if priority < 1:
            self.display_bottom_label("Priority must be > 0")
            return

        self.sort_place_list()
        self.display_bottom_label(" ")
        name = name + " "
        self.places.add_place(Place(name, country, priority))
        self.display_top_label()
        self.display_bottom_label(f"{name} in {country}, priority {priority} added")
        self.sort_place_list(self.root.ids.place_sorter.text)
        self.clear_input_field(input_name, input_country, input_priority)

    @staticmethod
    def clear_input_field(name, country, priority):
        """Clear the name, country, priority fields"""
        name.text = ''
        country.text = ''
        priority.text = ''

    def on_stop(self):
        self.places.save_places(FILENAME)
        return super().on_stop()


class PlaceButton(Button):
    def __init__(self, place, **kwargs):
        super().__init__(**kwargs)
        self.place = place

    def on_click(self, place):
        """change the background color and display the top & bottom tabs"""
        if place.is_visited:
            place.mark_unvisited()
            if place.is_important():
                bottom_label = f"You need to visit {str(place.name.strip())}. Get going!"
            else:
                bottom_label = f"You need to visit {str(place.name.strip())}."
        else:
            place.mark_visited()
            if place.is_important():
                bottom_label = f"You visited {str(place.name.strip())}. Great travelling!"
            else:
                bottom_label = f"You visited {str(place.name.strip())}."

        self.display_top_label()
        self.display_bottom_label(bottom_label)


if __name__ == '__main__':
    TravelTrackerApp().run()
