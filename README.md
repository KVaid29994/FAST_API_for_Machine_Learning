# 🩺 Patient Management API with FastAPI

## 🔍 What is an API?

An **API (Application Programming Interface)** enables two software systems to communicate with each other. Think of it as a bridge — for example, your application sends data (like a patient's weight and height) to an API, and in return, receives a prediction or computed output (like BMI). APIs make services reusable, secure, and scalable.

---

## ⚡ Why FastAPI?

[FastAPI](https://fastapi.tiangolo.com/) is a **modern, high-performance Python web framework** for building APIs quickly and efficiently. It is designed for speed, scalability, and developer-friendly features.

### ✅ Key Benefits:
- 🚀 **Blazing fast** — Built on Starlette & Pydantic with async support for production-grade performance.
- 🧪 **Auto-validation** — Automatically validates request and response data.
- 📄 **Interactive docs** — Swagger UI and ReDoc generated out of the box.
- 🧩 **Perfect for ML** — Seamlessly integrates with machine learning model deployments.

---

## 📦 Project Overview

A lightweight backend API built using **FastAPI + Python**, designed for doctors to **create, view, edit, and delete** patient records. This is a **prototype version** storing data in simple **JSON files** to simulate real database functionality.

> ⚠️ Database integration (e.g., PostgreSQL, MongoDB) is planned in future versions.

---

## 🔧 Core Features

- ✅ **Create New Patients**  
  Add new patient entries with automatic timestamping.

- 📋 **View Patients**  
  - View all records  
  - Filter by new or returning patients  
  - View full medical history of a patient

- ✏️ **Edit Existing Records**  
  Modify patient data such as name, vitals, or diagnosis.

- 📊 **Auto BMI Calculation**  
  Automatically compute and update Body Mass Index (BMI) based on provided height and weight.

- 🗑️ **Delete Records**  
  Remove individual patient entries when no longer needed.

---

## 🚀 Getting Started

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/FAST_API_for_Machine_Learning.git
   cd FAST_API_for_Machine_Learning
