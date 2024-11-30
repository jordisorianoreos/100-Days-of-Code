from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from forms import TodoForm, RegisterForm, LoginForm
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add-secret-key-here'
bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "all_todos"
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner = relationship("User", back_populates="todos")
    todo_item = db.Column(db.String(250), nullable=False)
    status = db.Column(db.String(250), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    todos = relationship("Todo", back_populates="owner")


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(User).where(User.id == id)).scalar()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.execute(
            db.select(User).where(User.email == email)).scalar()
        if not user:
            flash('This email does not exist. Please try again.', 'error')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.', 'error')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('mytodo'))
    return render_template('login.html', form=form, logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = request.form.get('email')
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!", 'error')
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(name=request.form.get("name"),
                        email=request.form.get("email"),
                        password=hash_and_salted_password,)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('mytodo'))
    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html", logged_in=current_user.is_authenticated)


@app.route("/mytodo", methods=["GET", "POST"])
@login_required
def mytodo():
    todo_form = TodoForm()
    todos = get_all_todos()
    if todo_form.validate_on_submit():
        new_todo = Todo(
            todo_item=request.form.get("todo_item"),
            status=request.form.get("status"),
            owner_id=current_user.id,
            owner=current_user,)

        try:
            db.session.add(new_todo)
            db.session.commit()

            todos = get_all_todos()
            return redirect(url_for('mytodo'))

        except IntegrityError:
            db.session.rollback()
            flash('Todo item already exists.', 'error')
            return redirect(url_for('mytodo'))
    return render_template("todo.html", form=todo_form, todos=todos, current_user=current_user)


def get_all_todos():
    return Todo.query.filter_by(owner_id=current_user.id).all() if current_user.is_authenticated else []


@app.route("/delete/<int:todo_id>", methods=["POST"])
@login_required
def delete_todo(todo_id):
    todo_to_delete = Todo.query.get_or_404(todo_id)
    if todo_to_delete.owner_id != current_user.id:
        return jsonify(success=False), 403

    db.session.delete(todo_to_delete)
    db.session.commit()
    return jsonify(success=True)


@app.route("/edit/<int:todo_id>", methods=["GET", "POST"])
@login_required
def edit_todo(todo_id):
    todo_to_edit = Todo.query.get_or_404(todo_id)
    edit_todo_form = TodoForm(
        todo_item=todo_to_edit.todo_item,
        status=todo_to_edit.status)

    if edit_todo_form.validate_on_submit():
        todo_to_edit.todo_item = edit_todo_form.todo_item.data
        todo_to_edit.status = edit_todo_form.status.data

        db.session.commit()
        return redirect(url_for("mytodo"))
    return render_template("edit_todo.html", form=edit_todo_form,
                           is_edit=True, current_user=current_user)


@app.route("/update_status/<int:todo_id>", methods=["POST"])
@login_required
def update_status(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    new_status = request.json.get('status')
    if new_status in ['To Do', 'Doing', 'Done']:
        todo.status = new_status
        db.session.commit()
        return jsonify(success=True)
    return jsonify(success=False), 400


@app.route("/clear_all", methods=["POST"])
@login_required
def clear_all_todos():
    todos_to_delete = Todo.query.filter_by(owner_id=current_user.id).all()
    for todo in todos_to_delete:
        db.session.delete(todo)
    db.session.commit()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run(debug=True)
