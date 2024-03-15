# 변수 선언 및 입력:
text = input()
pattern = input()

def is_sub(str_idx):
    t = len(text)
    p = len(pattern)

    if str_idx + p > t:
        return False

    elif text[str_idx:str_idx+p] == pattern:
        return True
    
    


def print_str_idx():
    for i in range(len(text)):
        if is_sub(i):
            return(i)
        
        
    return(-1)


print(print_str_idx())