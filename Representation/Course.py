class Course:

    def __init__(self, num_students, lecturers, courses, hours, two_hours):
        self.num_students = num_students
        self.lecturers = lecturers
        self.courses_which_can_take = courses
        self.num_hours = hours
        self.two_hour_count = two_hours