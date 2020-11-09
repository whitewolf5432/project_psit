"""Project PSIT Draft Version"""
import tkinter


def main():
    """Main Function"""
    height = 600  # ความสูง
    width = 800  # ความกว้าง
    window = tkinter.Tk()  # initialize tkinter
    canvas = tkinter.Canvas(window, height=height,
                            width=width)  # กำหนด size canvas
    canvas.pack()  # การรวม Widget ที่ทำมาลง Canvas
    window.mainloop()  # รอการทำงานจาก User


main()
