menu = { "Americano":3000, "Ice Americano":3500, "Cappuccino":4000, "Cafe Latte":4500, "Espresso":3600}

for key in menu:
    print("{:17} 가격 : {}".format(key,menu[key]))

choose = input("위의 메뉴중 하나를 선택하세요: ")
inMenuCheck = False

for key in menu:
    if key == choose:
        inMenuCheck = True
        break

if inMenuCheck == False:
    print("미안합니다. {}는 메뉴에 없습니다.".format(choose))
else:
    print("{}는 {}원 입니다. 결제를 부탁합니다.".format(choose, menu[key]))