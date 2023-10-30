from fastapi import FastAPI
import pickle 
import numpy as np 

app = FastAPI()

with open("model/decision_tree_model.pkl","rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(age:int, job:str, marital:str, education:str, balance:int, housing:str, loan:str, contact: str, duration:int, campaign:int, previous:int):
    
    contact_category = {"cellular":0, "tellephone":1, "unknown":2}
    job_category = {"management":4, "blue-collar":1,"technician":9, "admin.":0, "services":7,"retired":5, "self-employed":6,"entrepreneur":2, "unemployed":10,"housemaid":3,"student":8,"unknown":11}
    marital_category = {"single":2, "married":1, "divorced":0}
    education_category = {"primary":0, "secondary":1, "tertiary":2, "unknown":3}
    housing_category = {"yes":1,"no":0}
    loan_category = {"yes":1,"no":0}
    
    contact = contact_category[contact]
    job = job_category[job]
    marital = marital_category[marital]
    education = education_category[education]
    housing = housing_category[housing]
    loan = loan_category[loan]
    
    input = np.array([age, balance, duration, campaign, previous, contact, job, marital, education, housing, loan])
    prediction = int(model.predict([input]))
    
    if prediction==1:
        return "Customer will subscribe!"
    else:
        return "Customer will not subscribe!"
    