import pyautogui as pg
import random as r
import time as t
import sys

# import function to minimize windows on start
import minimize_windows as mw

# --- Setttings ---
SPEED_PX_PER_STEP = 140
TICK_SEC = 0.001
MARGIN = 5
TOLERANCE = 3

pg.FAILSAFE = False


def main():
    screen_w, screen_h = pg.size()

    # random start point
    x = r.randint(MARGIN, screen_w - MARGIN)
    y = r.randint(MARGIN, screen_h - MARGIN)

    # random vector
    dx = r.choice([-1, 1]) * SPEED_PX_PER_STEP
    dy = r.choice([-1, 1]) * SPEED_PX_PER_STEP

    # Close all windows to look  beautifull wallpaper
    mw.minimize_all_windows_cross_platform(prefer="show_desktop")

    # Go to start position
    pg.moveTo(x, y)

    try:
        while True:
            # new koordinates everything
            nx = x + dx
            ny = y + dy

            # Reflections from walls
            if nx <= MARGIN:
                nx = MARGIN
                dx = -dx

            elif nx >= screen_w - MARGIN:
                nx = screen_w - MARGIN
                dx = -dx

            if ny <= MARGIN:
                ny = MARGIN
                dy = -dy

            elif ny >= screen_h - MARGIN:
                ny = screen_h - MARGIN
                dy = -dy

            # Go to new position
            pg.moveTo(nx, ny, duration=0)
            t.sleep(TICK_SEC)

            # Check mouse don't given
            cx, cy = pg.position()
            if abs(cx - nx) > TOLERANCE or abs(cy - ny) > TOLERANCE:
                print("Mouse usebale. Exit...")
                break

            x, y = nx, ny
    except KeyboardInterrupt:
        print("\nStopped on keyboard.")
    except Exception as e:
        print(f"\n Error: {e}")
    finally:
        sys.exit(0)


if __name__ == "__main__":
    main()
