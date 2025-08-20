import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

class Data:

    LOGIN = os.getenv("LOGIN")
    PASSWORD = os.getenv("PASSWORD")