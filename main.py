from app import app, db
from models import Ticket  # Ensure Ticket is imported

# Initialize database and update sample tickets on every reload
with app.app_context():
    db.create_all()  # Ensure tables exist

    # Clear existing tickets and repopulate
    Ticket.query.delete()  # Deletes all existing records
    db.session.commit()  # Commit the deletion before inserting new records

    sample_tickets = [
        Ticket(event_name='Float Fest Pool Party', price=0),
        Ticket(event_name='PMP Certification Training', price=1599),
        Ticket(event_name='Women Art Exhibition 2025', price=0),
        Ticket(event_name='Elante Event', price=13),
        Ticket(event_name='Makeup Artist in Jalandhar', price=0),
        Ticket(event_name='4 Day PMP Training', price=1599),
        Ticket(event_name='Heritage Walk in Kapurthala', price=150),
        Ticket(event_name='Punjabi Poetry Recital', price=100),
        Ticket(event_name='Tractor Rally and Farming Expo', price=50),
        Ticket(event_name='Punjabi Movie Premiere', price=400),
        Ticket(event_name='Sports Tournament', price=300),
    ]

    db.session.bulk_save_objects(sample_tickets)
    db.session.commit()
    
    print("✅ Database refreshed with sample tickets.")

if __name__ == '__main__':
    app.run(debug=True)