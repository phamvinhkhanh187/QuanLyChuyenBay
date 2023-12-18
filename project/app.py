from flask import Flask, render_template

from project import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/passenger')
def passenger():
    return render_template('passenger.html')


@app.route('/seat-selection')
def selectser():
    return render_template('seat-selection.html')




if __name__ == '__main__':
    app.run(debug=True)
