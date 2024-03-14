import random
f_number = int(input("Enter the number of friends joining (including you): \n"))
print()


def above():
    if f_number <= 0:
        print("No one is joining for the party")
        quit()


def blood_offering():
    print("Enter the name of every friend (including you), each on a new line:")
    user_dict = {input(): 0 for n in range(f_number)}
    print()
    print("Enter the total bill value:")
    bill = int(input())
    print()
    print("""Do you want to use the "Who is lucky" feature? Write Yes/No:""")
    lucky = input()
    print()
    if lucky == "Yes":
        random_name = random.choice(list(user_dict.keys()))
        print(f"{random_name} is the lucky one!")
        split_value = round(bill / (f_number - 1), 2)
        if split_value.is_integer():
            split_value = int(split_value)
        d = {x: split_value for x in user_dict}
        d[random_name] = 0
        print()
        print(d)
    else:
        print("No one is going to be lucky")
        split_value = round(bill / f_number, 2)
        if split_value.is_integer():
            split_value = int(split_value)
        d = {x: split_value for x in user_dict}
        print()
        print(d)


above()
blood_offering()
