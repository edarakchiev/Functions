def age_assignment(*args, **kwargs):
    name_age = {}
    for arg in args:
        for kwarg in kwargs:
            if arg[0] == kwarg:
                name_age[arg] = kwargs[kwarg]
    return name_age


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
