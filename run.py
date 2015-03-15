from example import Example

def run_app(app):
    app.run(debug=True, port=5000)

def run_celery(app):
    app.celery
