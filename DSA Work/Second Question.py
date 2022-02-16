# we will create a code that will carry out a calculation that computes the amount(sum) of the biggest numbers in the rundown(list).

def sum(arr, k):
    non_duplicate = set(arr)
    list_n = list(non_duplicate)
    list_n.sort(reverse=True)
    print(list_n)
    sum_results = 0
    for i in range(k):
        sum_results += list_n[i]
    print(sum_results)


sum([9, 6, 11, 2, 13, 5, 19, 17, 16, 2], 3)