# Imports
from tkinter import Tk, BOTH, Canvas


# Window Class 
# Constructor idht, height in pixexes

class Window:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = Canvas()
        self.__canvas.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__canvas.update()
        self.__canvas.update_idletasks()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        
    def close(self):
        self.__is_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

# point classs 2 public data x and y coords
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


# class line, 2 points as input
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill=fill_color,
            width=2
        )
        canvas.pack()

# cell class, 
class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        self._win = win

    def draw(self):
        if self.has_left_wall:
            temp_line = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(temp_line, "red")

        if self.has_right_wall:
            temp_line = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(temp_line, "red")

        if self.has_top_wall:
            temp_line = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(temp_line, "red")

        if self.has_bottom_wall:
            temp_line = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(temp_line, "red")




def main():
    win = Window(800, 600)

    test_cell = Cell(100,200,100,200,win)
    test_cell.draw()


    win.wait_for_close()

   
if __name__ == "__main__":
    main()