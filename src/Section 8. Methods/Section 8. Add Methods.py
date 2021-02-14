class MusicSchool:

    students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                        "Talina": [28, "555-765-452", ["Cello"]],
                        "Eric":   [12, "583-356-223", ["Singing"]]}

    def __init__(self, working_hours, revenue):
        self.working_hours = working_hours
        self.revenue = revenue

    # Add your methods below this line
    def print_students_data(self):
        for key,val in MusicSchool.students.items():
            print(f'Student: {key} who is {val[0]} years old and is taking {val[2]}')

    def print_student(self, name):
        if name in MusicSchool.students.keys():
            print(f'Student: {name} who is {MusicSchool.students[name][0]} years old and is taking {MusicSchool.students[name][2]}')

    def add_student(self, name, data):
        MusicSchool.students[name] = data
        print(MusicSchool.students)

    def save_to_txt(self):
        with open('section8dict.txt', 'w') as file:
            for v, l in self.items():
                file.write(str(v) + '==>' + str(l) + '\n')

# Create the instance
lection = MusicSchool(8, 15000)

# Call the methods
# lection.print_students_data()
# lection.print_student("Gino")
# lection.add_student("Jack", [60, "562-234-234", ["Piano"]])
# lection.save_to_txt()


students = {"Gino":   [15, "653-235-345", ["Piano", "Guitar"]],
                    "Talina": [28, "555-765-452", ["Cello"]],
                        "Eric":   [12, "583-356-223", ["Singing"]]}

