import os
from os.path import join, dirname
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv_path = join(BASE_DIR, '.env')
load_dotenv(dotenv_path)

os.environ.setdefault("DEBUG_APP", "False")
os.environ.setdefault("HOST", "0.0.0.0")
os.environ.setdefault("PORT", "80")
os.environ.setdefault("INTERFACE", "wlan1")

DEBUG = os.environ.get("DEBUG_APP")
HOST = os.environ.get("HOST")
PORT = os.environ.get("PORT")
INTERFACE = os.environ.get("INTERFACE")