"""
Date:11/Jun/2023
Brief Project Description:Assignment 2 Travel Tracker_class Place
GitHub URL:https://github.com/JCUS-CP1404/cp1404---travel-tracker---assignment-2-QingboTan
"""
UNVISITED = 'n'
VISITED = 'v'


class Place:
    def __init__(self, name='', country='', priority=0, is_visited=False):
        self.name = name
        self.country = country
        self.priority = int(priority)

        """check the visited status, will return ValueError if the status is wrong"""
        if isinstance(is_visited, bool):
            self.is_visited = is_visited
        elif is_visited in {UNVISITED, VISITED}:
            if is_visited == VISITED:
                self.is_visited = True
            else:
                self.is_visited = False
        else:
            raise ValueError

    def __str__(self):
        """The format of output"""
        return '{0} in {1} with {2} is {3}'.format(self.name or "Unknown Name",
                                                   self.country or "Unknown Country",
                                                   self.priority,
                                                   '(visited)' if self.is_visited else'unvisited')

    def mark_visited(self):
        """Mark is visited"""
        self.is_visited = True

    def mark_unvisited(self):
        """Mark is unvisited"""
        self.is_visited = False

    def is_important(self):
        """Check if the place is considered important, which is defined as having a priority <= 2"""
        if self.priority <= 2:
            return True
        else:
            return False

    def convert_str_to_csv(self):
        return ','.join((self.name, self.country, str(self.priority), VISITED if self.is_visited else UNVISITED))
