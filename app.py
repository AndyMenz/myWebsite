from flask import Flask, render_template,request,redirect,url_for
from forms import loginForm,registerForm,shopForm

app= Flask(__name__)

app.config['SECRET_KEY']='abcd'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form=loginForm()
    # username= request.form['username']
    # password= request.form['password']
    username = form.username.data
    password = form.password.data
    if request.method=='POST' and username =='andy' and password=='123':
        
        return redirect(url_for('index'))
    else:
        return render_template('login.html',form=form)  
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        pass
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/shop',methods=['GET','POST'])
def shop():
    form=shopForm()
    return render_template('shop.html',form=form)

@app.route('/about')
def about():
    return render_template('about.html')




if __name__=='__main__':
    app.run(debug=True)