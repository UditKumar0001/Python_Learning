def information(**kwargs):
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(Name = "Udit Kumar", Age = 21, Designation = "Student")