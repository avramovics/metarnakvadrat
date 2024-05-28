import os
from dotenv import load_dotenv

# Get the absolute path to your root directory
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# Specify the absolute path to your .env file
env_file = os.path.join(root_dir, '.env')

# Load the .env file using the absolute path
load_dotenv(dotenv_path=env_file)
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')