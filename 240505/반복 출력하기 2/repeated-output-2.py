N = int(input())

def hello(n):
    if n == 0:
        return
    
    hello(n-1)
    print("HelloWorld")

hello(N)

"""
print_star()가 하는 일: 2가지
print_star(n-1)을 실행한다 -> 실행하고 나서 별을 출력한다



print_star(3) ->print_star(2) 실행완료 -> 나머지 수행-> *****
print_star(2) ->print_star(1) 실행완료 -> 나머지 수행 -> ***** 
print_star(1) ->print_star(0) 실행완료 -> 나머지 수행-> *****
print_star(0)-> return
"""