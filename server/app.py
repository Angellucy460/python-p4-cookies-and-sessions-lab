from app import app, db
from models import Article

with app.app_context():
    db.drop_all()
    db.create_all()

    article1 = Article(
        title="First Article",
        body="This is the body of the first article.",
        author="Admin"
    )
    article2 = Article(
        title="Second Article",
        body="Another article for testing.",
        author="Editor"
    )

    db.session.add_all([article1, article2])
    db.session.commit()
    print("✅ Database seeded with articles")
