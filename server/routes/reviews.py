from flask import Blueprint, request, jsonify
from server.models import db, Review
from datetime import datetime

reviews_bp = Blueprint('reviews_bp', __name__, url_prefix='/reviews')

@reviews_bp.route('/', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([{
        "id": r.id,
        "review_text": r.review_text,
        "user_id": r.user_id,
        "school_id": r.school_id,
        "is_standout": r.is_standout,
        "upvotes": r.upvotes,
        "created_at": r.created_at,
        "updated_at": r.updated_at
    } for r in reviews]), 200

@reviews_bp.route('/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify({
        "id": review.id,
        "review_text": review.review_text,
        "user_id": review.user_id,
        "school_id": review.school_id,
        "is_standout": review.is_standout,
        "upvotes": review.upvotes,
        "created_at": review.created_at,
        "updated_at": review.updated_at
    }), 200

@reviews_bp.route('/', methods=['POST'])
def create_review():
    data = request.get_json()
    try:
        new_review = Review(
            user_id=data['user_id'],
            school_id=data['school_id'],
            review_text=data['review_text'],
            is_standout=data.get('is_standout', False),
            upvotes=data.get('upvotes', 0),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"id": new_review.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@reviews_bp.route('/<int:id>', methods=['PATCH'])
def update_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    data = request.get_json()
    for field in ['review_text', 'is_standout', 'upvotes']:
        if field in data:
            setattr(review, field, data[field])
    review.updated_at = datetime.utcnow()
    db.session.commit()
    return jsonify({"message": "Review updated"}), 202

@reviews_bp.route('/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    db.session.delete(review)
    db.session.commit()
    return '', 204
