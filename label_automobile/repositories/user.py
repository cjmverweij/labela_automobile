from label_automobile.models.user import User


class UserRepository:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, id):
        return self.session.query(User).filter(
            User.id == id).one()

    def find_by_email(self, email):
        return self.session.query(User).filter(
            User.email == email).one()