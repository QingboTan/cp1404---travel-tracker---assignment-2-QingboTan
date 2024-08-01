"""
Replace the contents of this module docstring with your own details
Name:Qingbo Tan
Date started:29.April.2023
GitHub URL:https://github.com/JCUS-CP1404/cp1404--travel-tracker---assignment-1-QingboTan
"""
import csv
import random

MENU = "Menu:\nL - List places\nR - Recommend random place\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by <Qingbo Tan>")
    city_list = read_file(FILENAME)
    city_list = sorted(city_list, key=by_priority, reverse=True)
    print(f"{(len(city_list))} places loaded from {FILENAME}")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            display_city(city_list)
        elif choice == "r":
            recommend_city(city_list)
        elif choice == "a":
            add_city_data(city_list)
        elif choice == "m":
            display_city(city_list)
            mark_city_visited(city_list)
        else:
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").lower()
    save_file(FILENAME, city_list)
    print(f"{(len(city_list))} places saved to {FILENAME}\nHave a nice day :)")


def read_file(filename):
    city_list = []
    with open(filename, "r") as in_file:
        for line in in_file:
            city_information = line.strip().split(",")
            city_list.append(city_information)
        in_file.close()
    return city_list


def save_file(filename, city_list):
    with open(filename, "w", newline='') as out_file:
        city_writer = csv.writer(out_file)
        for city_data in city_list:
            city_writer.writerow(city_data)


def display_city(city_list):
    unvisited_number = 0
    for i, city in enumerate(city_list):
        if city[-1] == "n":
            visited = "*"
            unvisited_number += 1
        else:
            visited = " "
        print(f"{visited}{i+1}.{city[0]:<10} in {city[1]:<20}{city[2]:>2}")
    if unvisited_number == "0":
        print(f"{len(city_list)} places. No places left to visit. Why not add a new place?")
    else:
        print(f"{len(city_list)} places. You still want to visit {unvisited_number} places.")


def by_priority(priority):
    return priority[-2]


def recommend_city(city_list):
    unvisited_cities = []
    for city in city_list:
        if city[-1] == "n":
            unvisited_cities.append(city[0])
    if not unvisited_cities:
        print("No unvisited places")
    else:
        name = random.choice(unvisited_cities)
        print(f"Not sure where to visit next?\nHow about... {name} in {city[1]}?")


def add_city_data(city_list):
    city_name = check_blank("Name: ")
    city_country = check_blank("Country: ")
    city_priority = input("Priority: ")
    while not city_priority.isdigit():
        print("Priority must be a number")
        city_priority = input("Priority: ")
    city_data = [city_name, city_country, city_priority, "n"]
    city_list.append(city_data)
    print(f"{city_name} in {city_country} (priority {city_priority}) added to Travel Tracker")


def check_blank(prompt):
    data = input(prompt)
    while data == "":
        print("Input can not be blank")
        data = input(prompt)
    return data


def mark_city_visited(city_list):
    if is_unvisited(city_list):
        index = int(input(f"Enter the number of a place to mark as visited\n>>> "))
        while index not in range(1, len(city_list)+1):
            if index <= 0:
                print("Number must be > 0")
            else:
                print("Invalid place number")
            index = int(input(">>> "))
        if city_list[index-1][-1] == "n":
            print(f"{city_list[index-1][0]} in {city_list[index-1][1]} visited!")
            city_list[index-1][-1] = "v"
        else:
            print(f"You have already visited {city_list[index-1][0]}")
    else:
        print("No unvisited places")


def is_unvisited(city_list):
    for city in city_list:
        if city[-1] == "n":
            return True
    return False


if __name__ == '__main__':
    main()


# def test_display_city():
#     city_list = read_file(FILENAME)
#     display_city(city_list)
# test_display_city()

# def test_recommend():
#     city_list = read_file(FILENAME)
#     recommend_city(city_list)
# test_recommend()

# def test_add_city_data():
#     city_list = read_file(FILENAME)
#     add_city_data(city_list)
#     print(city_list)
# test_add_city_data()


