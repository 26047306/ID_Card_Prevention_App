# 🆔 ID Card Prevention App

The **ID Card Prevention App** is a Flask-based web application designed to **verify and prevent unauthorized use** of student ID cards. It allows users (such as gatekeepers, admins, or teachers) to check a student's identity using a unique ID number, retrieve their stored information, and verify their photo instantly from a secure database.

---

## 📘 Project Explanation

### 🎯 Objective
To build a lightweight, responsive, and secure web app that checks whether a student's ID is valid by querying a preloaded SQLite database containing details like name, course, batch, branch, college name, and photograph.

### 🧠 Problem Solved
Institutions face identity-related challenges such as:
- Entry by unauthorized persons using fake ID cards
- Manual identity verification delays
- Lack of digital student identity database

This app provides a **real-time verification tool** to authenticate IDs and reduce misuse.

### 📌 Use Case
- University or college gate entry checking
- Examination hall verification
- Hostel visitor management
- Admin or principal record lookup

---

## 🚀 Features

- 🔐 Secure backend with SQLite DB
- 🔎 ID-based student lookup
- 📸 Image display for visual confirmation
- 🧑‍🎓 Shows name, course, batch, branch, and college
- 🟢 Responsive design for mobile/desktop
- 🛰️ REST API endpoint for POST requests
- ☁️ Easily deployable on Render

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Frontend   | HTML, CSS, JavaScript |
| Backend    | Python (Flask)    |
| Database   | SQLite            |
| Deployment | Render            |

---

## 🖼️ UI Overview

- **Input Field**: Enter Unique ID
- **Submit Button**: Triggers verification
- **Output Section**: Displays result with details and image

---

## 📋 Sample Student Records

| Unique ID       | Name            | Course | Branch  | Batch      | College | Image Path                   |
|-----------------|------------------|--------|---------|------------|---------|------------------------------|
| 0126CD221111     | Sandeep Kumar     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/sandi.jpg`   |
| 0126CD221124     | Shubham Singh     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/shubham.png` |
| 0126CD221100     | Rahul Kumar       | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/rahul.png`   |
| 0126CD221083     | Nishant Kushwah   | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/nishant.png` |
| 0126CD221095     | Prince Kumar      | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/prince.png`  |
| 0126CD221096     | Prince Thakre     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/princt.png`  |

---

## 🔌 API Endpoint

### `/check_id` (POST)

**Request Example:**
```
unique_id=0126CD221111
```

**Response Example:**
```json
{
  "status": "exists",
  "unique_id": "0126CD221111",
  "name": "Sandeep Kumar",
  "course": "B.Tech",
  "branch": "CSE-DS",
  "batch": "2022-2024",
  "college": "OCT",
  "image_path": "/static/images/sandi.jpg"
}
```

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/yourusername/ID_Card_Prevention_App.git
cd ID_Card_Prevention_App

# (Optional) Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open your browser at `http://localhost:5000`

---

## ☁️ Deploy on Render

### Required Files:
- `requirements.txt`
- `Procfile`
- `render.yaml`

### `Procfile`
```
web: gunicorn app:app
```

### `render.yaml`
```yaml
services:
  - type: web
    name: id-card-prevention
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "gunicorn app:app"
    plan: free
    branch: main
    autoDeploy: true
```

---

## 👨‍💻 Author

**Sandeep Yadav**  
B.Tech CSE (Data Science)  
Oriental College of Technology, Bhopal  
📧 Email: ravindrayadav4367@gmail.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐ If you found this project useful, don’t forget to give it a star on GitHub!
