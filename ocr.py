from tkinter import messagebox
from cnocr import CnOcr

result_dict = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0
}


def ocr(img_list):
    try:
        ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3')
        for img in img_list:
            # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            out = ocr.ocr(img)
            list = []
            for x in out:
                if x['text'].isdigit():
                    list.append(int(x['text']))

            if len(list) == 2 and 1 <= list[0] <= 11 and isinstance(list[1], int):
                result_dict[list[0]] = list[1]

        values = []

        for i in range(1, 12):
            values.append(result_dict[i])

        return values

    except:
        messagebox.showinfo("QAQ", "ocr模型读取错误，请手动完成模型配置!")
