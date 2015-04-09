@app.route('/logworkout', methods=['GET','POST'])
def post_log_workout(): 
    error=""
    if request.method == 'POST':   
        major = (request.form.get['major'])
        if major is not None:       
            workout = Workout(major=major)
            db.session.add(workout)
            db.session.commit() 
            # you can redirect to home page on successful commit. or anywhere else
            return redirect()       
        else:
            error="Error, your log is incomplete! Please check and submit it again!")

    return render_template("index.html", error=error)