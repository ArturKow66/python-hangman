def which_animal(money, price, animal):
    how_many = money // price
    if how_many != 1:
        if animal == ' sheep':
            print(str(how_many) + animal)
        else:
            print(str(how_many) + animal + 's')
    else:
        print(str(how_many) + animal)


buyer_money = int(input())

if buyer_money < 23:
    print('None')
elif 23 <= buyer_money < 678:
    which_animal(buyer_money, 23, ' chicken')
elif 678 <= buyer_money < 1296:
    which_animal(buyer_money, 678, ' goat')
elif 1296 <= buyer_money < 3848:
    which_animal(buyer_money, 1296, ' pig')
elif 3848 <= buyer_money < 6769:
    which_animal(buyer_money, 3848, ' cow')
elif buyer_money >= 6769:
    which_animal(buyer_money, 6769, ' sheep')
