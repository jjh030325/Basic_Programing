name = input("이름을 입력하시오 : ")
tall = int(input("키를 입력하시오(단위 cm) : "))
if(tall<140):
    print(name, "님은 놀이기구를 탈 수 없습니다.")
else:
    print(name, "님은 놀이기구를 탈 수 있습니다.")