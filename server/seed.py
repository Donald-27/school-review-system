from server.models import db, User, School, Review
from server.app import app
with app.app_context():
    print("Seeding database...")

    Review.query.delete()
    User.query.delete()
    School.query.delete()
    user1 = User(name="Alice Mwende", email="alice@example.com", phone="0712345678", password="alicepass")
    user2 = User(name="Brian Otieno", email="brian@example.com", phone="0798765432", password="brianpass")

    db.session.add_all([user1, user2])
    db.session.commit()
    school1 = School(
        name="Meru High School",
        region="Meru",
        model="boarding",
        type="public",
        level="national",
        description="Top performing national school in Meru."
    )
    school2 = School(
        name="Green Valley Academy",
        region="Nairobi",
        model="day",
        type="private",
        level="county",
        description="Modern private school offering STEM."
    )

    db.session.add_all([school1, school2])
    db.session.commit()

    # Create reviews
    review1 = Review(
        review_text="Amazing learning environment and great teachers!",
        user_id=user1.id,
        school_id=school1.id,
        is_standout=True,
        upvotes=5
    )
    review2 = Review(
        review_text="Offers excellent STEM facilities and opportunities.",
        user_id=user2.id,
        school_id=school2.id
    )

    db.session.add_all([review1, review2])
    db.session.commit()

    print("Done seeding!")
