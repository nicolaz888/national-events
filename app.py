from blueprints.user_blueprint import user_blueprint
from config import app, db
from models.user import User
from models.event import Event
from models.campus import Campus
from models.cohort import Cohort
from models.event_type import EventType

app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)
