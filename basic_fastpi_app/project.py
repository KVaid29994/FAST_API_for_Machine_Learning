from fastapi import FastAPI, HTTPException, Path, Query
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(..., description= "ID of patient", examples= ['P001'])]
    name : Annotated [str, Field(..., description= "Name of the patient")] 
    city : Annotated[str, Field(...)]
    age :  Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender : Annotated [Literal['male', 'female', 'others'], Field(..., description= "gender of the patient")]
    weight : Annotated[float, Field(..., gt=0, description="weight of the patient in kgs")]
    height : Annotated[float, Field(..., gt=0, lt=150, description="weight of the patient in mts" )]

    @computed_field
    @property

    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi <18.5:
            return "under weight"
        elif self.bmi <25:
            return "elif"
        elif self.bmi <30:
            return "normal"
        else:
            return "obese"

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None, description="Name of the patient")]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Optional[Literal['male', 'female', 'others']], Field(default=None, description="Gender of the patient")]
    weight: Annotated[Optional[float], Field(default=None, gt=0, description="Weight of the patient in kgs")]
    height: Annotated[Optional[float], Field(default=None, gt=0, lt=150, description="Height of the patient in mts")]


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json",'w') as f:
        json.dump(data,f)

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

@app.post("/create")

def create_patient(patient: Patient):
    #load existing data
    data = load_data()
    # check if the patient duplicate 
    if patient.id in data:
        raise HTTPException(status_code=400, detail= "patient already exists")
    
        # add new patient to the database
    data[patient.id] =patient.model_dump(exclude={id})

    ## save into json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message':"Patient created successfully"})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})
@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})
