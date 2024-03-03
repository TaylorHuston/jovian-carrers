from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Software Engineer',
        'location': 'San Francisco, CA',
        'salary': '$100,000 - $150,000',
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'salary': '$120,000 - $180,000',
    },
    {
        'id': 3,
        'title': 'Product Manager',
        'location': 'Seattle, WA',
        'salary': '$130,000 - $200,000',
    },
    {
        'id': 4,
        'title': 'DevOps Engineer',
        'location': 'Austin, TX',
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                           company_name='Jovian')

# If ran from the command line with python3 app.py
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)