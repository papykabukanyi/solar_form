from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Define the scope and credentials for accessing Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(credentials)
# Open the Google Sheets spreadsheet
sheet = client.open("solarleads").sheet1

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/form.html')
def form():
    return render_template("form.html")
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form
        # Extract form data
        firstname = data['firstname']
        lastname = data['lastname']
        phone = data['phone']
        email = data['email']
        address = data['address']
        message = data['message']
        # Append data to Google Sheets
        sheet.append_row([firstname, lastname, phone, email, address, message])
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)