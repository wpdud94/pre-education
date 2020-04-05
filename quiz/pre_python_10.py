"""10. 팩토리얼을 구하는 함수를 작성하시오.
ex ) 5! = 5x4x3x2x1
  print(factoral(5)) -> 120 출력
  
예시
<입력>
print(factorial(5))

<출력>
120
  """


def factorial(x):
    num = list(range(1, x + 1, 1))
    result = 1
    for i in range(x):
        if i < x - 1:
            result = result * num[i + 1]
            continue
        return result


print(factorial(5))
