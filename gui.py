import customtkinter
import customtkinter as ctk


class HabitTrackrGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x650")
        self.title("habitTrackr")
        self.resizable(False, False)



if __name__ == "__main__":
    app = HabitTrackrGUI()
    app.mainloop()