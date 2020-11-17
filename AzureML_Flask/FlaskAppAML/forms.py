from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    RegionID = StringField('RegionID', [validators.Length(min=1, max=6)])
    Stock_Market = StringField('Stock_Market', [validators.Length(min=1, max=6)])
    Mortgage_Rate = StringField('Mortgage_Rate', [validators.Length(min=1, max=3)])
    Monthly_Supply_Of_Homes = StringField('Monthly_Supply_Of_Homes', [validators.Length(min=1, max=2)])