from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pincode : str

class Patient(BaseModel):
    name : str
    gender : str
    age : int
    address : Address


address_dict ={"city":"delhi", "state":"new delhi", "pincode":"3387737"}

address_1 = Address(**address_dict)
patient_dict = {"name": "kashish", "age":12, "gender": "male","address": address_1}

patient1 = Patient(**patient_dict)
print (patient1)