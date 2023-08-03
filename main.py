from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill import flat

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

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        name1 = bill_form.name1.data
        days_in_house1 = float(bill_form.days_in_house1.data)

        name2 = bill_form.name2.data
        days_in_house2 = float(bill_form.days_in_house2.data)

        the_bill = flat.Bill(amount=amount, period=period)
        flatmate1 = flat.Flatmate(name=name1, days_in_house=days_in_house1)
        flatmate2 = flat.Flatmate(name=name2, days_in_house=days_in_house2)

        return render_template("bill_form_page.html",
                               result=True,
                               bill_form=bill_form,
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(bill=the_bill, flatmate2=flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(bill=the_bill, flatmate2=flatmate1))



class ResultPage(MethodView):
    """Represents a page with results of app work."""

    def post(self):
        bill_form = BillForm(request.form)
        amount = float(bill_form.amount.data)
        period = bill_form.period.data

        name1 = bill_form.name1.data
        days_in_house1 = float(bill_form.days_in_house1.data)

        name2 = bill_form.name2.data
        days_in_house2 = float(bill_form.days_in_house2.data)

        the_bill = flat.Bill(amount=amount, period=period)
        flatmate1 = flat.Flatmate(name=name1, days_in_house=days_in_house1)
        flatmate2 = flat.Flatmate(name=name2, days_in_house=days_in_house2)

        return render_template("results.html",
                               name1=flatmate1.name,
                               amount1=flatmate1.pays(bill=the_bill, flatmate2=flatmate2),
                               name2=flatmate2.name,
                               amount2=flatmate2.pays(bill=the_bill, flatmate2=flatmate1))


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
# app.add_url_rule('/results', view_func=ResultPage.as_view('result_page'))

app.run(debug=True)
