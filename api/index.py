# api/index.py
import sys
import os
from mangum import Mangum

# Add the root project to the path so imports work
sys.path.append(os.path.join(os.path.dirname(app/main), "..", "app"))

from main import app  # your FastAPI app

handler = Mangum(app)  # Needed for Vercel serverless
