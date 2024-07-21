import tkinter as tk
import time


class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = "The quick brown fox jumps over the lazy dog."
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        self.sample_label = tk.Label(self.root, text="Type the following text:", wraplength=400)
        self.sample_label.pack(pady=10)

        self.text_sample = tk.Label(self.root, text=self.sample_text, wraplength=400, font=("Helvetica", 12, "italic"))
        self.text_sample.pack(pady=10)

        self.entry = tk.Entry(self.root, width=60, font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<Return>", self.check_text)

        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 12, "bold"))
        self.result_label.pack(pady=20)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def check_text(self, event):
        end_time = time.time()
        typed_text = self.entry.get()

        if typed_text == self.sample_text:
            elapsed_time = end_time - self.start_time
            wpm = (len(typed_text) / 5) / (elapsed_time / 60)
            self.result_label.config(text=f"Well done! Your typing speed is {wpm:.2f} words per minute.")
        else:
            self.result_label.config(text="Text does not match. Please try again.")

        # Reset timer
        self.start_time = None
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
