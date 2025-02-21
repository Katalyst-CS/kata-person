from flask import Blueprint, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from src.infrastructure.db.models.person import Person, db

person_bp = Blueprint("person", __name__)

# Crear una persona
@person_bp.route("/persons", methods=["POST"])
def create_person():
    try:
        data = request.json

        # Validaciones de datos requeridos
        required_fields = ["customer_id", "given_name", "family_name", "gender"]
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' es requerido"}), 400

        person = Person(
            customer_id=data["customer_id"],
            given_name=data["given_name"],
            family_name=data["family_name"],
            additional_name=data.get("additional_name"),
            birth_date=data.get("birth_date"),
            gender=data.get("gender"),
        )
        db.session.add(person)
        db.session.commit()
        return jsonify({"message": "Persona creada", "id": str(person.id)}), 201

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Error al guardar en la base de datos", "details": str(e)}), 500

# Buscar una persona por ID
@person_bp.route("/persons/<uuid:person_id>", methods=["GET"])
def get_person(person_id):
    person = Person.query.get(person_id)
    if not person:
        return jsonify({"error": "Persona no encontrada"}), 404
    return jsonify({
        "id": str(person.id),
        "customer_id": str(person.customer_id),
        "given_name": person.given_name,
        "family_name": person.family_name,
        "additional_name": person.additional_name,
        "birth_date": str(person.birth_date),
        "gender": person.gender
    }), 200

# Modificar datos de una persona por ID
@person_bp.route("/persons/<uuid:person_id>", methods=["PUT"])
def update_person(person_id):
    try:
        person = Person.query.get(person_id)
        if not person:
            return jsonify({"error": "Persona no encontrada"}), 404

        data = request.json
        person.given_name = data.get("given_name", person.given_name)
        person.family_name = data.get("family_name", person.family_name)
        person.additional_name = data.get("additional_name", person.additional_name)
        person.birth_date = data.get("birth_date", person.birth_date)
        person.gender = data.get("gender", person.gender)

        db.session.commit()
        return jsonify({"message": "Persona actualizada"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar en la base de datos", "details": str(e)}), 500

# Modificar datos de una persona por customer_id
@person_bp.route("/persons/customer/<uuid:customer_id>", methods=["PUT"])
def update_person_by_customer(customer_id):
    try:
        person = Person.query.filter_by(customer_id=customer_id).first()
        if not person:
            return jsonify({"error": "Persona no encontrada"}), 404

        data = request.json
        person.given_name = data.get("given_name", person.given_name)
        person.family_name = data.get("family_name", person.family_name)
        person.additional_name = data.get("additional_name", person.additional_name)
        person.birth_date = data.get("birth_date", person.birth_date)
        person.gender = data.get("gender", person.gender)

        db.session.commit()
        return jsonify({"message": "Persona actualizada"}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Error al actualizar en la base de datos", "details": str(e)}), 500

# Buscar una persona por customer_id
@person_bp.route("/persons/customer/<uuid:customer_id>", methods=["GET"])
def get_person_by_customer_id(customer_id):
    person = Person.query.filter_by(customer_id=customer_id).first()
    if not person:
        return jsonify({"error": "Persona no encontrada"}), 404
    return jsonify({
        "id": str(person.id),
        "customer_id": str(person.customer_id),
        "given_name": person.given_name,
        "family_name": person.family_name,
        "additional_name": person.additional_name,
        "birth_date": str(person.birth_date),
        "gender": person.gender
    }), 200

# Listar personas con paginación
@person_bp.route("/persons", methods=["GET"])
def list_persons():
    try:
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=10, type=int)

        persons = Person.query.paginate(page=page, per_page=size, error_out=False)
        persons_list = [{
            "id": str(person.id),
            "customer_id": str(person.customer_id),
            "given_name": person.given_name,
            "family_name": person.family_name,
            "additional_name": person.additional_name,
            "birth_date": str(person.birth_date),
            "gender": person.gender
        } for person in persons.items]

        return jsonify({
            "total": persons.total,
            "page": persons.page,
            "size": persons.per_page,
            "persons": persons_list
        }), 200

    except SQLAlchemyError as e:
        return jsonify({"error": "Error al obtener la lista de personas", "details": str(e)}), 500