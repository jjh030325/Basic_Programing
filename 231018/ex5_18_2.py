s_list = ['abc', 'bcd', 'bcdefg', 'abba', 'cddc', 'opq']
maxlen = len(s_list[0])
ans = s_list[0]

for i in range(len(s_list)):
    if maxlen < len(s_list[i]):
        maxlen = len(s_list[i])
        ans = s_list[i]

print(ans)

#(2) max() 함수나 sort() 메소드를 사용하지 말고, s_list 내의 문자열 항목 중에서 가장 길이가 긴 문자
#열을 출력 (길이가 가장 긴 문자열이 두개 이상 있을 경우 아래 출력과 같이 제일 먼저 나타나는 문자열을 출력)
