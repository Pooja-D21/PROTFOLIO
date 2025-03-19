from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Print to console (Later, you can store it in a database)
    print(f"New message from {name} ({email}): {message}")
    
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
