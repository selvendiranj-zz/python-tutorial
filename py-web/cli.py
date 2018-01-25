"""
Usage:   weppy --app=py-web <command>
Example: weppy --app=py-web shell
"""
from py-web import app


@app.cli.command('routes')
def print_routing():
    print(app.route.routes_out)


@app.cli.command('get_users')
def print_users():
    from py-web import db
    from py-web.models.user import User
    rows = db(User.email).select()
    for row in rows:
        print(row)
