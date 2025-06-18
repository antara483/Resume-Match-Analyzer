# 🧠 Resume Match Analyzer

Resume Match Analyzer is a full-stack web application that analyzes uploaded resumes and compares them with a job description to compute a match percentage using natural language processing (NLP).

It helps recruiters quickly assess how well a candidate's resume aligns with the job requirements.

---

## 📌 Current Job Description in Use

The application currently compares uploaded resumes against the following stored job description in the database:

**Job Title**: Software Engineer  
**Description**:  
> *We are looking for a Python developer with experience in Flask, REST APIs, MySQL, machine learning, and full-stack web development.*

---


## ⚙️ Features

- Upload resumes via drag-and-drop or file picker
- Parse resume content (name, email, skills, experience, etc.)
- Match resume with job description using NLP and keyword scoring
- Visualize match results with percentage charts
- User authentication (signup/login) with JWT
- RESTful API architecture

---

## 🛠️ Tech Stack

| Layer       | Technologies                                                                 |
|-------------|------------------------------------------------------------------------------|
| Frontend    | React, Tailwind CSS, Chart.js                                                |
| Backend     | Python, Flask, Flask-JWT, Flask-CORS                                         |
| NLP Engine  | NLTK                                                                         |
| Database    | MySQL                                                                        |
| Auth        | JWT (JSON Web Tokens)                                                        |

---
🚀 Running the Application
The project has two main folders:

my-app/ – React frontend for user interaction and visualization

resume-backend/ – Flask backend for resume parsing, matching logic, authentication, and database operations

🧩 1. Backend (Flask)
bash
- cd resume-backend
- python -m venv venv
- venv\Scripts\activate   # On Windows
  Or: source venv/bin/activate   # On Mac/Linux

- pip install -r requirements.txt

  Create a .env file based on .env.example
  Add your MySQL credentials and JWT secret key in the .env file

- python run.py
  ####  Backend will start at: http://127.0.0.1:5000/

💻 2. Frontend (React)
Open a new terminal window and run:

bash
- cd my-app
- npm install
- npm start

# 🙌 Thank You!
Thank you for checking out Resume Match Analyzer!
I hope this tool helps streamline the resume screening process and enhances candidate-job alignment.
Contributions and ideas for improvement are always welcome!
Frontend will start at: http://localhost:3000/

Make sure the backend is running first so the frontend can connect to the API.



