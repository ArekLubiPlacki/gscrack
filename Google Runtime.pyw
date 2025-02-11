import tkinter as tk
import random
import time

def place_window_top(window):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = 150  # Stała szerokość okna
    window_height = 25  # Stała wysokość okna
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")  
    window.attributes('-topmost', True)

def wyswietl_okno():
    while True:
        new_window = tk.Toplevel(root)
        new_window.title("Critical Error")
        error_codes = ["YOU ARE AN IDIOT ☻☺︎☻"]
        error_message = f"{random.choice(error_codes)}"
        label = tk.Label(new_window, text=error_message)
        label.pack()
        place_window_top(new_window)

        new_window.protocol("WM_DELETE_WINDOW", lambda: None)
        new_window.overrideredirect(True)

        root.update()
        time.sleep(0.5)
	

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    wyswietl_okno()
    root.mainloop()