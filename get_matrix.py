import numpy as np
from cut import get_matrix_pic


def get_matrix():

    image = get_matrix_pic()

    result_matrix = np.zeros((5, 6), dtype=int)

    for i in range(5):
        for j in range(6):
            if image[55 + 108 * i, 55 + 108 * j] > 200:
                result_matrix[i][j] = 0
            else:
                result_matrix[i][j] = -1

    print(result_matrix)

    return result_matrix
