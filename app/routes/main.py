from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app.models import User, Todo
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

main_bp = Blueprint('main', __name__)

# Home / Index
@main_bp.route('/')
def index():
    todos = current_user.todos if current_user.is_authenticated else []
    edit_id = request.args.get('edit_id', type=int)
    return render_template('index.html', todos=todos, edit_id=edit_id)

# Register route
@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check password match
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('main.register'))

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "danger")
            return redirect(url_for('main.register'))

        # Create new user
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            is_admin=True if 'is_admin' in request.form else False
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful! Please login.", "success")
        return redirect(url_for('main.login'))
    return render_template('register.html')

# Login route
@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f"Welcome {user.username}!", "success")
            return redirect(url_for('main.index'))
        else:
            flash("Invalid email or password!", "danger")
            return redirect(url_for('main.login'))

    return render_template('login.html')

# Logout route
@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('main.index'))

# Add new todo
@main_bp.route('/add_todo', methods=['POST'])
@login_required
def add_todo():
    title = request.form.get('title')
    if title:
        new_todo = Todo(title=title, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('main.index'))

# Toggle todo completed status
@main_bp.route('/toggle_todo/<int:todo_id>')
@login_required
def toggle_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        abort(403)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('main.index'))

# Delete todo
@main_bp.route('/delete_todo/<int:todo_id>')
@login_required
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        abort(403)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/edit_todo/<int:todo_id>', methods=['POST'])
@login_required
def edit_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if todo.user_id != current_user.id:
        abort(403)
    new_title = request.form.get('title')
    if new_title:
        todo.title = new_title
        db.session.commit()
        flash("Todo updated successfully!", "success")
    return redirect(url_for('main.index'))