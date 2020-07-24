# import required functions from modules math, decimal
from math import pow
from decimal import Decimal, ROUND_DOWN

# declare global variables for the script
user_choice = str()
proceed_with_operation = False


class NumericMatrixProcessor:

    def user_interface(self):
        global user_choice
        # read input from user
        while True:
            user_choice = input('\n'
                                '1. Add matrices\n'
                                '2. Multiply matrix by a constant\n'
                                '3. Multiply matrices\n'
                                '4. Transpose matrix\n'
                                '5. Calculate a determinant\n'
                                '6. Inverse matrix\n'
                                '0. Exit\n'
                                'Your choice: ')
            # break loop if user chose '0. Exit' option
            if user_choice == '0':
                break
            elif user_choice == '1':
                NumericMatrixProcessor.sum_matrices(self)
            elif user_choice == '2':
                NumericMatrixProcessor.multiply_matrix_by_a_constant(self)
            elif user_choice == '3':
                NumericMatrixProcessor.multiply_matrices(self)
            elif user_choice == '4':
                NumericMatrixProcessor.transpose_matrix(self)
            elif user_choice == '5':
                NumericMatrixProcessor.calculate_determinant(self)
            elif user_choice == '6':
                NumericMatrixProcessor.get_inverse_matrix(self)

    # script for matrix initialization
    def initialize_matrix(self, rows, columns):
        # take matrix elements as input from user and store in as str objects in nested list
        matrix_elements = [[matrix_element for matrix_element in input().split(maxsplit=columns - 1)] for _row in
                           range(rows)]
        # try to initialize matrix elements as integers
        try:
            matrix = [[int(matrix_element) for matrix_element in matrix_elements[row]] for row in range(rows)]
        # initialize matrix elements as floats if user provided float numbers
        except ValueError:
            matrix = [[float(matrix_element) for matrix_element in matrix_elements[row]] for row in range(rows)]
        return matrix

    def set_up_for_calculations(self):
        global user_choice
        # if user chose one of the following options:
        #   2. Multiply matrix by a constant
        #   4. Transpose matrix
        #   5. Calculate a determinant
        #   6. Inverse matrix
        # initialize 1 matrix
        if user_choice in ['2', '4', '5', '6']:
            rows, columns = [int(x) for x in input('Enter size of matrix: ').split(maxsplit=1)]
            print('Enter matrix:')
            matrix = NumericMatrixProcessor.initialize_matrix(self, rows, columns)
            return matrix
        # if user chose one of the following options:
        #   1. Add matrices
        #   3. Multiply matrices
        # initialize 2 matrices
        elif user_choice == '1' or user_choice == '3':
            # initialize first matrix
            matrix_1_rows, matrix_1_columns = [int(x) for x in input('Enter size of first matrix: ').split(maxsplit=1)]
            print('Enter first matrix:')
            matrix_1 = NumericMatrixProcessor.initialize_matrix(self, matrix_1_rows, matrix_1_columns)
            # initialize second matrix
            matrix_2_rows, matrix_2_columns = [int(x) for x in input('Enter size of second matrix: ').split(maxsplit=1)]
            print('Enter second matrix:')
            matrix_2 = NumericMatrixProcessor.initialize_matrix(self, matrix_2_rows, matrix_2_columns)
            return matrix_1, matrix_2

    def check_matrices_dimensions(self, matrix_1, matrix_2):
        global user_choice, proceed_with_operation
        # if user chose to sum matrices
        # return True if matrices are of the same size
        if user_choice == '1' and len(matrix_1) == len(matrix_2) and len(matrix_1[0]) == len(matrix_2[0]):
            proceed_with_operation = True
        # if user chose to multiply matrices
        # return True if the number of columns of the 1st matrix is equal to the number of rows of the 2nd matrix.
        elif user_choice == '3' and len(matrix_1[0]) == len(matrix_2):
            proceed_with_operation = True
        # return False if dimensions are wrong
        else:
            proceed_with_operation = False
        return proceed_with_operation

    # script to sum matrices of the same size
    def sum_matrices(self):
        global proceed_with_operation
        # initialize matrices
        matrix_1, matrix_2 = NumericMatrixProcessor.set_up_for_calculations(self)
        # check matrices dimensions
        NumericMatrixProcessor.check_matrices_dimensions(self, matrix_1, matrix_2)
        # sum matrices
        if proceed_with_operation:
            result = [[matrix_1[row][column] + matrix_2[row][column] for column in range(len(matrix_1[row]))] for row in
                      range(len(matrix_1))]
            return NumericMatrixProcessor.output_result(self, result)
        else:
            return NumericMatrixProcessor.error_message(self)

    # script to multiply matrix by a constant
    def multiply_matrix_by_a_constant(self, matrix=None, constant=None, infunction_calc=False):
        # initialize matrix and constant if not provided by user - used for 2. Multiply matrix by a constant option
        if not infunction_calc:
            # initialize matrix and constant
            matrix = NumericMatrixProcessor.set_up_for_calculations(self)
            # try to initialize constant as integer:
            constant = input('Enter constant: ')
            try:
                constant = int(constant)
            except ValueError:
                constant = float(constant)
        # carry out matrix by constant multiplication
        calc_result = [[matrix[row][column] * constant for column in range(len(matrix[row]))] for row in
                       range(len(matrix))]

        # output result for non-infunction calculations
        if not infunction_calc:
            return NumericMatrixProcessor.output_result(self, calc_result)
        else:
            return calc_result

    # script for matrices multiplication
    def multiply_matrices(self):
        # initialize matrices
        matrix_1, matrix_2 = NumericMatrixProcessor.set_up_for_calculations(self)
        # check matrices dimensions
        NumericMatrixProcessor.check_matrices_dimensions(self, matrix_1, matrix_2)
        # multiply matrices
        if proceed_with_operation:
            calc_result = list()
            for matrix_1_row in range(len(matrix_1)):
                calc_result.append(list())
                for matrix_2_column in range(len(matrix_2[matrix_1_row])):
                    product = 0
                    for matrix_1_column in range(len(matrix_1[matrix_1_row])):
                        product += matrix_1[matrix_1_row][matrix_1_column] * matrix_2[matrix_1_column][matrix_2_column]
                    calc_result[matrix_1_row].append(product)
            return NumericMatrixProcessor.output_result(self, calc_result)
        else:
            return NumericMatrixProcessor.error_message(self)

    # script for matrix transposition
    def transpose_matrix(self, transpose_option=None, matrix=None, infunction_calc=False):
        # initialize transpose_option & matrix if not provided by user - used for option 4. Transpose matrix
        if not infunction_calc:
            # initialize transpose option chosen by user
            transpose_option = input('\n'
                                     '1. Main diagonal\n'
                                     '2. Side diagonal\n'
                                     '3. Vertical line\n'
                                     '4. Horizontal line\n'
                                     'Your choice: ')
            # initialize matrix and constant
            matrix = NumericMatrixProcessor.set_up_for_calculations(self)
        # transpose matrix along main diagonal if user chose to
        if transpose_option == '1':
            matrix = [[matrix[column][row] for column in range(len(matrix))] for row in range(len(matrix[0]))]
        # transpose matrix along side diagonal if user chose to
        elif transpose_option == '2':
            for row in range(len(matrix)):
                for column in range(len(matrix) - row):
                    temp = matrix[row][column]
                    matrix[row][column] = matrix[len(matrix) - 1 - column][len(matrix) - 1 - row]
                    matrix[len(matrix) - 1 - column][len(matrix) - 1 - row] = temp
        # transpose matrix along the vertical line if user chose to
        elif transpose_option == '3':
            for row in matrix:
                row.reverse()
            return NumericMatrixProcessor.output_result(self, matrix)
        # transpose matrix along the horizontal line if user chose to
        elif transpose_option == '4':
            matrix.reverse()
        # output matrix transposition result
        if not infunction_calc:
            # output matrix in formatted view for non-infunction calc
            return NumericMatrixProcessor.output_result(self, matrix)
        else:
            return matrix

    # script for calculation of matrix determinant
    def calculate_determinant(self):
        # initialize matrix and constant
        matrix = NumericMatrixProcessor.set_up_for_calculations(self)
        # output error message for non-square matrix
        if len(matrix) != len(matrix[0]):
            return NumericMatrixProcessor.error_message(self)
        # call recursive function to calculate matrix determinant
        matrix_determinant = NumericMatrixProcessor.determinant_recursive(self, matrix)
        # output matrix determinant
        return NumericMatrixProcessor.output_result(self, matrix_determinant)

    # script for getting matrix minor
    def get_matrix_minor(self, matrix, matrix_row, matrix_column):
        return [row[:matrix_column] + row[matrix_column + 1:] for row in
                (matrix[:matrix_row] + matrix[matrix_row + 1:])]

    # script for recursive function to calculate determinant
    def determinant_recursive(self, matrix):
        # output determinant for 1x1 matrix
        if len(matrix) == 1:
            return matrix[0][0]
        # base case for recursive function - 2x2 matrix determinant
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        matrix_determinant = 0
        # loop through 1st row of matrix to calculate determinant
        for column in range(len(matrix)):
            matrix_determinant += \
                pow(-1, column) * \
                matrix[0][column] * \
                NumericMatrixProcessor.determinant_recursive(self,
                                                             NumericMatrixProcessor.get_matrix_minor(self,
                                                                                                     matrix,
                                                                                                     0,
                                                                                                     column)
                                                             )
        return matrix_determinant

    # script to get inverse matrix
    def get_inverse_matrix(self):
        # initialize matrix and constant
        matrix = NumericMatrixProcessor.set_up_for_calculations(self)
        # check if matrix determinant is equal to 0 or not
        # output error message for matrix with zero determinant
        if NumericMatrixProcessor.determinant_recursive(self, matrix) == 0:
            return NumericMatrixProcessor.error_message(self, inverse=True)
        # calculate inverse determinant of the matrix
        inverse_determinant = 1 / NumericMatrixProcessor.determinant_recursive(self, matrix)
        # calculate cofactor matrix
        cofactor_matrix = \
            [
                [
                    pow(-1, (row + 1) + (column + 1)) * NumericMatrixProcessor.determinant_recursive(self,
                                                                                                     NumericMatrixProcessor.get_matrix_minor(
                                                                                                         self,
                                                                                                         matrix,
                                                                                                         row,
                                                                                                         column)
                                                                                                     )
                    for column in range(len(matrix[row]))
                ]
                for row in range(len(matrix))
            ]
        # transpose cofactor matrix to get adjoint matrix
        cofactor_matrix_transposed = NumericMatrixProcessor.transpose_matrix(self, '1', cofactor_matrix, True)
        # multiply inverse determinant by cofactor matrix to get inverse of a matrix
        inverse_matrix = NumericMatrixProcessor.multiply_matrix_by_a_constant(self,
                                                                              cofactor_matrix_transposed,
                                                                              inverse_determinant,
                                                                              True)
        # output inverse matrix
        return NumericMatrixProcessor.output_result(self, inverse_matrix)

    # script to output matrix
    def output_result(self, result):
        global user_choice
        # output matrices if user chose any option from the list:
        #   1. Add matrices
        #   2. Multiply matrix by a constant
        #   3. Multiply matrices
        #   4. Transpose matrix
        #   6. Inverse matrix
        # format numbers in the matrix properly before output:
        #   a) 2 decimal points for floats,
        #   b) no negative zeros
        if user_choice != '5':
            # format output for inverse matrix calculations
            if user_choice == '6':
                for row in range(len(result)):
                    for digit in range(len(result[row])):
                        # check if matrix element equals zero - it might have '-' sign that program should get rid off
                        # with this block of code
                        if result[row][digit] == 0:
                            result[row][digit] = round(result[row][digit] + 0)
                        else:
                            if not (isinstance(result[row][digit], int)):
                                result[row][digit] = Decimal(str(result[row][digit])).quantize(Decimal('1.00'),
                                                                                               ROUND_DOWN)
                            else:
                                result[row][digit] = round(result[row][digit])
            print('The result is:', '\n'.join([' '.join([str(digit) for digit in row]) for row in result]), sep='\n')
        else:
            print('The result is:', result, sep='\n')

    # script for error message output
    def error_message(self, inverse=False):
        if inverse:
            print('This matrix doesn\'t have an inverse.')
        else:
            print('The operation cannot be performed.')


if __name__ == '__main__':
    matrix_processor = NumericMatrixProcessor()
    matrix_processor.user_interface()
