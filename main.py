from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
    """Represents the main page of my app."""

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):
    """Represents the form for bill data filling."""

    def get(self):
        bill_form = BillForm()
        return render_template('bill_form_page.html', bill_form=bill_form)


class ResultPage(MethodView):
    """Represents a page with results of app work."""

    pass


class BillForm(Form):
    """The submitting form used by BillFormPage and bill_form_page for jinjas"""
    # General info about a bill
    amount = StringField(label="Bill Amount: ")
    period = StringField(label="Bill Period: ")
    # Info about first flatmate
    name1 = StringField(label="Name: ")
    days_in_house1 = StringField(label="Days in the house: ")
    # Info about second flatmate
    name2 = StringField(label="Name: ")
    days_in_house2 = StringField(label="Days in the house: ")

    submit_button = SubmitField("Calculate")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))

app.run(debug=True)
