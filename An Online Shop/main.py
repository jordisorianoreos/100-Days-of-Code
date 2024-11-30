from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from sqlalchemy import Integer, String, Float, ForeignKey, DateTime
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aojidjifa8998udasi9328jud?23mbq8u¡1!0846512'
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_ecommerce.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Product(Base):
    __tablename__ = 'product'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    image_url: Mapped[str] = mapped_column(String(250), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String(100), nullable=False)


class CartItem(Base):
    __tablename__ = 'cartitem'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customer.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    product: Mapped['Product'] = relationship('Product')
    customer: Mapped['Customer'] = relationship('Customer', back_populates='cart_items')


class Customer(UserMixin, Base):
    __tablename__ = 'customer'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    cart_items: Mapped[List['CartItem']] = relationship('CartItem', back_populates='customer')
    purchases: Mapped[List['Purchase']] = relationship('Purchase', back_populates='customer')


class Purchase(Base):
    __tablename__ = 'purchase'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customer.id'))
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey('product.id'))
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    purchase_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    customer: Mapped['Customer'] = relationship('Customer', back_populates='purchases')
    product: Mapped['Product'] = relationship('Product')


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(Customer, user_id)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
@login_required
def products():
    result = db.session.execute(db.select(Product))
    list_of_products = result.scalars().all()
    return render_template('products.html', products=list_of_products)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def product(product_id):
    product = db.session.get(Product, product_id)
    if product is None:
        return "Product not found", 404

    if request.method == 'POST':
        quantity = request.form.get('quantity', type=int)
        cart_item = CartItem(customer_id=current_user.id, product_id=product.id, quantity=quantity)
        db.session.add(cart_item)
        db.session.commit()

        flash('Product added to cart!', 'success')
        return redirect(url_for('products'))

    return render_template('product.html', product=product)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = db.session.execute(db.select(Customer).where(Customer.email == email)).scalar()
        if not user:
            flash('This email does not exist. Please try again or register to create a new account.', 'error')
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.', 'error')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('products'))
    return render_template('login.html', form=form, logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        email = register_form.email.data
        user = db.session.execute(db.select(Customer).where(Customer.email == email)).scalar()
        if user:
            flash("You've already signed up with that email, log in instead!", 'error')
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            register_form.password.data,
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = Customer(name=register_form.name.data,
                            email=email,
                            password=hash_and_salted_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('products'))
    return render_template("register.html", form=register_form, logged_in=current_user.is_authenticated)


@login_manager.unauthorized_handler
def unauthorized():
    flash('You need to log in first.', 'error')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    customer_products = db.session.execute(
        db.select(CartItem).where(CartItem.customer_id == current_user.id)
    ).scalars().all()

    total_price = 0
    for item in customer_products:
        if item.product:
            total_price += item.quantity * item.product.price

    return render_template('cart.html', customer_products=customer_products, total_price=total_price)


@app.route('/remove-item', methods=['POST'])
@login_required
def remove_item():
    item_id = request.form.get('item_id')
    cart_item = db.session.get(CartItem, item_id)
    if cart_item and cart_item.customer_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()
        return '', 204
    return 'Item not found', 404


@app.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = db.session.execute(
        db.select(CartItem).where(CartItem.customer_id == current_user.id)
    ).scalars().all()

    if not cart_items:
        return "Cart is empty", 400

    for item in cart_items:
        product = db.session.get(Product, item.product_id)
        if product:
            product.stock -= item.quantity
            purchase = Purchase(customer_id=current_user.id, product_id=item.product_id, quantity=item.quantity)
            db.session.add(purchase)
            db.session.delete(item)

    db.session.commit()
    return redirect(url_for('purchases'))


@app.route('/orders', methods=['GET'])
@login_required
def purchases():
    purchases = db.session.execute(
        db.select(Purchase).where(Purchase.customer_id == current_user.id)
    ).scalars().all()

    purchase_summary = {}
    for purchase in purchases:
        product_name = purchase.product.name
        total_price = purchase.quantity * purchase.product.price

        if product_name in purchase_summary:
            purchase_summary[product_name]['quantity'] += purchase.quantity
            purchase_summary[product_name]['total_price'] += total_price
            purchase_summary[product_name]['purchase_date'] = purchase.purchase_date
        else:
            purchase_summary[product_name] = {
                'quantity': purchase.quantity,
                'total_price': total_price,
                'purchase_date': purchase.purchase_date
            }

    return render_template('purchases.html', purchase_summary=purchase_summary)


if __name__ == '__main__':
    app.run(debug=True)
