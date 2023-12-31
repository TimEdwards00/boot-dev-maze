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

    def draw_line(self,line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack()

def main():
    win = Window(800,600)

    p1 = Point(100,100)
    p2 = Point(200, 250)
    l1 = Line(p1,p2)

    win.draw_line(l1, "red")

    win.wait_for_close()

if __name__ == "__main__":
    main()