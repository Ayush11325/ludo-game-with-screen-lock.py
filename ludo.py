import pygame
import sys
import tkinter as tk
from tkinter import messagebox

class LockScreenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lock Screen")
        self.root.geometry("300x200")
        self.password = "ayush123"  # change kar skte h

        self.label = tk.Label(root, text="Enter Password:")
        self.label.pack(pady=20)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.button = tk.Button(root, text="Unlock", command=self.unlock)
        self.button.pack()

    def unlock(self):
        entered_password = self.password_entry.get()
        if entered_password == self.password:
            messagebox.showinfo("Success", "Lock Screen Unlocked!")
            self.root.destroy()
        else:
            messagebox.showerror("Error", "Incorrect Password")

if __name__ == "__main__":
    root = tk.Tk()
    app = LockScreenApp(root)
    root.mainloop()



pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
SCREEN_SIZE = (WIDTH, HEIGHT)
BACKGROUND_COLOR = (255, 255, 255)
SQUARE_SIZE = WIDTH // 15

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Ludo Game")

# Draw the Ludo board
def draw_board():
    screen.fill(BACKGROUND_COLOR)
    
    for i in range(0, WIDTH, SQUARE_SIZE):
        for j in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.rect(screen, RED, (i, j, SQUARE_SIZE, SQUARE_SIZE), 2)
            
    pygame.draw.rect(screen, GREEN, (0, 0, 6 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    pygame.draw.rect(screen, BLUE, (0, 9 * SQUARE_SIZE, 6 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    pygame.draw.rect(screen, YELLOW, (9 * SQUARE_SIZE, 0, 6 * SQUARE_SIZE, 6 * SQUARE_SIZE))
    pygame.draw.rect(screen, RED, (9 * SQUARE_SIZE, 9 * SQUARE_SIZE, 6 * SQUARE_SIZE, 6 * SQUARE_SIZE))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()


