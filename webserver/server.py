from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Message, Mail


mail = Mail()
app = Flask(__name__)

app.secret_key = "aVd2dgs@34vdgad3has"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'shieldsresumewebsite@gmail.com'
app.config['MAIL_PASSWORD'] = 'resumeWebsite'

mail.init_app(app)




@app.route('/')
def home():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/resume.html')
def resume():
    return render_template('resume.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    FlaskForm = ContactForm()

    if request.method == 'POST':
        if FlaskForm.validate() == False:
            flash('All fields are required')
            return render_template('contact.html', form=FlaskForm)
        else:
            msg = Message(FlaskForm.subject.data,
                          sender='shieldsresumewebsite@gmail.com',
                          recipients=['jamesshields.96@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (FlaskForm.name.data, FlaskForm.email.data,
                   FlaskForm.message.data)

            mail.send(msg)

            flash(
                'Thank you for messaging me, I will get back to you as soon as possible!'
            )
            return render_template('contact.html', form=FlaskForm)

    elif request.method == 'GET':
        return render_template('contact.html', form=FlaskForm)

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/work/onePieceWork.html')
def worksOP():
    return render_template('work/onePieceWork.html')

@app.route('/work/hatchetWork.html')
def worksHatchet():
    return render_template('work/hatchetWork.html')

@app.route('/work/OBVpredictWork.html')
def worksOBV():
    return render_template('work/OBVpredictWork.html')

@app.route('/work/howAngryWork.html')
def workTwitBot():
    return render_template('work/howAngryWork.html')