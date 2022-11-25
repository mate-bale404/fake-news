from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/newsfeed')
def news_feed():
    return render_template('news_feed.html')

@app.route('/aboutus')
def about_us():
    return render_template('about_us.html')

if __name__=='__main__':
    app.run(debug=True)