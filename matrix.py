import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here  
        return self[0][0] * self[1][1] - self[0][1] * self[1][0]
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        trace = 0
        for i in range(self.h):
            for j in range(self.h):
                trace += (self[i][j] if i == j else 0)        
        
        return trace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
        inverse = []
        
        if self.h == 1:
            inverse.append([1 / self[0][0]])
        elif self.h == 2:
            factor = 1 / Matrix.determinant(self)
            inverse = [[self[1][1], -self[0][1]], [-self[1][0], self[0][0]]]
            
            for i in range(len(inverse)):
                for j in range(len(inverse[0])):
                    inverse[i][j] = factor * inverse[i][j]
    
        return Matrix(inverse)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        transpose = []
        for row_num in range(self.w):
            new_row = []
            for col_num in range(self.h):
                new_row.append(self[col_num][row_num])
            transpose.append(new_row)
                   
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        # TODO - your code here
                   
        total = []
        for i in range(self.h):
            row_sum = []
            for j in range(self.w):
                row_sum.append(self[i][j] + other[i][j])
            total.append(row_sum)
        return Matrix(total)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
         
        # TODO - your code here
        
        return Matrix.__rmul__(self, -1)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
          
        # TODO - your code here
        
        difference = []
        for i in range(self.h):
            row_diff = []
            for j in range(self.w):
                row_diff.append(self[i][j] - other[i][j])
            difference.append(row_diff)
        return Matrix(difference)           
                   
    def dot_product(vector_one, vector_two):
        dot = 0
        for i in range(len(vector_one)):
            dot = dot + vector_one[i] * vector_two[i]
        return dot
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
           
        # TODO - your code here
        product = []
    
        other_transpose = Matrix.T(other)
    
        for row_num in range(self.h):
            row_result = []
            for col_num in range(other.w):
                row_result.append(Matrix.dot_product(self[row_num], other_transpose[col_num]))
            product.append(row_result)
        
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
               
            # TODO - your code here
        r = []

        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(other * self[i][j])
            r.append(new_row)
        return Matrix(r)
            