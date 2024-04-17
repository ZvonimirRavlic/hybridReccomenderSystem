import math


def calculate_mse_and_rmse(data):
    squared_diff_sum = sum((actual - predicted) ** 2 for actual, predicted in data)
    mean_squared_error = squared_diff_sum / len(data)
    root_mean_squared_error = math.sqrt(mean_squared_error)
    return mean_squared_error, root_mean_squared_error
