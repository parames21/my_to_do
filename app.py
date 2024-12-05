# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import TaskManager

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Replace with your MySQL username
app.config['MYSQL_PASSWORD'] = 'parames@123'  # Replace with your MySQL password
app.config['MYSQL_DB'] = 'to_do_app'

# Initialize TaskManager
task_manager = TaskManager(app)

@app.route('/')
def index():
    pending_tasks = task_manager.get_pending_tasks()
    completed_tasks = task_manager.get_completed_tasks()
    return render_template('index.html', pending=pending_tasks, completed=completed_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        task_manager.add_task(task_name)
    return redirect(url_for('index'))

@app.route('/complete_task', methods=['POST'])
def complete_task():
    task_id = request.form.get('task_id')
    if task_id:
        task_manager.complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete_completed_task', methods=['POST'])
def delete_completed_task():
    task_id = request.form.get('task_id')
    if task_id:
        task_manager.delete_completed_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
