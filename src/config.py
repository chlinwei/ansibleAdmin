import os 
from dotenv import load_dotenv
load_dotenv()
ABS_DATA_DIR=os.path.abspath(os.getenv("DATA_DIR"))
config = {
    "PORT": os.getenv("PORT"),
    "DB_URL": f"sqlite:///{ABS_DATA_DIR}/sql_app.db"
}
