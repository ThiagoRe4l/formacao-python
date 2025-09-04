from datetime import datetime, timezone, timedelta
from flask import Flask, request, jsonify
from database import db
from models.meal import Meal

app = Flask(__name__)
app.config['SECRET_KEY'] = "oriundio"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ate7815@127.0.0.1:3306/desafio-02'

db.init_app(app)

@app.route('/meal', methods=['POST'])
def create_meal():
    data = request.json
    meal = Meal(   
        name = data.get("name"),
        description = data.get("description"),
        date=datetime.strptime(data["date"], "%d/%m/%Y %H:%M") if "date" in data else datetime.now(timezone.utc),
        diet = data.get("diet", False)
    )

    db.session.add(meal)
    db.session.commit()
    return jsonify({"message": "Refeição cadastrada com sucesso"})

@app.route('/meal/<int:id_meal>', methods=['PUT'])
def update_meal(id_meal):
    data = request.json # Recupera oq o usuario enviou
    meal = Meal.query.get(id_meal) # Recupera o usuario pelo ID

    if meal and data.get("name") or data.get("description") or data.get("diet"):
        meal.name = data.get("name")
        meal.description = data.get("description")
        meal.diet = data.get("diet")
        db.session.commit()

        return jsonify({"message": f"Refeição '{meal.name}' atualizada com sucesso."})
    
    return jsonify({"message": f"Refeição não encontrada"}), 404

    
# @app.route('/meal/<str:name_meal>', methods=['DELETE'])
# def delete_meal():

# @app.route('/meal', methods=['GET'])
# def get_meal():

# @app.route('/meal/<str:name_meal>', methods=['GET'])
# def getById_meal():
    

@app.route("/hello-world", methods=['GET'])
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run(debug=True)