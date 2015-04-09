@app.route('/logworkout', methods=['GET','POST'])
def post_log_workout(): 
    error=""
    if request.method == 'POST':   
        major = (request.form.get['major'])
        if studio is not None:       
            workout = Workout(studio=studio)
            db.session.add(workout)
            db.session.commit() 
            # you can redirect to home page on successful commit. or anywhere else
            return redirect(url_for('index'))       
        else:
            error="Error, your log is incomplete! Please check and submit it again!")

    return render_template("submit_workout.html", error=error)