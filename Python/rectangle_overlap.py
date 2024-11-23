def rectangle_overlap(a, b):
    a_min_x = min(point[0] for point in a)
    a_max_x = max(point[0] for point in a)
    a_min_y = min(point[1] for point in a)
    a_max_y = max(point[1] for point in a)

    return any(
        (a_min_x <= point_b[0] <= a_max_x and a_min_y <= point_b[1] <= a_max_y)
        for point_b in b
    )