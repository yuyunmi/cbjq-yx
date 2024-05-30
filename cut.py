import cv2

from ocr import ocr


def get_num():
    image = cv2.imread('./cache.png')

    image01 = image[159:292, 86:218]
    image02 = image[159:292, 223:356]
    image03 = image[295:428, 86:218]
    image04 = image[295:428, 223:356]
    image05 = image[432:564, 86:218]
    image06 = image[432:564, 223:356]
    image07 = image[568:701, 86:218]
    image08 = image[568:701, 223:350]
    image09 = image[704:837, 86:218]
    image10 = image[704:837, 223:356]

    image_list = [image01, image02, image03, image04, image05, image06, image07, image08, image09, image10]

    values = ocr(image_list)

    return values


def get_matrix_pic():

    image = cv2.imread('./cache.png')
    image0 = image[242:788, 561:1217]

    return image0
