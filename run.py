print("Hello World")

import sys
import os
from dotenv import load_dotenv
from src.app import App

def resources_path(relative_path):
    try:
        path = sys._MEIPASS
    except:
        path = os.path.abspath(os.path.dirname(__file__))

    return os.path.join(path,relative_path)

load_dotenv()

name_app = os.getenv("APP_NAME")
description = os.getenv("DESCRIPTION")
version = os.getenv("VERSION")


print(f"{name_app}\n")
print(f"Review: {description}\n")
print(f"Version : {version}\n")

app = App(name_app)
app.run()