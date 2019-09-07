# Project: Linear Regression


def get_y(m, b, x):
    y = m * x + b
    return y


# Write your calculate_error() function here
def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y_value = get_y(m, b, x_point)
    avalue = abs(y_value - y_point)
    return avalue


''' ###### for test calculate_error()
# this is a line that looks like y = x, so (3, 3) should lie on it. thus, error should be 0:
print(calculate_error(1, 0, (3, 3)))
# the point (3, 4) should be 1 unit away from the line y = x:
print(calculate_error(1, 0, (3, 4)))
# the point (3, 3) should be 1 unit away from the line y = x - 1:
print(calculate_error(1, -1, (3, 3)))
# the point (3, 3) should be 5 units away from the line y = -x + 1:
print(calculate_error(-1, 1, (3, 3)))
'''


# Write your calculate_all_error function here
def calculate_all_error(m, b, points):
    total_error = 0
    for point in points:
        mid_error = calculate_error(m, b, point)
        total_error += mid_error
    return total_error


''' ###### for test calculate_all_error()
# every point in this dataset lies upon y=x, so the total error should be zero:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 0, datapoints))
# every point in this dataset is 1 unit away from y = x + 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, 1, datapoints))
# every point in this dataset is 1 unit away from y = x - 1, so the total error should be 4:
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(1, -1, datapoints))
# the points in this dataset are 1, 5, 9, and 3 units away from y = -x + 1, respectively, so total error should be
# 1 + 5 + 9 + 3 = 18
datapoints = [(1, 1), (3, 3), (5, 5), (-1, -1)]
print(calculate_all_error(-1, 1, datapoints))
'''


# your list comprehension here
def predict(m, b, points):
    possible_ms = [m * 0.1 for m in range(-100, 101)]
    possible_bs = [m * 0.1 for m in range(-200, 201)]
    smallest_error = float('inf')
    best_m = 0
    best_b = 0
    for m in possible_ms:
        for b in possible_bs:
            if calculate_all_error(m, b, points) < smallest_error:
                best_m = m
                best_b = b
                smallest_error = calculate_all_error(m, b, points)
    return best_m, best_b, smallest_error


datapoints1 = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
print(predict(-1, 1, datapoints1))

