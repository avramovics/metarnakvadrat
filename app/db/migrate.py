'''
To migrate run command docker exec -it <container name> bash 
then run command python3 ./app/db/migrate.py
'''

import os
import sys

# Add the parent directory of 'app' to the sys.path
#!!Dont touch prekidach! the order it must keep! 
current_dir = os.path.dirname(__file__)
app_parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, '../../app'))
sys.path.append(app_parent_dir)
#!!Dont touch prekidach! the order it must keep! 

from sqlalchemy import create_engine, Column, Integer, String,  text, inspect    


from app.model.model import sqlalchemy_models
from app.db.db import engine






for models in sqlalchemy_models:

     # Query to check if the table exists
    table_exists = inspect(engine).has_table(models.__tablename__)

    # Check if the table exists
    if table_exists:
        print(f"The {models.__table__} table exists.")
    else:
        models.__table__.create(engine)
        print(f"Created table: {models.__table__}")