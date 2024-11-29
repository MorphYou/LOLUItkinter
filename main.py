import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

lastClickX, lastClickY = 0, 0

def zamknij_okno():
    root.destroy()

def saveLastClick(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def drag(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry(f"+{x}+{y}")


# Create the main window
root = ttk.Window(themename="darkly", overrideredirect=TRUE)
root.geometry("800x600")

# Create navbar frame
navbar = ttk.Frame(root, style="secondary.TFrame", cursor="hand2")
navbar.pack(side=TOP, fill=X)

navbar.bind("<Button-1>", saveLastClick)
navbar.bind("<B1-Motion>", drag)

# Add some buttons to navbar
home_btn = ttk.Button(navbar, text="Patch Notes", style="secondary.Outline.TButton", command=lambda: webbrowser.open("https://www.tacter.com/lol/guides/patch-1424-lol-1424-patch-notes-43588798"))
home_btn.pack(side=LEFT, padx=5, pady=5)

# Add some elements to navbar
nav_title = ttk.Label(navbar, text="Lol Stats Finder", style="secondary.Inverse.TLabel", font=("Helvetica", 12, "bold"))
nav_title.place(relx=0.5, rely=0.5, anchor="center")

# Add some buttons to navbar
about_btn = ttk.Button(navbar, text="X", style="secondary.Outline.TButton", command=zamknij_okno)
about_btn.pack(side=RIGHT, padx=5, pady=5)

#main
main_content = ttk.Frame(root)
main_content.pack(side=TOP, fill=BOTH, expand=True)

#avatar..
player_info_frame = ttk.Frame(main_content)
player_info_frame.pack(side=LEFT, padx=20, pady=20, fill=Y)

player_info_container = ttk.Frame(player_info_frame)
player_info_container.pack(fill=X)

avatar_frame = ttk.Frame(player_info_container, width=128, height=128, style="secondary.TFrame")
avatar_frame.pack(side=LEFT, pady=(0, 10))
avatar_frame.pack_propagate(False)

info_text_container = ttk.Frame(player_info_container)
info_text_container.pack(side=LEFT, padx=(10, 0), pady=(0, 10))

nickname_label = ttk.Label(info_text_container, text="Nickname", font=("Helvetica", 16, "bold"))
nickname_label.pack(anchor=W)

level_label = ttk.Label(info_text_container, text="Level: 0")
level_label.pack(anchor=W)

#szukanie
search_frame = ttk.Frame(main_content)
search_frame.pack(pady=20, anchor=E, padx=20)

search_label = ttk.Label(search_frame, text="Wyszukaj gracza")
search_label.pack(pady=(0, 5))

search_entry = ttk.Entry(search_frame, width=40)
search_entry.pack(side=LEFT, padx=5)

search_button = ttk.Button(search_frame, text="Szukaj", style="primary.TButton")
search_button.pack(side=LEFT, padx=5)

root.mainloop()
