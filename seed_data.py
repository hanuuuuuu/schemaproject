import sys
import os

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from models import db, User, Transaction
from main import app

with app.app_context():
    # Add some users
    user1 = User(name="Alice", credit_score=750)
    user2 = User(name="Bob", credit_score=680)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Add some transactions
    transaction1 = Transaction(user_id=user1.id, amount=150.00, date="2024-11-01")
    transaction2 = Transaction(user_id=user2.id, amount=200.00, date="2024-11-02")
    db.session.add(transaction1)
    db.session.add(transaction2)
    db.session.commit()

    print("Data seeded successfully!")