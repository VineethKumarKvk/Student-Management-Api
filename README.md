# Student Management System API

The **Student Management System API** is a Flask-based project designed for efficiently managing student information within an educational institution. This API leverages Flask for creating endpoints and utilizes SQLAlchemy to interact with a database. Below are the primary functionalities and endpoints of this project:

## Table of Contents
- [User Registration](#user-registration)
- [User Login and JWT Generation](#user-login-and-jwt-generation)
- [Adding Student Marks](#adding-student-marks)
- [Viewing Student Results](#viewing-student-results)

---

## User Registration

**Endpoint:** `/register`  
**Method:** `POST`

**Description:** Users can register their accounts within the system. This endpoint collects user information and stores it securely in the database, allowing for future authentication and authorization.

---

## User Login and JWT Generation

**Endpoint:** `/login`  
**Method:** `POST`

**Description:** Users can log in to the system through this endpoint, which generates JSON Web Tokens (JWTs) using Flask-JWT-Extended. These tokens are used for secure and authenticated access to protected endpoints.

---

## Adding Student Marks

**Endpoint:** `/addMarks`  
**Method:** `POST`

**Description:** This protected endpoint is accessible only to authorized users, specifically Teachers and the Principal. It enables them to add academic marks and performance data for individual students, ensuring the accuracy and security of student records.

---

## Viewing Student Results

**Endpoint:** `/getMarks`  
**Method:** `GET`

**Description:** Users, including Teachers and the Principal, can retrieve and view student results and academic performance through this endpoint. It provides access to essential information for tracking and evaluating student progress.

---

This Student Management System API is designed to streamline the process of managing student data within an educational institution, ensuring secure access, data integrity, and authentication. It is a valuable tool for administrators, teachers, and other authorized personnel to maintain and retrieve student information efficiently.

For detailed usage and installation instructions, please refer to the project documentation.
