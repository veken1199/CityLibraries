from database import db

# reset the db
def reset_db():

    # Deleting up the databasae
    print("Deleting the database...")
    db.reflect()
    db.drop_all()

    # Creating all tables for the models
    print("Creating database models...")
    db.create_all()

if __name__ == '__main__':
    reset_db()