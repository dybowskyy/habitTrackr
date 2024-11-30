import sqlite3

class HabitTrackerDatabase():
        def __init__(self):
            conn = sqlite3.connect('data/habits.db')
            cursor = conn.cursor()
            self.conn = conn
            self.cursor = cursor
        def add_habit(self, name, start_date):
            pass
        def update_habit(self, habit_id, new_name):
            pass
        def delete_habit(self, habit_id):
            pass
        def log_progress(self, habit_id, date, status):
            pass
        def get_habit(self, habit_id):
            pass
        def get_all_habits(self):
            pass
        def close(self):
            self.conn.commit()
            self.conn.close()