import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.environ['DATABASE_URL']
GENERIC_API_KEY = os.environ['GENERIC_API_KEY']
