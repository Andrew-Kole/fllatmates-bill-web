from flask.views import MethodView
from wtforms import Form
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
    """Represents the main page of my app."""

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    """Represents the form for bill data filling."""

    def get(self):
        return "I am a bill form page!"


class ResultPage(MethodView):
    """Represents a page with results of app work."""

    pass


class BillForm(Form):
    pass


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
