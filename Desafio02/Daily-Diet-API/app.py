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
    
@app.route('/meal/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": f"Refeição '{meal.name}' deletada com sucesso."})
    
    return jsonify({"message": f"Refeição não encontrada."}), 404

@app.route('/meal', methods=['GET'])
def getAll_meal():
    meals = Meal.query.order_by(Meal.date.desc()).all()

    if meals:
        meals_list = [{"id": m.id, "name": m.name, "date": m.date} for m in meals]
        return  jsonify(meals_list)
    
    return jsonify({"message": "Nenhuma refeição encontrada."}), 200

@app.route('/meal/<int:id_meal>', methods=['GET'])
def getById_meal(id_meal):
    meal = Meal.query.get(id_meal)

    if meal:
        meal_dict = {
            "id": meal.id, 
            "name": meal.name, 
            "date": meal.date,
        }
        return jsonify(meal_dict)
    
    return jsonify({"message": f"Refeição não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)