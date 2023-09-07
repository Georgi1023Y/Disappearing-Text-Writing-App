# Imports needed libraries
import tkinter as tk


# Creates Application class that will contain all functions and GUI interface of the app.
class Application:
    def __init__(self, window):
        self.window = window
        self.window.title("Disappearing Text Writing App")

        self.text_widget = tk.Text(window, wrap=tk.WORD)
        self.text_widget.pack(fill=tk.BOTH, expand=True)

        self.timer_label = tk.Label(window, text="Time left: 10 seconds")
        self.timer_label.pack()

        # This button will start the timer. When user clicks it, start_timer function will be triggered.
        self.start_button = tk.Button(window, text="Start", command=self.start)
        self.start_button.pack()

        self.timer_running = False
        self.countdown_duration = 10

        # Creates a variable to store the last text length. At the beginning it is 0.
        self.last_text_length = 0

    # Function that will get triggered if Start button is pressed.
    def start(self):
        # Sets timer_running boolean variable to True.
        self.timer_running = True
        # Makes sure that the button can't be clicked many times at once.
        self.start_button.config(state=tk.DISABLED)
        # Deletes the old text.
        self.text_widget.delete(1.0, tk.END)
        self.countdown()

    def countdown(self):
        if self.timer_running:
            self.timer_label.config(text=f"Time left: {self.countdown_duration} seconds")
            if self.countdown_duration == 0:
                self.text_widget.delete(1.0, tk.END)
                self.timer_label.config(text="Time's up!")
                self.start_button.config(state=tk.NORMAL)
                return
            # If countdown is not 0 it decreases countdown by 1.
            self.countdown_duration -= 1
            self.window.after(1000, self.countdown)  # Calls countdown after 1000 milliseconds or 1 second.

            # Checks if the user has started typing.
            # Checks the current_length.
            current_text_length = len(self.text_widget.get("1.0", tk.END))
            # If the current_length is greater than last_text_length, which is set to 0, reset_count function is triggered.
            if current_text_length > self.last_text_length:
                self.reset_count()
            self.last_text_length = current_text_length

    # Function that resets the countdown if user starts writing.
    def reset_count(self):
        self.countdown_duration = 10
        self.timer_label.config(text=f"Time left: {self.countdown_duration} seconds")


# Starts the desktop application.
if __name__ == "__main__":
    # Creates a window for the app.
    root = tk.Tk()
    # Creates object called app.
    app = Application(root)
    # Mainloop of the app.
    root.mainloop()
