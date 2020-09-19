from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

# Route for main entry point
@app.route('/')
def hello_world():

    # init the parameters
    title="My Flask Website"
    name='Main body of the Website'

    # make the return call
    # render the html and pass the parameters
    return render_template('test.html', siteTitle=title, bodyContent=name)


# Another route for Ajax functionality example
@app.route('/data')
def data():
    # This is python dictionary
    my_data = {
        'title': "Roby",
        'names': ['one', 'two', 'three']
    }
    # To return this to calling page, we need to Jasonify this data
    # so, import Jsonify at the top...
    return jsonify(my_data)


    # Return simple text to show that ajax send data from server..
    # Page can request data that can be partial/chuck of data/info
    #return 'test'