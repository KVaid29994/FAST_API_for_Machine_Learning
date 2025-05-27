from fastapi import FastAPI, HTTPException, Path
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient management system API"}

@app.get("/about")
def about():
    return {
        "About": "A fully functional API to manage patient records, appointments, and medical history."
    }

@app.get("/view")
def view():
    return load_data()

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description= "ID of patient in DB", example= "P001")):
    data = load_data()
    patient_id = patient_id.upper()
    print("Available IDs:", list(data.keys()))       # Debug
    print("Received ID:", repr(patient_id))  
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient does not exist")
