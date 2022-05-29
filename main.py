from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from config import DevApplication
from db import db
from resources.routes import routes
from flask_cors import CORS

app=Flask(__name__)

app.config.from_object(DevApplication)
db.init_app(app)
api=Api(app)
migrate=Migrate(app, db)
CORS(app)
[api.add_resource(*r) for r in routes]

if __name__=="__main__":
    app.run()

