import sqlite3



class HabitTrackerDatabase:
    def __init__(self):
        conn = sqlite3.connect('data/habits.db')
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor

    def add_habit(self, habit_name, start_date, target):
        self.cursor.execute("INSERT INTO habits (habit_name, start_date, target) VALUES (?, ?, ?)", (habit_name, start_date, target))
        self.conn.commit()
    def update_habit(self, id, new_name=None, target=None):
        if new_name is not None:
            self.cursor.execute("UPDATE OR IGNORE habits SET habit_name = ? WHERE id = ?", (new_name, id))
        if target is not None:
            self.cursor.execute("UPDATE OR IGNORE habits SET target = ? WHERE id = ?", (target, id))
        self.conn.commit()
    def delete_habit(self, id):
        self.cursor.execute("DELETE FROM habits WHERE id = ?", (id,))
        self.conn.commit()
    def log_progress(self, habit_id, progress_date, status):
        self.cursor.execute("INSERT OR REPLACE INTO progress (habit_id, progress_date, status) VALUES (?, ?, ?)", (habit_id, progress_date, status))
        self.conn.commit()
    def get_habit(self, habit_id):
        pass
    def get_all_habits(self):
        pass
    def close(self):
        self.conn.commit()
        self.conn.close()

habit_tracker = HabitTrackerDatabase()
