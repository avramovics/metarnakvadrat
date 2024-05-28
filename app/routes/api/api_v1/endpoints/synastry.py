from fastapi import APIRouter, Depends
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select
from .....db.db import get_db
from .....model.model import User,UserList
from .....helper.h_v1.calculations import get_compability


router = APIRouter()


# Get a specific user.
@router.post("/")
async def create_user(users: UserList, db = Depends(get_db)):
        try:
            #user_ids = ["Nelli", "Stefan"]
            user_query = select(User).where(User.user_id.in_(users.users_id))
            #user_query = select(User).where(User.user_id==user_id)
            res = db.execute(user_query).all()
            if res:
            # Return a list of user data
                users = [user[0].__dict__ for user in res]
            if len(users)==2:    
                return await get_compability(users)
            else:
                return {"message": "User not found"}
        except SQLAlchemyError as e:
            # Rollback the transaction in case of an error
            db.rollback()
            return {"error": str(e)}
        finally:
            # Close the database session
            db.close()