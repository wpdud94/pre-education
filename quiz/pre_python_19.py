"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']


예시
<입력>
print(list)

<출력>
['charlie', 'foxtrot']

 """
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
list = []
# print(len(a[0]))
for i in range(len(a)) :
    if len(a[i]) != 7 :
        continue
    list = list + [a[i]]
print(list)