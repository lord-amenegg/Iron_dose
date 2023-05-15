from flask import Flask, render_template, request, url_for
from helper_2 import IronDoseCalculator
app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')


@app.route('/calculator', methods=['GET', 'POST'])
def bmi_calculator():
    # set the initial values to 0
    bmi = 0
    ibw = 0
    height = 0
    weight = 0
    hb = 0
    sex= 'Fluid'
    iron_dose = 0
    try:

        if request.method == 'POST':
            #try:
            weight = request.form.get('weight', type=float)
            height = (request.form.get('height', type=float))/100
            hb = request.form.get('Hb', type=int)
            sex = request.form['sex']

        # calculate the BMI
            if sex == 'Male':
                bmi = round((weight / (height ** 2)),2)
                ibw =  round((50 + 0.91 * ((height*100) - 152)), 2) 
                if bmi > 30:
                    iron_dose = round(min(ibw*20,IronDoseCalculator.ganzoni(hb, ibw)), -2)
                else:
                    iron_dose = round(min(weight*20,IronDoseCalculator.ganzoni(hb, weight)), -2)

            else:
                bmi = round((weight / (height ** 2)),2)
                ibw =  round((45 + 0.91 * ((height*100) - 152)), 2)
                if bmi > 30:
                    iron_dose = round(min(ibw*20,IronDoseCalculator.ganzoni(hb, ibw)), -2)
                else:
                    iron_dose = round(min(weight*20,IronDoseCalculator.ganzoni(hb, weight)), -2)


        return render_template("calculator.html", bmi=bmi, ibw=(str(ibw)+'kg'), iron_dose = (str(iron_dose)+'mg'), height = height, weight=weight, hb=hb)
    except TypeError:
        return render_template("error.html", bmi=bmi, ibw=(str(ibw)+'kg'), iron_dose = iron_dose, height = height, weight=weight, hb=hb)


if __name__ == '__main__':
    app.run(debug=True)