# server/routes/reviews.py

from flask import Blueprint, request, jsonify
from models import db, Review, School, User
from datetime import datetime

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@reviews_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200
@reviews_bp.route('/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict()), 200

@reviews_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    try:
        new_review = Review(
            user_id=data['user_id'],
            school_id=data['school_id'],
            review=data['review'],
            is_standout=data.get('is_standout', False),
            upvotes=data.get('upvotes', 0),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@reviews_bp.route('/<int:id>', methods=['PATCH'])
def update_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data = request.get_json()
    for field in ['review', 'is_standout', 'upvotes']:
        if field in data:
            setattr(review, field, data[field])
    review.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify(review.to_dict()), 202

@reviews_bp.route('/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    db.session.delete(review)
    db.session.commit()
    return '', 204
