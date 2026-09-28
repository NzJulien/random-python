"""Render the Mandelbrot set as ASCII art in the terminal."""
import sys

PALETTE = " .:-=+*#%@"


def escape_time(c: complex, max_iter: int) -> int:
    z = 0j
    for i in range(max_iter):
        z = z * z + c
        if abs(z) > 2:
            return i
    return max_iter


def render(width: int = 78, height: int = 30, max_iter: int = 60) -> str:
    rows = []
    for y in range(height):
        im = 1.2 - 2.4 * y / (height - 1)
        row = ""
        for x in range(width):
            re = -2.2 + 3.2 * x / (width - 1)
            t = escape_time(complex(re, im), max_iter)
            row += PALETTE[-1] if t == max_iter else PALETTE[t * (len(PALETTE) - 1) // max_iter]
        rows.append(row)
    return "\n".join(rows)


if __name__ == "__main__":
    width = int(sys.argv[1]) if len(sys.argv) > 1 else 78
    print(render(width=width))
