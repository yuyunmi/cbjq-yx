import tkinter as tk
from get_frame import get_frame
import snow_dfs
from tkinter import messagebox

global image
global matrixs
global result_n
global widget

# 定义每个数字对应的颜色
colors = {
    0: "#27282E",
    1: "#B7D8F4",
    2: "#B5B6E1",
    3: "#89AECC",
    4: "#99D6D2",
    5: "#BAC59C",
    6: "#AED0A6",
    7: "#EAC69E",
    8: "#D0E29E",
    9: "#FF00AE",
    10: "#8A2BE2",
    11: "#FF00FF",
}


# 创建按钮并添加到网格中
def create_button_grid():
    global result_n
    if result_n < len(matrixs):
        result_n += 1

    rows = len(matrixs[result_n])
    columns = len(matrixs[result_n][0])

    buttons = [[None for _ in range(columns)] for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):

            button = tk.Button(widget, text=str(matrixs[result_n][i][j]), bg=colors.get(matrixs[result_n][i][j]),
                               width=50, height=50)
            # 设置按钮的实际大小
            button.config(width=6, height=2)
            # 将按钮放置到网格中
            button.grid(row=i, column=j, padx=1, pady=1)  # padx和pady是按钮间的间距
            # 保存按钮引用
            buttons[i][j] = button

    return buttons

# 更新下一方案
def update(widget, buttons, matrix, colors):
    global result_n
    result_n += 1
    for i in range(5):
        for j in range(6):
            buttons[i][j] = tk.Button(widget, text=str(matrix[result_n][i][j]), bg=colors.get(matrix[i][j]),
                                      width=50, height=50)


def result_draw():
    global matrixs
    global widget
    global result_n
    global image

    result_n = -1

    try:
        image = get_frame()

        image.save('cache.png')

    except:
        messagebox.showinfo("QAQ", "截图失败，请确定游戏窗口正确打开！")
        return
    matrixs = snow_dfs.get_dfs()

    if matrixs:

        widget = tk.Tk()
        widget.title('QWQ')
        widget.geometry('+200+200')

        create_button_grid()

        next_button = tk.Button(root, text="下一方案", command=create_button_grid)
        next_button.config(width=6, height=2)
        next_button.place(x=100)

        widget.mainloop()
    else:
        widget = tk.Tk()
        widget.title('QWQ')
        messagebox.showinfo("QAQ", "碎片不足，无法完成研析！")
        widget.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('研析小工具')
    root.geometry('230x50+1200+200')
    # root.maxsize(230, 50)
    root.minsize(230, 50)

    start_button = tk.Button(root, text='开始研析', font='Arial', width=50, height=50, command=result_draw)
    start_button.place(x=0, y=5, width=100, height=40)

    root.mainloop()
