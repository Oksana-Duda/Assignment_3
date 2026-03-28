def evaluate_polynomial(poly_dict, x):
    sum = 0
    for key in poly_dict.keys():
        sum = sum+pow(x, key)*poly_dict[key]
    return sum
my_poly = {}
x=int(input())
while True:
    try:
        c_key, c_val=map(int, input().split())
        my_poly[c_key] = c_val
    except ValueError: break


print(evaluate_polynomial(my_poly, x))