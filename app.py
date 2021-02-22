"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from forms import CupcakeAddForm
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "yummy-yummy-cupcakes"

connect_db(app)

@app.route('/')
def show_webpage():
    """Shows the webpage"""
    form = CupcakeAddForm()
    return render_template('index.html', form=form)
    
# *****************************
# RESTFUL TODOS JSON API
# *****************************
@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Returns JSON with all cupcakes"""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:id>')
def get_single_cupcake(id):
    """Returns JSON with single cupcake info"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a new cupcake and add to database"""
    (flavor, size, rating) = (request.json['flavor'], request.json['size'], request.json['rating'])
    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating)
    if request.json.get('image', None):
        new_cupcake.image=request.json['image']
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)

@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Updates a particular cupcake and responds w/ JSON of that updated cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    for field in ('flavor', 'size', 'rating', 'image'):
        if request.json.get(field, None):
            setattr(cupcake, field, request.json[field])
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Deletes identified cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")