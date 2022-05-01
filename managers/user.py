from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user import ComplainerModel, ApproverModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = ComplainerModel(**user_data)  # razvirihirame data-ta tuka
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            raise BadRequest("Please login")
        return user

    @staticmethod
    def login(user_data):
        user = ComplainerModel.query.filter_by(
            email=user_data["email"]
        ).first()  # checks whether we've got the user with this email
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(
            user.password, user_data["password"]
        ):  # checks if the password is same
            raise BadRequest("Wrong email or password")

        return user
