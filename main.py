import numpy as np
import math


def rotationMatrix(x, y, alpha):
    R = np.array([[math.cos(alpha), math.sin(-1 * alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    M_positive = np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])
    M_negative = np.array([[1, 0, -1 * x], [0, 1, -1 * y], [0, 0, 1]])
    A = M_positive.dot(R).dot(M_negative)
    return A


def getNormal(a: list, b: list, c: list ) -> tuple:
    ny = (b[2] - a[2]) * (c[0] - a[0]) - (c[2] - a[2]) * (b[0] - a[0])
    nz = -((b[1] - a[1]) * (c[0] - a[0]) - (c[1] - a[1]) * (b[0] - a[0]))
    nx = -(nz * (b[2] - a[2]) + ny * (b[1] - a[1])) / (b[0] - a[0])

    return nx, ny, nz


def pointInFlat(a: list, b: list, c: list, x, y) -> bool:
    First = (a[0] - x) * (b[1] - a[1]) - (b[0] - a[0]) * (a[1] - y)
    Second = (b[1] - x) * (c[1] - b[1]) - (c[0] - b[0]) * (b[1] - y)
    Third = (c[0] - x) * (a[1] - c[1]) - (a[0] - c[0]) * (c[1] - y)
    if (First < 0) and (Second < 0) and (Third < 0):
        return True
    else:
        return False


if __name__ == '__main__':
    print('First task:')
    print(rotationMatrix(1, 1, 0.785))
    print('Second task:')
    print(getNormal([0, 1, 31, ], [10, 20, 0, ], [19, 11, 0]))
    print('Third task:')
    print(pointInFlat([0, 1, 31, ], [10, 20, 0, ], [19, 11, 0, ], 1, 10))
