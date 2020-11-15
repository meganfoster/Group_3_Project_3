from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    RegionID = StringField('RegionID', [validators.Length(min=2, max=30)])
    Stock_Market = StringField('Stock_Market', [validators.Length(min=0, max=300)])
    Mortgage_Rate = TextAreaField('Mortgage_Rate', [validators.Length(min=1, max=10)])
    Monthly_Supply_Of_Homes = TextAreaField('Monthly_Supply_Of_Homes', [validators.Length(min=1, max=100)])