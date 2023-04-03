from flask import *
import pandas as pd
import numpy as np 
import pickle

app=Flask(__name__)
pickle_in=open('classifier.pkl','rb')
rf=pickle.load(pickle_in)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        name=request.form['Name']
        age=request.form['Age']
        bmi=request.form['BMI']
        electsur=request.form['elective_surgery']
        apac2diag=request.form['apache_2_diagnosis']
        apac3diag=request.form['apache_3j_diagnosis']
        arfapa=request.form['arf_apache']
        bunapa=request.form['bun_apache']
        creatapach=request.form['creatinine_apache']
        gcsunaapa=request.form['gcs_unable_apache']
        gcsverapa=request.form['gcs_verbal_apache']
        gluapa=request.form['glucose_apache']
        intuapa=request.form['intubated_apache']
        mapapa=request.form['map_apache']
        venapa=request.form['ventilated_apache']
        wbc=request.form['wbc_apache']
        ap4hoprob=request.form['apache_4a_hospital_death_prob']
        ap4icuprob=request.form['apache_4a_icu_death_prob']
        leuk=request.form['leukemia']
        resapa=request.form['resprate_apache']
        hepfail=request.form['hepatic_failure']
        aids=request.form['aids']
        diamel=request.form['diabetes_mellitus']
        cirrhosis=request.form['cirrhosis']
        lymp=request.form['lymphoma']
        immusupp=request.form['immunosuppression']
        pre=[[bmi,electsur,apac2diag,apac3diag,arfapa,bunapa,creatapach,gcsunaapa,gcsverapa,gluapa,intuapa,mapapa,resapa,venapa, wbc, ap4hoprob, ap4icuprob, aids, cirrhosis,diamel,hepfail,immusupp, leuk, lymp]]
        y_pred=rf.predict(pre)
        if y_pred==1:
            return 'Survived'
        else:
            return 'Not Survived'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=7000)