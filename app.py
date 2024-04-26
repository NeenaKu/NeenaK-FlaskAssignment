from flask import Flask, render_template, request                   
import pickle                       
import numpy as np                      
                        
app=Flask(__name__)     
                        
@app.route('/')                     
def hello():
    return render_template('index.html')                   
                        
@app.route('/result', methods=['POST'])                         
def predict():                      
    gend=request.form['Gender']                     
    if gend=='Male': 
        Gender=1                        
    elif gend=='Female':                        
        Gender=0                        
    Age=int(request.form['Age'])                        
    EstimatedSalary=int(request.form['EstimatedSalary'])                        
    print(Gender,Age,EstimatedSalary)                       
    social_model=pickle.load(open('socialmodel.pkl','rb'))                        
    feature=np.array([[Gender,Age,EstimatedSalary]]) 
    print(feature)                       
    social=social_model.predict(feature)                        
    print(social)                       
    print(social[0])
    if social[0]==1:
        social='User will purchase'
    elif social[0]==0:
        social='User will not purchase'
    print(social)               

    return render_template('result.html',predicted=social)                      
                        
if __name__=='__main__':                        
    app.run()                       
