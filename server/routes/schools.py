from flask import Blueprint, request, jsonify
from models import db, School, SchoolCategory, SchoolModel, SchoolType
schools_bp = Blueprint('schools', __name__, url_prefix='/schools')
@schools_bp.route('/', methods=['GET'])
def get_schools():
    schools = School.query.all()
    return jsonify([school.to_dict() for school in schools]), 200

@schools_bp.route('/<int:id>', methods=['GET'])
def get_school_by_id(id):
    school = School.query.get(id)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    return jsonify(school.to_dict()), 200

@schools_bp.route('/', methods=['POST'])
def create_school():
    data = request.get_json()

    try:
        name = data['name']
        region = data['region']
        description = data.get('description')
        type_id = data['type_id']
        model_id = data['model_id']
        category_id = data['category_id']

        new_school = School(
            name=name,
            region=region,
            description=description,
            type_id=type_id,
            model_id=model_id,
            category_id=category_id
        )
        db.session.add(new_school)
        db.session.commit()

        return jsonify(new_school.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@schools_bp.route('/<int:id>', methods=['PATCH'])
def update_school(id):
    school = School.query.get(id)
    if not school:
        return jsonify({'error': 'School not found'}), 404


    data = request.get_json()
    for field in ['name', 'region', 'description', 'type_id', 'model_id', 'category_id']:
        if field in data:
            setattr(school, field, data[field])
    db.session.commit()
    return jsonify(school.to_dict()), 202

@schools_bp.route('/<int:id>', methods=['DELETE'])
def delete_school(id):
    school = School.query.get(id)
    if not school:
        return jsonify({'error': 'School not found'}), 404
    db.session.delete(school)
    db.session.commit()
    return '', 204
