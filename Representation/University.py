import numpy as np

class University:

    def __init__(self, rooms: list, courses: list):
        self.rooms = rooms
        self.courses = courses
        times = []
        for room in rooms:
            times = times + room.available_time_slots
        times = np.unique(times)
        self.num_time_slots = max(times)
