from flask import Flask
app = Flask(__name__)


@app.route('/index', methods=['GET','POST'])
def post_log_workout(): 
    error=""
    if request.method == 'POST':   
        major = (request.form.get['major'])
        if major is not None:       
            db.session.commit() 
            # you can redirect to home page on successful commit. or anywhere else
            return hello world     
        else:
            return hello world

    return render_template("index.html", error=error)


if __name__ == "__main__":
    app.run()