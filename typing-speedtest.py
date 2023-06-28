import tkinter as tk
import time


class TypingTestApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Speed Test")
        self.root.geometry("400x300")

        self.text = tk.StringVar()
        self.user_input = tk.StringVar()
        self.start_time = None

        self.text_label = tk.Label(self.root, textvariable=self.text, font=("Arial", 14))
        self.text_label.pack(pady=20)

        self.input_entry = tk.Entry(self.root, textvariable=self.user_input, font=("Arial", 12))
        self.input_entry.pack(pady=10)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a powerful programming language.",
            "I love using artificial intelligence in my projects."
        ]
        self.current_sentence = 0

    def start_test(self):
        self.start_button.config(state=tk.DISABLED)
        self.user_input.set("")
        self.text.set("Type the following sentence:\n" + self.sentences[self.current_sentence])
        self.start_time = time.time()
        self.root.bind('<Return>', self.check_result)

    def check_result(self, event):
        if self.start_time is None:
            return

        elapsed_time = time.time() - self.start_time
        user_text = self.user_input.get().strip()
        expected_text = self.sentences[self.current_sentence]

        if user_text == expected_text:
            wpm = int(len(user_text) / elapsed_time * 60)
            self.result_label.config(text=f"Congratulations!\nYour typing speed is {wpm} words per minute.", fg="green")
        else:
            self.result_label.config(text="Incorrect input. Try again.", fg="red")

        self.current_sentence += 1
        if self.current_sentence < len(self.sentences):
            self.start_button.config(text="Next Sentence")
            self.start_button.config(state=tk.NORMAL)
        else:
            self.start_button.config(text="Test Completed", state=tk.DISABLED)

        self.root.unbind('<Return>')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    typing_test_app = TypingTestApp()
    typing_test_app.run()
