#This is my matrix_math module
from functools import reduce

class Vector:

    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return "{}".format(self.vector)

    @property
    def shape(self):
        return len(self.vector)

    @property
    def magnitude(self):
        mag = 0
        for x in range(self.shape):
            mag += self.vector[x] ** 2
            mag = mag ** 0.5
        return mag

    def shape_rule_check(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape Rule Violation!")

    def dot_product(self, other):
        self.shape_rule_check(other)
        vec_for_add = []
        for x in range(self.shape):
            pos_multiplication = self.vector[x] * other.vector[x]
            vec_for_add.append(pos_multiplication)
        dot_total = reduce(lambda x, y: x + y, vec_for_add)
        return dot_total

    def __add__(self, other):
        self.shape_rule_check(other)
        output_vector = []
        for i in range(self.shape):
            output_num = self.vector[i] + other.vector[i]
            output_vector.append(output_num)
        return output_vector

    def __sub__(self, other):
        self.shape_rule_check(other)
        output_vector = []
        for i in range(self.shape):
            output_num = self.vector[i] - other.vector[i]
            output_vector.append(output_num)
        return output_vector

    def __mul__(self, scalar):
        output_vector = []
        for i in range(self.shape):
            output_num = self.vector[i] * scalar
            output_vector.append(output_num)
        return output_vector
