import random
from Representation.University import University
import numpy as np


def eval_fitness(individual: list, university: University):
    no_courses = [(x[1], x[2]) for x in individual]
    unique = np.unique(no_courses)
    double_bookings = len(no_courses) - len(unique)

    room_vio = 0
    for course in individual:
        room_capacity = university.rooms[course[1]].capacity
        if room_capacity < course[0].num_students:
            room_vio += 1

    time_dict = {}
    clashes = 0
    for course in individual:
        if course[2] not in time_dict.keys():
            time_dict[course[2]] = []
        time_dict[course[2]] += course[0].courses_which_can_take
    for item in time_dict.items():
        item = item[1]
        unique = np.unique(item)
        clashes += len(item) - len(unique)

    return double_bookings + room_vio + clashes

def penalty(individual: list):
    pass
