from flask import Flask,render_template 

sikiza = Flask(__name__)  # initialize sikiza


@sikiza.route('/')
def IntroPage():
    return render_template('index.html')



@sikiza.route('/home')
def HomePage():
    return render_template('home.html')





if __name__ == '__main__':
    sikiza.run(debug=True)