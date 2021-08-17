from flask import Flask, redirect, url_for, render_template, flash
from forms import ContactForm 

app = Flask(__name__)

app.config['SECRET_KEY'] = b'klHy8(h27)Hjh&*&*o@8&*'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    
    form = ContactForm()

    if form.validate_on_submit():
        flash("Message Sent Successfully", "success")
        return redirect('home')

    return render_template('home.html', form=form)


@app.route("/expert")
def expert():
    return render_template('expertise.html')


if __name__ == '__main__':
    app.run()
