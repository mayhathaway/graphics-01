from display import *

def draw_line( x0, y0, x1, y1, screen, color ):

    if x1 < x0:
        x0copy = x0
        x0 = x1
        x1 = x0copy
        y0copy = y0
        y0 = y1
        y1 = y0copy

    x = int(x0)
    y = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    dx = x1 - x
    dy = y1 - y

    A = dy
    B = -1 * dx

    # horizontal line
    if (dx == 0):
        while (y <= y1):
            plot(screen, color, x, y)
            y += 1

    # vertical line
    elif (dy == 0):
        while (x <= x1):
            plot(screen, color, x, y)
            x += 1

    # octants 1 and 5
    elif ((A / B) >= -1 and (A / B) < 0):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    # octants 2 and 6
    elif ((A / B) < -1):
        d = 2 * B + A
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    # octants 3 and 7
    elif ((A / B) > 1):
        d = 2 * B - A
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    # octants 4 and 8
    else:
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
