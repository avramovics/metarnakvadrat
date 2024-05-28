from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select,update
from .....db.db import get_db
from .....model.model import UserInsert,UserBase,User

router = APIRouter()

@router.get("/update")
async def update_table(db = Depends(get_db)):
    try:
        
        # Define the update query
        update_query = update(User).where(User.id == 6).values(username='# Stefan vrcin 123')

        # Execute the update query
        result = db.execute(update_query)

        # Commit the transaction to persist the changes
        db.commit()
        # Get the number of rows affected or updated
        rows_affected = result.rowcount

        if rows_affected > 0:
            # Rows were affected, return a success message
            db.commit()  # Commit the transaction
            return {"message": f"{rows_affected} rows updated successfully" }
        else:
            # No rows were affected, return a message
            return {"message": "No rows updated"}
    except SQLAlchemyError as e:
        # Rollback the transaction in case of an error
        db.rollback()
        return {"error": str(e)}
    finally:
        # Close the database session
        db.close()

@router.get("/user/{id}")
async def create_user(id: int, db = Depends(get_db)):
        try:
            
            user_query = select(User).where(User.id==id)
            res = db.execute(user_query).all()
   
            if res:
            # Return a list of user data
                return {"users": [user[0].__dict__ for user in res]}
            else:
                return {"message": "User not found"}
        except SQLAlchemyError as e:
            # Rollback the transaction in case of an error
            db.rollback()
            return {"error": str(e)}
        finally:
            # Close the database session
            db.close()

@router.post("/user")
async def create_user(user: UserBase, db = Depends(get_db)):
        try:
            # Build a query to select a user based on user.id
            db.execute(text("INSERT INTO users (username) values ('Stefan atlas')"))
            user_query = select(User).where(User.id == user.id)
            res = db.execute(user_query).all()
   
            if res:
            # Return a list of user data
                return {"users": [user[0].__dict__ for user in res]}
            else:
                return {"message": "User not found"}
        except SQLAlchemyError as e:
            # Rollback the transaction in case of an error
            db.rollback()
            return {"error": str(e)}
        finally:
            # Close the database session
            db.close()


@router.post("/newuser")
async def create_user(user: UserInsert, db = Depends(get_db)):
        try:
            # Execute an SQL statement to insert a new user into the "users" table
            insert_query = text("INSERT INTO users (user_id) VALUES (:user_id)")
            db.execute(insert_query, {"user_id": user.user_id})

            # Commit the transaction
            db.commit()

         # Return a response indicating the user was successfully inserted
            return {"message": "User inserted successfully"}
        except SQLAlchemyError as e:
            # Rollback the transaction in case of an error
            db.rollback()
            return {"error": str(e)}
        finally:
            # Close the database session
            db.close()