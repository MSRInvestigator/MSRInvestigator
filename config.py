
import os

FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "devkey")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
