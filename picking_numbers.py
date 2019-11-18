#
# https://www.hackerrank.com/challenges/picking-numbers/problem
#
#
# Refactor idea: Only count frequency of pair of numbers where difference is 1 or smaller than 1
#
def pickingNumbers(arry):
    arr = sorted(arry)
    arr_2d = []
    answer = 0

    for index, x in enumerate(arr):
        temp_arr = []
        temp_arr.append(x)
        for y in arr[index+1:]:
            if abs(x - y) < 2:
                temp_arr.append(y)
            elif abs(x - y) >= 2:
                arr_2d.append(temp_arr)
                break
            arr_2d.append(temp_arr)            

    for inner_arr in arr_2d:
        if len(inner_arr) > answer:
            answer = len(inner_arr)   

    return answer 