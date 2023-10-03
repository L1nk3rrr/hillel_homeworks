from flask import render_template, request

from . import api, get_db

FIELDS_TO_FILTER = ['id', 'first_name', 'last_name']


@api.route("/names/")
def get_names():
    db = get_db()
    unique_names = db.execute("SELECT DISTINCT first_name FROM customers").fetchall()
    return render_template('names.html', names=unique_names, first_name='first_name')


@api.route("/customers/")
def get_customers():
    db = get_db()
    query = "SELECT * FROM customers WHERE 1=1"
    params = []
    for field in FIELDS_TO_FILTER:
        filter_param = request.args.get(field)
        if filter_param is not None:
            query += f" AND {field} = ?"
            params.append(filter_param)
    customers = db.execute(query, params).fetchall()
    return render_template('customers.html', customers=customers)
