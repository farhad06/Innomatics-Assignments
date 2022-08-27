from flask import Flask, render_template, request,url_for

app = Flask(__name__)

notes = []
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST' and request.form['note'] != '':
        note = request.form['note']
        notes.append(note)
        #print(notes)
    return render_template("home.html", notes=notes)


if __name__ == '__main__':
    app.run(debug=True)