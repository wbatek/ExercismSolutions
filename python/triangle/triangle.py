def correct_triangle(sides):
    if not all(side > 0 for side in sides):
        return False
    s = sorted(sides)
    if not s[0] + s[1] >= s[2]:
        return False
    return True


def equilateral(sides):
    if not correct_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not correct_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides):
    if not correct_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
