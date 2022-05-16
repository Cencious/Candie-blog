from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField
from wtforms.validators import DataRequired, Email


class BlogForm(FlaskForm):

    title = StringField('Author', validators=[DataRequired()])
    post = TextAreaField('Blog', validators=[DataRequired()])
    submit = SubmitField('Post')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Let us know you better',validators = [DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post')

class Vote(FlaskForm):
    submit = SelectField('Like')
