"""17. 1988년 ~ 2060년까지 중 월드컵이 개최되는 연도를 출력하시오


예시
<출력>
1988
1992
1996
2000
2004
2008
2012
2016
2020
2024
2028
2032
2036
2040
2044
2048
2052
2056
2060
"""
wyear = 1988-4
b = int((2060-1988)/4)
for i in range(1,b+2,1) :
    wyear = wyear + 4
    print(wyear)