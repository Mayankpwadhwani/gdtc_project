
from core.database import collectionusers
from Auth.login import get_password_hash
from models.users import UserCreate


def get_user_by_email(email: str):
    return collectionusers.find_one({"email": email})

def create_user(user: UserCreate, role="user"):
    user_dict = user.dict()
    user_dict["password"] = get_password_hash(user.password)
    user_dict["role"] = role
    collectionusers.insert_one(user_dict)
    return user_dict

