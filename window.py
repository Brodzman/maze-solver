from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, height, width):
        self.root = Tk()
        self.root.title('Maze Solver')
        self.canvas = Canvas(self.root, bg='white', height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:    
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, fill_colour='black'):
        line.draw(self.canvas, fill_colour)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.win = win

    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall == True:
            line=Line(Point(x1, y1), Point(x1, y2))
            self.win.draw_line(line)
        if self.has_bottom_wall == True:
            line=Line(Point(x1, y2), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_right_wall == True:
            line=Line(Point(x2, y1), Point(x2, y2))
            self.win.draw_line(line)
        if self.has_top_wall == True:
            line=Line(Point(x1, y1), Point(x2, y1))
            self.win.draw_line(line)