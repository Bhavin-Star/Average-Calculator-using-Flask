from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')

@app.route('/form', methods = ["GET","POST"])

def form():
    if request.method == "GET":
        return render_template('form.html')

    else:
        maths = float(request.form['maths'])
        physics = float(request.form['physics'])
        chem = float(request.form['chem']) 

        avg =  (maths+physics+chem)/3
        return render_template('form.html', score = avg)

if __name__ == "__main__":
    app.run(debug=True)