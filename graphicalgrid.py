from typing import Any
import tkinter as tk


class GraphicalGrid:
    def __init__(self, size: int, w: int = 450, h: int = 480, text: int = 30):
        self.text = text
        self.size = size
        self.stop = False
        self.view = (w, h)
        self.values: dict[tuple[int, int], Any] = {}
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.on_quit)
        self.canvas = tk.Canvas(self.root, width=w, height=h)
        self.canvas["background"] = "white"
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.canvas.winfo_toplevel().title("Tic Tac Toe")
        self.canvas.update()
        self.draw_grid()

    def on_quit(self):
        """
        callback lors du click sur fermeture de fenêtre
        """
        self.stop = True

    def wait_quit(self):
        """
        attend explicitement la fermeture de la fenêtre graphique
        """
        while not self.stop:
            self.canvas.update()
        self.root.destroy()

    def draw_grid(self):
        """
        trace le plateau de jeu 
        """
        if self.stop:
            return

        self.canvas.delete("all")

        w = self.view[0] - self.text
        h = self.view[1] - self.text

        stepx = w / self.size
        stepy = h / self.size

        for c in range(self.size+1):
            self.canvas.create_text(c*stepx+self.text+stepx/2, self.text/2, text=str(c),
                                    width=stepx, font=("Purisa", int(stepx*.25)))
            if c == 0 or c == self.size:
                self.canvas.create_line(
                    c*stepx+self.text, self.text, c * stepx + self.text, h + self.text, fill="black", width=3)
            else:
                self.canvas.create_line(c*stepx+self.text, self.text, c *
                                        stepx+self.text, h + self.text, fill="black")

        for r in range(self.size+1):
            self.canvas.create_text(self.text/2, r*stepy+self.text+stepy/2, text=str(r),
                                    width=stepx, font=("Purisa", int(stepx*.25)))
            if r == 0 or r == self.size:
                self.canvas.create_line(self.text, r*stepy+self.text, w + self.text,
                                        r * stepy+self.text, fill="black", width=3)
            else:
                self.canvas.create_line(self.text, r*stepy+self.text, w + self.text,
                                        r * stepy+self.text, fill="black")

        self.canvas.update()

    def write(self, i: int, j: int, character: str):
        if i < 0 or i >= self.size or j < 0 or j >= self.size or (character != 'X' and character != 'O'):
            return

        w = self.view[0]
        h = self.view[1]

        stepx = (w - self.text) / self.size
        stepy = (h - self.text) / self.size

        if (i, j) in self.values:
            id = self.values[i, j]
            self.canvas.itemconfig(id, text=character)
        else:
            id = self.canvas.create_text(
                self.text + j*stepx + stepx / 2, 30 + i*stepy + stepy / 2, text=character, font=("Purisa", int(stepx*.75)))
            self.values[i, j] = id

        self.canvas.update()

    def erase(self, i: int, j: int):
        if (i, j) in self.values:
            self.canvas.delete(self.values[i, j])
            self.values.pop((i, j))
        self.canvas.update()


if __name__ == "__main__":
    grid = GraphicalGrid(10)

    grid.write(0, 1, 'X')
    grid.write(3, 4, 'O')
    grid.write(0, 0, 'O')
    grid.erase(3, 4)
    grid.write(3, 4, 'X')

    grid.wait_quit()
