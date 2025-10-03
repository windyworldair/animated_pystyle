import sys, time, math, signal

class AnimatedGradient:
    def __init__(self, text, colors, speed=2.0, spacing=0.3, fps=20):
        self.text = text
        self.colors = colors
        self.speed = speed
        self.spacing = spacing
        self.frame_delay = 1/fps
        signal.signal(signal.SIGINT, self.cleanup)

    def lerp(self, a, b, t):
        return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

    def gradient(self, t):
        n = len(self.colors) - 1
        idx = int(t * n)
        t_local = (t * n) - idx
        return self.lerp(self.colors[idx], self.colors[min(idx+1, n)], t_local)

    def cleanup(self, sig=None, frame=None):
        print("\033[0m\033[?25h")
        exit()

    def start(self):
        print("\033[?25l", end="")
        try:
            while True:
                line = ""
                now = time.time()
                for i, ch in enumerate(self.text):
                    t = (math.sin(now*self.speed + i*self.spacing) + 1)/2
                    r, g, b = self.gradient(t)
                    line += f"\033[38;2;{r};{g};{b}m{ch}"
                sys.stdout.write("\r" + line)
                sys.stdout.flush()
                time.sleep(self.frame_delay)
        finally:
            self.cleanup()
