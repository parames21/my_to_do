# models.py
from flask_mysqldb import MySQL

class TaskManager:
    def __init__(self, app):
        self.mysql = MySQL(app)

    def add_task(self, task_name):
        cursor = self.mysql.connection.cursor()
        query = "INSERT INTO tasks (task, status) VALUES (%s, %s)"
        cursor.execute(query, (task_name, "Pending"))
        self.mysql.connection.commit()
        cursor.close()

    def complete_task(self, task_id):
        cursor = self.mysql.connection.cursor()
        query = "UPDATE tasks SET status = %s WHERE id = %s"
        cursor.execute(query, ("Completed", task_id))
        self.mysql.connection.commit()
        cursor.close()

    def delete_completed_task(self, task_id):
        cursor = self.mysql.connection.cursor()
        query = "DELETE FROM tasks WHERE id = %s AND status = %s"
        cursor.execute(query, (task_id, "Completed"))
        self.mysql.connection.commit()
        cursor.close()


    def get_pending_tasks(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, task FROM tasks WHERE status = %s", ("Pending",))
        tasks = cursor.fetchall()
        cursor.close()
        return tasks

    def get_completed_tasks(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT id, task FROM tasks WHERE status = %s", ("Completed",))
        tasks = cursor.fetchall()
        cursor.close()
        return tasks
