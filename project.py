from fastapi import FastAPI, HTTPException, Path, Query
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
    raise HTTPException(status_code=404, detail="Patient does not exist")

@app.get("/sort")
def sort_patients(sort_by :str = Query(..., description= "sort on the basis of height, weight or BMI"), order:str = Query("asc",description= "sort in asc or desc order")):
    valid_fiels = ["height", "weight", 'bmi']

    if sort_by not in valid_fiels:
        raise HTTPException(status_code= 400, detail=f"invaid field select from {valid_fiels}")

    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, details= "Invalid order select between asc and desc")
    
    data = load_data()
    sort_order = True if order=="desc" else False
    sorted_data = sorted(data.values(),key= lambda x:x.get(sort_by,0), reverse= sort_order)

    return sorted_data