from weppy import response

from py-web import app, auth


@app.route("/")
def welcome():
    response.meta.title = "Py Web"
    return dict()


@app.route('/account(/<str:f>)?(/<str:k>)?')
def account(f, k):
    response.meta.title = "Py Web | Account"
    form = auth(f, k)
    return dict(req=f, form=form)
