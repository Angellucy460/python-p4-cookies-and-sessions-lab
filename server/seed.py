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

    db.session.add(article1)
    db.session.commit()
    print("Database seeded!")
