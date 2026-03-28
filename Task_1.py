def evaluate_polynomial(poly_dict, x):
    sum = 0
    for key in poly_dict.keys():
        sum = sum+pow(x, key)*poly_dict[key]
    return sum
