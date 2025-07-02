# 🆔 ID Card Prevention App – Smart Student Verification System 🎓

A lightweight, responsive, and secure Flask-based web application for verifying student identity using their unique ID. Designed to prevent unauthorized access using fake ID cards in college environments.

---

## 🌟 Features

- 🔐 Unique ID validation using SQLite database
- 📸 Student image preview for verification
- 🧑‍🎓 Displays name, course, branch, batch & college
- 📱 Mobile-friendly web UI
- ⚙️ Easily deployable on Render or cloud platforms

---

## 📁 Project Structure

```
ID_Card_Prevention_App/
│
├── app.py                   # Main Flask app logic
├── init_db.py               # Script to create & insert database records
├── students.db              # SQLite database (auto-generated)
├── requirements.txt         # Python dependencies
├── Procfile                 # For Render deployment
├── render.yaml              # Render configuration
├── templates/
│   └── index.html           # Web frontend
├── static/
│   └── style.css            # App styling
└── README.md
```

---

## 🚀 Live Demo

👉 [https://id-card-prevention-app.onrender.com](#) 

---

## 🛠️ Installation

> Prerequisite: Python 3.8–3.12

```bash
git clone https://github.com/26047306/ID_Card_Prevention_App.git.git
cd ID_Card_Prevention_App
```

### Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
python init_db.py    # Creates students.db with records
python app.py        # Runs Flask app
```

Then open:  
`http://localhost:5000`

---

## 📦 Deploy on Render

1. Create a **Web Service** on [https://render.com](https://render.com)
2. Connect your GitHub repository
3. Use:
   - **Build Command:**
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     gunicorn app:app
     ```
   - **Python Version**: `3.12.3` via `.python-version`

---

## 📚 Sample Student Records

| Unique ID       | Name            | Course | Branch  | Batch      | College | Image Path                   |
|-----------------|------------------|--------|---------|------------|---------|------------------------------|
| 0126CD221111     | Sandeep Kumar     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/sandi.jpg`   |
| 0126CD221124     | Shubham Singh     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/shubham.png` |
| 0126CD221100     | Rahul Kumar       | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/rahul.png`   |
| 0126CD221083     | Nishant Kushwah   | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/nishant.png` |
| 0126CD221095     | Prince Kumar      | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/prince.png`  |
| 0126CD221096     | Prince Thakre     | B.Tech | CSE-DS  | 2022-2024 | OCT     | `/static/images/princt.png`  |

---

## 🧠 Tech Stack

- Python 3
- Flask
- SQLite
- HTML5/CSS3
- JavaScript (for frontend logic)
- Gunicorn (for deployment)

---

## 🔌 API Endpoint

### `/check_id` (POST)

**Request:**
```
unique_id=0126CD221111
```

**Response (if exists):**
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

## 🧪 Sample Usage

> **User enters ID:** `0126CD221111`  
> **App returns:** Student details with photo if found, else "Student not found."

---

## 📜 License

This project is licensed under the [MIT License](LICENSE)

---

## 👨‍💻 Author

**Sandeep Yadav**  
📧 [ravindrayadav4367@gmail.com](mailto:ravindrayadav4367@gmail.com)  
🎓 B.Tech CSE (Data Science), Oriental College of Technology

---

⭐ If you liked this project, consider giving it a ⭐ on GitHub!
