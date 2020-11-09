"""Project PSIT Draft Version"""
import tkinter


def main():
    """Main Function"""
    height = 600
    width = 800
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, height=height, width=width)
    canvas.pack()
    window.mainloop()


main()
