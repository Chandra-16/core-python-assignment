def find_avg(marks):
    return sum(marks) / len(marks)


def topper(averages):

    top_student = None
    top_avg = -1
    for student, avg in averages.items():
        if avg > top_avg:
            top_avg = avg
            top_student = student
    return top_student

students = {}

n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Enter name: ")
    marks = list(map(int, input(f"Enter marks for {name} (space separated): ").split()))
    students[name] = marks

averages = {name: round(find_avg(marks), 2) for name, marks in students.items()}

top_student = topper(averages)

print("Average Marks:", averages)
print(f'Top Student: "{top_student}"')