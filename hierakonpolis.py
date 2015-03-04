import sqlite3
from flask import Flask
from flask import g
from flask.ext import restful

DATABASE = 'products.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

app = Flask(__name__)
api = restful.Api(app)

products = {}

class Products(restful.Resource):
    def get(self):
        return {'products': 'more products'}

api.add_resource(Products, '/')

if __name__ == "__main__":
    app.run(debug=True)
