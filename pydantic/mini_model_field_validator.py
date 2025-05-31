## In Pydantic v2, a @model_validator is a class-level validator used to validate or transform the entire model after all fields are validated.
''' 🔍 Purpose of @model_validator
Validate relationships between fields

Run logic that needs access to multiple fields at once

Modify field values or enrich the model before it's finalized'''

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):
    name : str
    email : EmailStr
    age :int
    weight : float
    married : bool
    allergies : list[str]
    contact_details : dict[str, str]

    @model_validator(mode = "after")
    
    def validate_emergency_contact(cls,model):
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError ('Patients older than 60 must have an emergency contact')
        else:
            return model



def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'nitish', 'email':'abc@icici.com', 'age': '66', 'weight': 75.2, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details':{'phone':'2353462', "emergency": "2337773273"}}

patient1 = Patient(**patient_info) 


