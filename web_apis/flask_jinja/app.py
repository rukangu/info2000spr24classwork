from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# adds new student to database
@app.route('/add/')
def add_student():
    return render_template('add_user.html')


#views all students
@app.route('/view', methods = ['POST', 'GET'])
def view_students():
    first_name = request.form.get('first_name') # get data from form based on the names of the elements
    last_name = request.form.get('surname')
    level = request.form.get('level')
    color = request.form.get('favorite_color')

    context = {'my_first_name':first_name, 'my_last_name': last_name, 'my_level': level, 'my_color':color}


    return render_template('view_user.html', **context)

# @app.route('/greet')
# def greet():
#     return "Hello INFO2000"

if __name__ == "__main__":
    app.run(debug = True)