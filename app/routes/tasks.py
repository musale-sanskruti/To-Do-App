from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models import Task 

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        flash('Please log in to view tasks.', 'warning')
        return redirect(url_for('auth.login'))

    tasks = Task.query.all() #Fetch all tasks from the database
    return render_template('tasks.html', tasks=tasks)

@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        flash('Please log in to add tasks.', 'warning')
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title: #check if title is not empty
        new_task = Task(title=title) 
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty', 'warning')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id):
    if 'user' not in session:
        flash('Please log in to update tasks.', 'warning')
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Completed'
        else:
            task.status == 'Pending'
        db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 'user' not in session:
        flash('Please log in to delete tasks,', 'warning')
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Task deleted successfully!', 'success')
        return redirect(url_for('tasks.view_tasks'))
            
    
    
    