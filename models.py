from flask_mysqldb import MySQL

class TaskManager:
    def __init__(self, app):
        try:
            self.mysql = MySQL(app)
        except Exception as e:
            print(f"Error initializing MySQL connection: {e}")

    def add_task(self, task_name):
        try:
            cursor = self.mysql.connection.cursor()
            query = "INSERT INTO tasks (task, status) VALUES (%s, %s)"
            cursor.execute(query, (task_name, "Pending"))
            self.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error adding task: {e}")

    def complete_task(self, task_id):
        try:
            cursor = self.mysql.connection.cursor()
            query = "UPDATE tasks SET status = %s WHERE id = %s"
            cursor.execute(query, ("Completed", task_id))
            self.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error completing task: {e}")

    def delete_completed_task(self, task_id):
        try:
            cursor = self.mysql.connection.cursor()
            query = "DELETE FROM tasks WHERE id = %s AND status = %s"
            cursor.execute(query, (task_id, "Completed"))
            self.mysql.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"Error deleting completed task: {e}")

    def get_pending_tasks(self):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT id, task FROM tasks WHERE status = %s", ("Pending",))
            tasks = cursor.fetchall()
            cursor.close()
            return tasks
        except Exception as e:
            print(f"Error fetching pending tasks: {e}")
            return []

    def get_completed_tasks(self):
        try:
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT id, task FROM tasks WHERE status = %s", ("Completed",))
            tasks = cursor.fetchall()
            cursor.close()
            return tasks
        except Exception as e:
            print(f"Error fetching completed tasks: {e}")
            return []
