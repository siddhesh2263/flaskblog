from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Sid Marker',
        'title': 'Only Time',
        'content': 'Time Will Tell',
        'date_posted': '24 Feb'
    },
    {
        'author': 'John',
        'title': 'Enemies',
        'content': 'Time Will Tell All',
        'date_posted': '23 Feb'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)