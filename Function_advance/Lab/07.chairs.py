def combination_calc(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
    for index in range(len(names)):
        name = names[index]
        combs.append(name)
        combination_calc(names[index+1:], n, combs)
        combs.pop()


names_list = input().split(", ")
num = int(input())
combination_calc(names_list, num)