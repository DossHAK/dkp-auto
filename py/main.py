from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dkp.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.Text, nullable=False)
    city = db.Column(db.Text, nullable=False)
    fio_pro = db.Column(db.Text, nullable=False)
    date_birth_pro = db.Column(db.Text, nullable=False)
    pasport_pro_s = db.Column(db.Text, nullable=False)
    pasport_pro_n = db.Column(db.Text, nullable=False)
    pasport_pro_kod = db.Column(db.Text, nullable=False)
    pasport_pro_date = db.Column(db.Text, nullable=False)
    pasport_pro_reg = db.Column(db.Text, nullable=False)
    
    fio_po = db.Column(db.Text, nullable=False)
    date_birth_po = db.Column(db.Text, nullable=False)
    pasport_po_s = db.Column(db.Text, nullable=False)
    pasport_po_n = db.Column(db.Text, nullable=False)
    pasport_po_kod = db.Column(db.Text, nullable=False)
    pasport_po_date = db.Column(db.Text, nullable=False)
    pasport_po_reg = db.Column(db.Text, nullable=False)
    
    model = db.Column(db.Text, nullable=False)
    vin = db.Column(db.Text, nullable=False)
    type = db.Column(db.Text, nullable=False)
    year = db.Column(db.Text, nullable=False)
    engine_m = db.Column(db.Text, nullable=False)
    engine_n = db.Column(db.Text, nullable=False)
    frame = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)
    km = db.Column(db.Text, nullable=False)
    color = db.Column(db.Text, nullable=False)

    pts_s = db.Column(db.Text, nullable=False)
    pts_n = db.Column(db.Text, nullable=False)
    pts_date = db.Column(db.Text, nullable=False)
    pts_reg = db.Column(db.Text, nullable=False)
    
    sts_s = db.Column(db.Text, nullable=False)
    sts_n = db.Column(db.Text, nullable=False)
    sts_date = db.Column(db.Text, nullable=False)
    sts_reg = db.Column(db.Text, nullable=False)
    
    number = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.title

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    items = Item.query.order_by(Item.price).all()
    return render_template('index.html', data=items)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        price = request.form['price']
        text = request.form['text']

        item = Item(title=title, price=price, text=text)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except:
            return 'Произошла ошибка при добавлении товара'
    else:
        return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
