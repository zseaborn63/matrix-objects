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

class Matrix(Vector):

    def __init__(self, matrix):
        self.matrix = matrix
        for row in self.matrix:
            self.row = row

    def __str__(self):
        return "{}".format(self.matrix)

    @property
    def shape(self):
        for row in self.matrix:
            num_rows = len(self.matrix)
            for col in row:
                num_col = len(row)
        return num_rows, num_col

    def shape_checker(self, other):
        if self.shape[1] != other.shape[0]:
            raise ValueError("Shape Rule Violated!")

    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape Rule Violated!")
        output_matrix = []
        for self.row in self.matrix:
            output_row = []
            for x in range(len(self.row)):
                output_num = self.row[x] + other.row[x]
                output_row.append(output_num)
            output_matrix.append(output_row)
        return output_matrix

    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape Rule Violated!")
        output_matrix = []
        for self.row in self.matrix:
            output_row = []
            for x in range(len(self.row)):
                output_num = self.row[x] - other.row[x]
                output_row.append(output_num)
            output_matrix.append(output_row)
        return output_matrix

    def __mul__(self, other):
        if type(other) == int:
            output_matrix = []
            for self.row in self.matrix:
                output_row = []
                for column in self.row:
                    calculated_value = column * other
                    output_row.append(calculated_value)
                output_matrix.append(output_row)
            return output_matrix
        else:
            other = Vector(other)
            #self.shape_checker(other)
            final_vec = []
            for self.row in self.matrix:
                placeholder = 0
                for x in range(len(self.row)):
                    placeholder += self.row[x] * other[x]
                final_vec.append(placeholder)
            return final_vec
