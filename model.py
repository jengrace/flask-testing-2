from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    #FIXME: write a function that creates a game and adds it to the database.
    ticket_to_ride = Game(name="Ticket to Ride",
                          description="a cross-country train adventure")

    power_grid = Game(name="Power Grid",
                      description="supply the most cities with power")

    amazing_labyrinth = Game(name="Amazing Labyrinth",
                            description="move around the shifting paths of the Labryinth")

    db.session.add_all([ticket_to_ride, power_grid, amazing_labyrinth])
    db.session.commit()

if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    print "Connected to DB."
