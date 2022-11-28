from model.Student_load import load

students = load()

student1 = students.__getitem__(0)
print(student1.list_scores)
print(student1.name)


