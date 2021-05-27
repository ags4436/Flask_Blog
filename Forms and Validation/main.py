from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']="047bc6130a56fff4a6ed454a9c4f91bd"

posts=[

    {
     'author':'ags',
     'title':'Blog Post 1',
     'content' : 'First Post Content',
     'date_posted': 'May 27, 2021'
    },
    {
     'author':'james',
     'title':'Blog Post 2',
     'content' : 'second Post Content',
     'date_posted': 'May 15, 2021'
    }   

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!','success') # success is the class name
        return redirect(url_for('home'))

    return render_template('register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data =='password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful!','danger')

    return render_template('login.html',title='login',form=form)

if __name__ =='__main__':
    app.run(debug=True) 