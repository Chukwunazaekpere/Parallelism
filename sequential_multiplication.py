"""
Author: Chukwunazaekpere Emmanuel Obioma
Lecture: Parallelism
Nationality: Biafran
Email-1: chukwunazaekpere.obioma@ue-germany.de 
Email-2: ceo.naza.tech@gmail.com
************************************************
Implementation: to implement the sequential multiplication of squared matrices
Course: Multi-core Programming
Written: Oct 21st 2024
Due: Oct 23rd 2024
"""

from datetime import datetime
import random
from time import time
import logging
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)


class Sequential_Matrix_Multiplication():
    def __init__(self):
        self.row_dim = 0

    def get_mat_size(self):
        logging.info(msg=f"\n\t {datetime.now()} This is the sequential matrix multiplication algorithm...")
        try:
            matrix_size = input("\n\t Please enter a matrix size: ")
            self.row_dim = int(matrix_size)
        except Exception as err:
            return f"Matrix dimension unacceptable. Please enter a number."

    def generate_random_matrix(self):
        count = 0
        matrix = []
        while count < self.row_dim:
            new_row = []
            for val in range(0, self.row_dim):
                value = random.randint(2, 100) # generate random matrix elements
                new_row.append(value)
            matrix.append(new_row)
            count+=1
        return matrix
    
    def sequential_multiplication(self):
        matrix_A = self.generate_random_matrix()
        matrix_B = self.generate_random_matrix()
        logging.info(msg=f"The first generated {self.row_dim} by {self.row_dim} matrix is: {matrix_A}")
        logging.info(msg=f"The second generated {self.row_dim} by {self.row_dim} matrix is: {matrix_B}")
        dot_product = []
        multiply_comp = 0
        for matrix_A_rows in matrix_A:
            index_of_row_in_A = 0
            matrix_B_row_index= 0
            matrix_B_col_index= 0
            row_sums = []
            while True:
                multiply_comp+= (matrix_A_rows[matrix_B_row_index]*(matrix_B[matrix_B_row_index])[matrix_B_col_index])
                add_row_B_index = True
                if matrix_B_row_index == self.row_dim-1:
                    index_of_row_in_A+=1
                    matrix_B_col_index+=1
                    matrix_B_row_index=0
                    add_row_B_index = False
                    row_sums.append(multiply_comp)
                    multiply_comp = 0
                if index_of_row_in_A == self.row_dim:
                    dot_product.append(row_sums)
                    break
                matrix_B_row_index+= 1 if add_row_B_index else 0
        # print("\n\t matrices: ", matrix_A, matrix_B)
        return dot_product


if __name__ == "__main__":
    mat_mult = Sequential_Matrix_Multiplication()
    start_time = time()
    mat_dim = mat_mult.get_mat_size()
    if mat_dim == None:
        dim = mat_mult.sequential_multiplication()
        end_time = time()
        print(f"\n\t total time taken: {(end_time-start_time)} secs")
    else:
        print(mat_dim)
    



    
