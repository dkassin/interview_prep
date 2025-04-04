def replace_digits(s: str) -> str:
    solution = ""
    for index,value in enumerate(s):
        if index == 0 or index % 2 == 0:
            solution += value
        else:
            solution += shift(s[s[index-1], int(value)])
    
    def shift(c:str,x:int):
        return chr(ord(c)+x)