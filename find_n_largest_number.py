def n_largest(lst, n):
    sorted_lst = sorted(lst)
    largest_elements = sorted_lst[int(-n):]
    return largest_elements

sample =  [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34, 69]

N = int(input(f"Number upto: "))

result = n_largest(sample, N)

print(result)

#sorting can be reversed to implement the descending counting
