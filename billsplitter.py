import random

print('Enter the number of friends joining (including you):')
quantity = int(input())
if quantity > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    people = [input() for i in range(quantity)]
    print()
    print('Enter the total bill value:')
    pay = int(input())
    check = dict.fromkeys(people, round(pay / quantity, 2))
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()
    if choice == 'Yes':
        rand = people[random.randint(0, quantity)]
        print(F'{rand} is the lucky one!')
        check = dict.fromkeys(people, round(pay / (quantity - 1), 2))
        check[rand] = 0
    else:
        print('No one is going to be lucky')
    print(check)
else:
    print('No one is joining for the party')
