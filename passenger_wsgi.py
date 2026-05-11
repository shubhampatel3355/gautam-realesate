import sys
import os

# Set up the path to your FastAPI app
sys.path.insert(0, os.path.dirname(__file__))

# Import your FastAPI app instance
from main import app as application

# Passenger expects 'application' to be the entry point
