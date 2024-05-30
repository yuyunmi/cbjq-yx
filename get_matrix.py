import numpy as np
import cv2
from cut import get_matrix_pic


def get_matrix():
    # 读取图像
    image_path = get_matrix_pic()

    img = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

    # 自适应阈值处理
    thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    # 确定小正方形尺寸
    num_rows, num_cols = 5, 6
    square_height = img.shape[0] // num_rows
    square_width = img.shape[1] // num_cols

    # 创建结果矩阵
    result_matrix = np.zeros((num_rows, num_cols), dtype=int)

    # 遍历每个小正方形区域
    for i in range(num_rows):
        for j in range(num_cols):
            # 计算当前小正方形区域的像素均值
            roi = thresh_img[i * square_height:(i + 1) * square_height, j * square_width:(j + 1) * square_width]
            mean_value = np.mean(roi)

            # 根据均值判断颜色
            if mean_value < 32:
                result_matrix[i, j] = 0
            else:
                result_matrix[i, j] = -1

    return result_matrix
