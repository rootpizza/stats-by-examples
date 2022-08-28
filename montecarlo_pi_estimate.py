import math
import random


def rnd_between_minus_one_and_one():
    return (random.random() - .5) * 2


def estimate_pi(n):
    # Generate N random 2D points in the square with center (0, 0) and side 2
    random_points = [(rnd_between_minus_one_and_one(), rnd_between_minus_one_and_one()) for _ in range(n)]
    # Separate the ones inside the unit circle
    points_in_circle = [p for p in random_points if (p[0] ** 2 + p[1] ** 2) ** .5 < 1]
    # Ratio of points inside the unit circle
    ratio_inside = len(points_in_circle) / len(random_points)
    # Area of the square is side^2
    square_area = 2 ** 2
    # I can estimate the circle area using the square area and the ratio_inside
    circle_area = square_area * ratio_inside
    # The circle area can be obtained as A = π * r^2, so I can estimate π as A / r^2. Since r=1, the estimate is A
    pi_estimate = circle_area
    return pi_estimate


if __name__ == '__main__':
    print(f"π from math library is {math.pi}")
    for exponent in range(1, 8):
        pi_estimate = estimate_pi(n := 10 ** exponent)
        print(f"{n} random points: π estimate is {pi_estimate}")
