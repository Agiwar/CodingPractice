# sample variance:

# summation of each value with (element_value - mean_value(seq))^2, then divided by len(seq)


def get_variance(test_list):
    mean_val = sum(test_list) / len(test_list)
    summation = sum((num - mean_val) ** 2 for num in test_list)
    
    return round(summation / len(test_list), 2)


def get_variance(test_list):
    import numpy as np
    return round(np.std(test_list) ** 2, 2)