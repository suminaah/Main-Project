from flask import*

from public import *

from admin import *



app=Flask(__name__)

app.secret_key='asdfg'

app.register_blueprint(public)
app.register_blueprint(admin)


app.run(debug=True)

