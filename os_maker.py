#!/usr/bin/env python3
"""Windows 7 HDMI mockup desktop generator.

This is a visual mockup-only project. It creates a fullscreen Windows 7-inspired
UI on a 1920x1080 HDMI-style desktop, useful for demonstration and prototyping.
It does not produce a real bootable operating system.
"""

import os
import tkinter as tk
from tkinter import messagebox


class HDMIWindows7Mockup(tk.Tk):
    """Fullscreen mockup styled like Windows 7 on a standard HDMI display."""

    def __init__(self):
        super().__init__()
        self.title("Windows 7 HDMI Mockup")
        self.geometry("1920x1080")
        self.attributes("-fullscreen", True)
        self.configure(bg="#4e89d8")

        self.screen_w = self.winfo_screenwidth()
        self.screen_h = self.winfo_screenheight()

        self.canvas = tk.Canvas(
            self,
            width=self.screen_w,
            height=self.screen_h,
            bg="#4e89d8",
            highlightthickness=0,
        )
        self.canvas.pack(fill="both", expand=True)

        self.start_menu_open = False
        self._draw_desktop()

    def _draw_desktop(self):
        # wallpaper/background
        self.canvas.create_rectangle(0, 0, self.screen_w, self.screen_h, fill="#4f8edc", outline="")

        # subtle glow shapes to mimic a Windows 7 desktop wallpaper
        self.canvas.create_rectangle(0, 0, self.screen_w, self.screen_h, fill="#4f8edc", outline="")
        self.canvas.create_rectangle(0, self.screen_h // 2, self.screen_w, self.screen_h, fill="#4b78c8", outline="")
        self.canvas.create_polygon(
            [
                self.screen_w * 0.68, 0,
                self.screen_w, 0,
                self.screen_w, self.screen_h * 0.45,
                self.screen_w * 0.80, self.screen_h * 0.22,
                self.screen_w * 0.70, self.screen_h * 0.05,
            ],
            fill="#82b7ff",
            outline="",
        )

        # desktop shortcuts
        icons = [
            ("Computer", 60, 60),
            ("Documents", 60, 150),
            ("Pictures", 60, 240),
            ("Network", 60, 330),
            ("Recycle Bin", 60, 420),
        ]

        for label, x, y in icons:
            self.canvas.create_rectangle(x, y, x + 60, y + 60, fill="#dfe9f8", outline="#b9cae8")
            self.canvas.create_text(x + 30, y + 72, text=label, fill="white", font=("Segoe UI", 10, "bold"))

        # center hero text area for a "mock OS" look
        self.canvas.create_rectangle(
            self.screen_w * 0.53,
            self.screen_h * 0.18,
            self.screen_w * 0.82,
            self.screen_h * 0.58,
            fill="#ebf2ff",
            outline="#d8e5ff",
            width=2,
        )
        self.canvas.create_text(
            self.screen_w * 0.675,
            self.screen_h * 0.25,
            text="OS Maker",
            fill="#1e2d52",
            font=("Segoe UI", 26, "bold"),
        )
        self.canvas.create_text(
            self.screen_w * 0.675,
            self.screen_h * 0.31,
            text="HDMI mock display",
            fill="#2d4a73",
            font=("Segoe UI", 18),
        )
        self.canvas.create_text(
            self.screen_w * 0.675,
            self.screen_h * 0.40,
            text="Windows 7-inspired interface",
            fill="#375c8f",
            font=("Segoe UI", 16),
        )

        # taskbar
        taskbar_y = self.screen_h - 50
        self.canvas.create_rectangle(0, taskbar_y, self.screen_w, self.screen_h, fill="#d8d8d8", outline="")

        # start button
        start_x = 10
        start_y = taskbar_y + 6
        self.canvas.create_rectangle(start_x, start_y, start_x + 108, start_y + 38, fill="#3eaa46", outline="#2f7c35")
        self.canvas.create_text(start_x + 54, start_y + 19, text="Start", fill="white", font=("Segoe UI", 10, "bold"))

        # quick launch placeholders
        for i in range(5):
            x = 150 + i * 74
            self.canvas.create_rectangle(x, taskbar_y + 6, x + 60, taskbar_y + 40, fill="#c7d6ef", outline="#a8bbdc")

        # system tray and clock
        self.clock_text = self.canvas.create_text(self.screen_w - 90, taskbar_y + 24, text="9:41 PM", fill="#1d1d1d", font=("Segoe UI", 10, "bold"))

        # start menu overlay (hidden by default)
        self.start_menu = self.canvas.create_rectangle(
            10,
            taskbar_y - 180,
            260,
            taskbar_y - 10,
            fill="#efefef",
            outline="#b3b3b3",
            width=2,
            state="hidden",
        )
        self.canvas.create_text(35, taskbar_y - 150, text="Programs", anchor="w", fill="#1f1f1f", font=("Segoe UI", 10, "bold"), state="hidden", tags="menu_text")
        self.canvas.create_text(35, taskbar_y - 125, text="Documents", anchor="w", fill="#1f1f1f", font=("Segoe UI", 10), state="hidden", tags="menu_text")
        self.canvas.create_text(35, taskbar_y - 105, text="Pictures", anchor="w", fill="#1f1f1f", font=("Segoe UI", 10), state="hidden", tags="menu_text")
        self.canvas.create_text(35, taskbar_y - 85, text="Computer", anchor="w", fill="#1f1f1f", font=("Segoe UI", 10), state="hidden", tags="menu_text")

        self.canvas.tag_bind("start_button", "<Button-1>", self.toggle_start_menu)

        # Clickable start region implemented via canvas rectangle
        self.start_button_id = self.canvas.create_rectangle(start_x, start_y, start_x + 108, start_y + 38, fill="", outline="", tags="start_button")

        self.canvas.bind("<Escape>", lambda event: self.destroy())
        self.bind("<F11>", lambda event: self.attributes("-fullscreen", not self.attributes("-fullscreen")))

    def toggle_start_menu(self, event=None):
        menu_items = self.canvas.find_withtag("menu_text")
        if self.start_menu_open:
            self.canvas.itemconfigure(self.start_menu, state="hidden")
            for item in menu_items:
                self.canvas.itemconfigure(item, state="hidden")
            self.start_menu_open = False
        else:
            self.canvas.itemconfigure(self.start_menu, state="normal")
            for item in menu_items:
                self.canvas.itemconfigure(item, state="normal")
            self.start_menu_open = True

    def update_clock(self):
        import time
        current = time.strftime("%I:%M %p")
        self.canvas.itemconfigure(self.clock_text, text=current)
        self.after(1000, self.update_clock)


def generate_output_files(base_dir: str):
    project_dir = os.path.join(base_dir, "generated", "hdmi_windows7_mockup")
    os.makedirs(project_dir, exist_ok=True)

    readme = """# HDMI Windows 7 Mockup

This is a mockup-only desktop inspired by Windows 7, designed for a fullscreen HDMI display.

## Run

```bash
python3 os_maker.py
```

## Notes

This is only a graphic mockup. It does not boot as an operating system.
"""

    desktop_code = """import tkinter as tk\n\nroot = tk.Tk()\nroot.attributes('-fullscreen', True)\nroot.configure(bg='#4f8edc')\n\ncanvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg='#4f8edc', highlightthickness=0)\ncanvas.pack(fill='both', expand=True)\n\ncanvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill='#4f8edc')\ncanvas.create_rectangle(0, root.winfo_screenheight() - 50, root.winfo_screenwidth(), root.winfo_screenheight(), fill='#d8d8d8')\ncanvas.create_rectangle(12, root.winfo_screenheight() - 44, 120, root.winfo_screenheight() - 10, fill='#3eaa46')\ncanvas.create_text(66, root.winfo_screenheight() - 27, text='Start', fill='white', font=('Segoe UI', 10, 'bold'))\ncanvas.create_text(root.winfo_screenwidth() - 90, root.winfo_screenheight() - 27, text='9:41 PM', fill='#1d1d1d', font=('Segoe UI', 10, 'bold'))\n\nroot.mainloop()\n"""

    with open(os.path.join(project_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write(readme)
    with open(os.path.join(project_dir, "desktop.py"), "w", encoding="utf-8") as f:
        f.write(desktop_code)

    message = f"Generated HDMI mockup under: {project_dir}"
    return message


def main():
    project_root = os.getcwd()
    app = HDMIWindows7Mockup()
    app.update_clock()
    app.after(250, lambda: app.focus_force())

    # Keep a simple export action available for project generation.
    msg = generate_output_files(project_root)
    print(msg)

    app.mainloop()


if __name__ == "__main__":
    main()

