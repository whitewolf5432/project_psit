"""Project PSIT Draft Version"""
import tkinter


def main():
    """Main Function"""
    # Window settings
    height = 600  # ความสูง
    width = 800  # ความกว้าง
    window = tkinter.Tk()  # initialize tkinter
    canvas = tkinter.Canvas(window, height=height,
                            width=width)  # กำหนด size canvas

    # Widget settings
    button_ans1 = tkinter.Button(canvas, text="1", font=40)  # ปุ่มตอบ 1
    button_ans2 = tkinter.Button(canvas, text="2", font=40)  # ปุ่มตอบ 2
    button_ans3 = tkinter.Button(canvas, text="3", font=40)  # ปุ่มตอบ 2
    button_ans4 = tkinter.Button(canvas, text="4", font=40)  # ปุ่มตอบ 2

    # Pack widget to canvas
    canvas.pack()  # การรวม Widget ที่ทำมาลง Canvas

    # วางตำแหน่งปุ่มคำตอบ
    button_ans1.place(height=125, width=250, x=100, y=180)
    button_ans2.place(height=125, width=250, x=450, y=180)
    button_ans3.place(height=125, width=250, x=100, y=360)
    button_ans4.place(height=125, width=250, x=450, y=360)

    window.mainloop()  # รอการทำงานจาก User


main()
