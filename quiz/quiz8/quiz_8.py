# Written by *** for COMP9021

# Defines a class Building that defines a few special methods,
# as well as the two methods:
# - go_to_floor_from_entry()
# - leave_floor_from_entry()
# and an atribute, number_created, to keep track of
# the number of Building objects that have been created.
#
# Also defines a function compare_occupancies() meant to take
# as arguments two Building objects.
#
# Building objects are created with statements of the form
# Building(height, entries) where height is a positive integer
# (possibly equal to 0) and entries is a nonempty string that
# denotes all access doors to the building, with at least
# one space within the string to separate entries.
# You can assume that height and entries are as expected.
#
# If building denotes a Building object, then
# building.go_to_floor_from_entry(floor, entry, nb_of_people)
# takes as argument an integer, a string, and an integer.
# An error of type BuildingError is raised,
# all with the same message, if:
# - floor is not between 0 and the building's height, or
# - entry is not one of the building's entries, or
# - nb_of_people is not strictly positive.
# If the lift at that entry has to go down,
# then by how many floors it has to go down is printed out.
#
# If building denotes a Building object, then
# building.leave_floor_from_entry(floor, entry, nb_of_people)
# takes as argument an integer, a string, and an integer.
# An error of type BuildingError is raised if:
# - floor is not between 0 and the building's height, or
# - entry is not one of the building's entries, or
# - nb_of_people is not strictly positive, or
# - there are not at least nb_of_people on that floor.
# The same error message is used for the first 3 issues,
# and another error message is used for the last issue.
# If the lift at that entry has to go up or down, then
# by how many floors it has to go up or down is printed out.
#
# For the number of floors to go up or down, use
# "1 floor..." or "n floors..." for n > 1.


# DEFINE AN ERROR CLASS HERE
class BuildingError(Exception):
    pass


class Building:
    number_created = 0

    # REPLACE PASS WITH YOUR CODE
    def __init__(self, height, entries):
        if height < 0 and entries == '':
            raise BuildingError('quiz_8.BuildingError: That makes no sense!')
        self.height = height
        self.entries = entries.split()
        Building.number_created += 1

        self.floor_people = {}
        self.cur_floor = {}
        for entry in self.entries:
            self.cur_floor[entry] = 0
            temp = [0] * (self.height + 1)
            self.floor_people[entry] = temp

    def get_nb_people(self):
        num = 0
        for entry in self.entries:
            num += sum(self.floor_people[entry])
        return num

    def __str__(self):
        temp = ', '.join(e for e in self.entries)
        return f"Building with {self.height + 1} floors accessible from entries: {temp}"

    def __repr__(self):
        return f"Building({self.height}, '{' '.join(self.entries)}')"

    # less than <
    def __lt__(self, other):
        return self.get_nb_people() < other.get_nb_people()

    # def __gt__(self, other):
    #     return not self.__lt__(other)

    # 相等
    def __eq__(self, other):
        return self.get_nb_people() == other.get_nb_people()

    def go_to_floor_from_entry(self, floor, entry, nb_of_people):
        if floor < 0:
            raise BuildingError('That makes no sense!')
        elif floor > self.height:
            raise BuildingError('That makes no sense!')
        elif entry not in self.entries:
            raise BuildingError('That makes no sense!')
        elif nb_of_people <= 0:
            raise BuildingError('That makes no sense!')
        else:
            cur_floor = self.cur_floor[entry]  # get current floor
            if cur_floor != 0:
                print(f'Wait, lift has to go down {cur_floor} floors...')  # go down

            self.cur_floor[entry] = floor  # reset (go up)
            self.floor_people[entry][floor] += nb_of_people

    def leave_floor_from_entry(self, floor, entry, nb_of_people):
        if floor < 0:
            raise BuildingError('That makes no sense!')
        elif floor > self.height:
            raise BuildingError('That makes no sense!')
        elif entry not in self.entries:
            raise BuildingError('That makes no sense!')
        elif nb_of_people <= 0:
            raise BuildingError('That makes no sense!')

        elif self.floor_people[entry][floor] < nb_of_people:
            raise BuildingError("There aren't that many people on that floor!")
        else:
            cur_floor = self.cur_floor[entry]
            if cur_floor > floor:
                # need to go down
                print(f'Wait, lift has to go down {cur_floor - floor} floors...')
            elif cur_floor < floor:
                # need to go up
                print(f'Wait, lift has to go up {floor - cur_floor} floors...')
            self.cur_floor[entry] = 0  # reset
            self.floor_people[entry][floor] -= nb_of_people


def compare_occupancies(building_1, building_2):
    # pass
    # REPLACE PASS WITH YOUR CODE
    # 大于， 等于， 小于
    if building_1 < building_2:
        print("There are more occupants in the second building.")
    elif building_1 == building_2:
        print("There is the same number of occupants in both buildings.")
    elif building_1 > building_2:
        print("There are more occupants in the first building.")
