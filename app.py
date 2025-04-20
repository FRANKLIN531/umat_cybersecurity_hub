from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'frankinyeboah@gmail.com'  # Your Gmail address
app.config['MAIL_PASSWORD'] = 'NoT16@FRANKLIN'        # Replace with your App Password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/submit_report', methods=['GET', 'POST'])
def submit_report():
    if request.method == 'POST':
        title = request.form['reportTitle']
        description = request.form['reportDescription']
        country = request.form['reportCountry']
        report_link = request.form['reportSource']

        # Compose the email
        msg = Message(subject=f"New Security Report: {title}",
                      sender=app.config['MAIL_USERNAME'],
                      recipients=['frankinyeboah@gmail.com'])  # Recipient's email
        msg.body = f"""
        Title: {title}
        Description: {description}
        Country: {country}
        Link: {report_link}
        """

        try:
            mail.send(msg)
            return redirect(url_for('submit_report'))
        except Exception as e:
            return f"An error occurred while sending the email: {e}"
    return render_template('submit_report.html')

if __name__ == '__main__':
    app.run(debug=True)
