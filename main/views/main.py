from models.store_manager import StoreManager
from pydantic import BaseModel, constr, ValidationError


# validates credentials for registration
class RegisterationInfo(BaseModel):
    full_name: str
    username: str
    password: constr(min_length=8)
    secret_phrase: constr(max_length=25) # for password reset


# main app (all processes begins here)
def main():
    # dummy data for registration
    # will be removed once we start GUI
    reg_data = {
        "full_name": "Edwin Setsoafia",
        "username": "Eddie",
        "password": "12345678",
        "secret_phrase": "loud silence"
    }


if __name__=="__main__":
    main()
    