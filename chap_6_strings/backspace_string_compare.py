def backspace_compare(s: str, t: str) -> bool:
    ## First Solution - Does beat 100%

    # string_1 = []
    # string_2 = []

    # for i in s:
    #     if i == "#":
    #         if len(string_1) == 0:
    #             continue
    #         else:
    #             string_1.pop()
    #     else:
    #         string_1.append(i)

    # for j in s:
    #     if j == "#":
    #         if len(string_2) == 0:
    #             continue
    #         else:
    #             string_2.pop()
    #     else:
    #         string_2.append(j)
    
    # return string_1 == string_2
    solution,start = [], [s,t]
    for i in start:
        string_value = []
        for char in i:
            if char == "#":
                if len(string_value) == 0:
                    continue
                else:
                    string_value.pop()
            else:
                string_value.append(char)
        solution.append(string_value)
    return string_value[0] == string_value[1]
        

        