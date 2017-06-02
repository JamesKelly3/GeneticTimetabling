import random
from Representation.Course import Course
from Representation.Room import Room
from Representation.University import University


def generate_random_courses(n: int, lecturers: list, courses: list):
    modules = []
    for i in range(n):
        num_students = random.randint(5, 200)
        max_courses = 10 if 10 > len(courses) else len(courses)
        num_courses = random.randint(1, max_courses)
        num_lecturers = random.randint(1, 2)
        random.shuffle(lecturers)
        lecturers_module = lecturers[:num_lecturers]
        random.shuffle(courses)
        courses_module = courses[:num_courses]
        two_hr = random.randint(0, 1)
        num_hrs = random.randint(2, 4)
        course = Course(num_students, lecturers_module, courses_module, num_hrs, two_hr)
        modules.append(course)
    return modules


def generate_random_rooms(n: int):
    rooms = []
    times = list(range(10))
    for i in range(n):
        capacity = random.randint(10, 300)
        time = []
        for j in range(5):
            for x in random.sample(times, random.randint(0, 10)):
                time.append((j * 10) + x)
        room = Room(capacity, time)
        rooms.append(room)
    return rooms


def generate_random_uni(num_modules: int, num_rooms: int, num_lecturers: int, num_courses):
    lecturers = list(range(num_lecturers))
    courses = list(range(num_courses))
    modules = generate_random_courses(num_modules, lecturers, courses)
    rooms = generate_random_rooms(num_rooms)
    return University(rooms, modules)


if __name__ == '__main__':
    small_uni = generate_random_uni(50, 5, 35, 7)
    medium_uni = generate_random_uni(150, 10, 800, 20)
    large_uni = generate_random_uni(300, 25, 200, 30)
    very_large_uni = generate_random_uni(1000, 100, 570, 175)
