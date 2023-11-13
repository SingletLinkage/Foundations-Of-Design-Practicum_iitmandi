import numpy as np

def cross_product(p1, p2, p3):
    v1 = np.array([p2[0] - p1[0], p2[1] - p1[1]])
    v2 = np.array([p3[0] - p2[0], p3[1] - p2[1]])
    return np.cross(v1, v2)

def is_convex_polygon(vertices):
    # Working principle: 
    # For a convex polygon, cross product of all of its edge vectors taken in order has the same sign
    n = len(vertices)
    sign = 0

    for i in range(n):
        p1, p2, p3 = vertices[i], vertices[(i + 1) % n], vertices[(i + 2) % n]
        current_cross_product = cross_product(p1, p2, p3)

        if sign == 0:                                       sign = np.sign(current_cross_product)
        elif (current_cross_product * sign) < 0:              return False
    return True

if __name__ == '__main__':
    vertices = [[600, 203], [595, 383], [365, 481], [280, 306], [417, 136]]
    result = is_convex_polygon(vertices)
    print("Is the polygon convex?", result)