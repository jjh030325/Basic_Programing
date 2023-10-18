s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
minlen = len(s_list[0])

for i in range(len(s_list)):
    if minlen > len(s_list[i]):
        minlen = len(s_list[i])

s_list.sort(key=len)

for i in range(len(s_list)):
    if minlen == len(s_list[i]):
        print(s_list[i])


#(3) 위 (1) 번 문제에서 ＇abc＇, ＇bcd＇, ＇opq＇의 세 문자열의 길이가 3으로 모두 같다. 이와 같이
#문자열의 길이가 같을 경우 다음과 같이 가장 길이가 짧은 문자열 3개를 모두 출력하는 프로그램 작성. 
#sort(key=len) 함수를 사용하여 길이에 따라 정렬한 후 코드를 작성
