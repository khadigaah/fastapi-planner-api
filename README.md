#  Event Planner API

A robust RESTful API built with **FastAPI** and **MongoDB** for managing events, users, and secure authentication. This project is designed with best practices in mind, featuring asynchronous database operations and complete containerization.

---

## Features

* **User Authentication:** Secure signup and login mechanisms using hashed passwords (bcrypt) and JSON Web Tokens (JWT).
* **Event Management:** Full CRUD (Create, Read, Update, Delete) operations for event planning.
* **Asynchronous Database:** Fast and non-blocking database interactions using MongoDB, Motor, and Beanie ODM.
* **Data Validation:** Strict data validation and serialization using Pydantic V2.
* **Containerization:** Fully dockerized environment for seamless setup and deployment.
* **Automated Testing:** Comprehensive API testing using Pytest and HTTPX.

---

##  Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MongoDB
* **ODM (Object Document Mapper):** Beanie
* **Authentication & Security:** Passlib (bcrypt), python-jose (JWT)
* **Testing:** Pytest, HTTPX
* **Environment/Deployment:** Docker, Docker Compose, Uvicorn

---

## 📂 Project Structure

```text
planner/
├── auth/               # JWT authentication and hashing logic
├── database/           # MongoDB connection and database settings
├── models/             # Beanie ODM models and Pydantic schemas (Users, Events)
├── routes/             # API endpoints (Routers)
├── test/               # Pytest automated tests
├── main.py             # FastAPI application entry point
├── requirements.txt    # Production dependencies
├── docker-compose.yml  # Docker services configuration
└── Dockerfile          # Docker image instructions
