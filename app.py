from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Define data_store in the global scope
data_store = {
    'example_id': {
        'name': 'Example Name',
        'value': 42
    }
}

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    value = IntegerField('Value', validators=[DataRequired(), NumberRange(min=1, max=100)])
    submit = SubmitField('Submit')

# Routes for handling form submissions
@app.route('/add_data', methods=['POST'])
def add_data():
    # Access data_store from the global scope
    global data_store

    form = MyForm()
    if form.validate_on_submit():
        new_id = len(data_store) + 1
        data_store[new_id] = {'name': form.name.data, 'value': form.value.data}
        return f'Data submitted successfully! New ID: {new_id}'
    return 'Form validation failed. Please check your inputs.'

# New route for the root URL
@app.route('/')
def home():
    return render_template('form_template.html', form=MyForm())

if __name__ == '__main__':
    app.run(debug=True)
