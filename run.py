#!/usr/bin/python
from app import app

if __name__ == '__main__':
    app.run(host=app.config["HOST"],
            port=int(app.config["PORT"]))
