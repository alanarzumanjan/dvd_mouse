# DVD MOUSE

Tiny Python utility: the mouse cursor bounces around the screen like the classic DVD logo.
As soon as you move the mouse yourself, the program exits.
Optional: minimize all windows on start (best-effort across Windows/macOS/Linux)

---

Features

- Diagonal “DVD” movement with edge bounces.

- Auto-exit on real user movement (cursor position mismatch).

- Optional minimize/show desktop on start (cross-platform best-effort).

---

## Dependences:

Need to install python 3.11 and click - `Add To System PATH`

👉 [python version 3.11](https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe)

This Version is which works stably with all libraries and dependencies

**Windows(Powershell):**

```bash
    py -3.11 --version # check version

    py -3.11 -m venv venv # create virtual environment
    .\venv\Scripts\activate # activate virtual environment

    pip install -r requirements.txt # downloading dependences

    python.exe -m pip install --upgrade pip # optional: upgrade pip

```

**macOS/Linux:**

```bash
    python3 --version # check version

    python3 -m venv venv # create virtual environment
    source venv/bin/activate # activate virtual environment

    pip install -r requirements.txt # downloading dependences

    python -m pip install --upgrade pip # optional: upgrade pip

```

`requirements.txt` **(minimal)**:

```bash
pyautogui==0.9.54
```

`tkinter` ships with Python.
Linux: for the “show desktop” action under X11 you may also want `xdotool`:

```bash
sudo apt install xdotool
```

## Run program

```bash
    python dvd_mouse.py
```

The cursor starts bouncing. Touch the mouse yourself — the app quits.
You can also stop it with Ctrl+C in the terminal.

### Close windows

> if you wasn't close all windows after start program everything - "insert '#' after line 30"
