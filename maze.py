from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.isrunning = False


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.isrunning = True
        while self.isrunning == True:
            self.redraw()
    
    def close(self):
        self.isrunning = False



def main():
    win = Window(800,600)
    win.wait_for_close()

if __name__ == "__main__":
    main()