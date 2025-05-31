## 🎯 Project: User Signup Form Validatorun     

import re
import streamlit as st
from pydantic import BaseModel, EmailStr, field_validator,ValidationError

class UserSignup(BaseModel):
    name : str
    email : EmailStr
    age: int
    password: str
    confirm_password : str

    @field_validator("name")
    @classmethod
    def name_must_be_alpha(cls,v):
        if not v.replace(" ", "").isalpha():
            raise ValueError ("Name must contain only alphabets and spaces")
        return v.title().upper()
    
    @field_validator("email")
    @classmethod
    def email_validator(cls,v):
        ## class and Value (which user inputs)
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = v.split("@")[-1]
        if domain_name not in valid_domains:
             raise ValueError("not a valid domain")
        else:
             return v

    @field_validator('age')
    @classmethod
    def age_must_be_18_or_more(cls, v):
        if v < 18:
            raise ValueError("You must be at least 18 years old to register")
        return v

    @field_validator('password')
    def password_strength(cls, v):
            pattern = re.compile(r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$')
            if not pattern.match(v):
                raise ValueError("Password must be 8+ chars, include a number, a special char, and an uppercase letter")
            return v

    @field_validator('confirm_password')
    def passwords_match(cls, v, values):
            if 'password' in values.data and v != values.data['password']:
                raise ValueError("Passwords do not match")
            return v

st.title("🔐 User Signup Form Validator")

with st.form("signup_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    age = st.number_input("Age", min_value=0, step=1)
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Validate")

    if submit:
        try:
            user = UserSignup(
                name=name,
                email=email,
                age=age,
                password=password,
                confirm_password=confirm_password
            )
            st.success("✅ User data validated successfully!")
            st.json(user.model_dump())
        except ValidationError as e:
            st.error("❌ Validation failed:")
            for err in e.errors():
                st.write(f"**{err['loc'][0]}**: {err['msg']}")