def evaluate_polynomial(poly_dict, x):
    sum = 0
    for key in poly_dict.keys():
        sum = sum+pow(x, key)*poly_dict[key]
    return sum
my_poly = {0: -10, 2: 3, 4: 1}
x=2
print(evaluate_polynomial(my_poly, x))