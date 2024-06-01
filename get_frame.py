from win32gui import *
import win32con
from PIL import ImageGrab


def get_frame():
    names = set()

    def get_window_title(window, nouse):
        if IsWindow(window) and IsWindowEnabled(window) and IsWindowVisible(window):
            names.add(GetWindowText(window))

    EnumWindows(get_window_title, 0)

    list_ = [name for name in names if name]

    name = '尘白禁区'

    window = FindWindow(0, name)

    ShowWindow(window, win32con.SW_MAXIMIZE)

    x_start, y_start, x_end, y_end = GetWindowRect(window)

    # 坐标信息
    box = (x_start, y_start, x_end + 200, y_end + 200)

    image = ImageGrab.grab(box)

    return image
