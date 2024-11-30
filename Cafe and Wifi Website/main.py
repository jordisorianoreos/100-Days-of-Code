from flask import Flask, render_template, url_for, redirect, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEadsadwafBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

with app.app_context():
    db.create_all()

class CafeForm(FlaskForm):
    name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    map_url = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    img_url = URLField('Cafe Image (URL)', validators=[DataRequired()])
    seats = SelectField(label='Number of seats',
                        choices=[("0-10", "0-10"), ("20-30", "20-30"), ("30-40", "30-40"),
                                 ("40-50", "40-50"), ("50+", "50+")], validators=[DataRequired()])
    coffee_price = StringField('Coffee Price, e.g. £2.5', validators=[DataRequired()])
    sockets = BooleanField('Cafe has sockets')
    toilet = BooleanField('Cafe has toilet')
    wifi = BooleanField('Cafe has WiFi')
    calls = BooleanField('Cafe allows calls')
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = request.form.get("name")
        existing_cafe = db.session.execute(db.select(Cafe).filter_by(name=cafe_name)).scalar()
        if existing_cafe:
            return jsonify(error={"Conflict": "A cafe with this name already exists."}), 409

        new_cafe = Cafe(
            name=cafe_name,
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=1 if request.form.get("sockets") == 'y' else 0,
            has_toilet=1 if request.form.get("toilet") == 'y' else 0,
            has_wifi=1 if request.form.get("wifi") == 'y' else 0,
            can_take_calls=1 if request.form.get("calls") == 'y' else 0,
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})

    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    result = db.session.execute(db.select(Cafe))
    list_of_cafes = result.scalars().all()

    unique_locations = sorted(set(cafe.location for cafe in list_of_cafes))
    unique_seats = sorted(set(cafe.seats for cafe in list_of_cafes))

    return render_template('cafes.html', cafes=list_of_cafes,
                           unique_locations=unique_locations,
                           unique_seats=unique_seats)


if __name__ == '__main__':
    app.run(debug=True)
