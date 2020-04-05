"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F

예시
<입력>
score : 88

<출력>
A

"""
s = float(input('score : '))

if s >= 0 and s <= 20 :
    print('F')
elif s > 20 and s <= 40 :
    print('D')
elif s > 40  and s <= 60 :
    print('C')
elif s > 60 and s <= 80 :
    print('B')
elif s > 80 and s <= 100 :
    print('A')
