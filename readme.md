# Django Quiz App

## Overview
This is a simple Django-based quiz application. The app allows a user to:
1. Start a quiz session.
2. Get a random multiple-choice question.
3. Submit an answer.
4. View a summary of their quiz session with total, correct, and incorrect responses.

### Features
- **Session-based quiz progress tracking:** Stores user progress without requiring authentication.
- **Randomized questions:** Questions are fetched randomly from the database.
- **Answer evaluation:** Validates submitted answers and updates the session.

---

## Assumptions
- The application assumes that the database has preloaded questions.
- Each question has four options (`A`, `B`, `C`, `D`) and a single correct answer (`correct_option`).

---



### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo-url/quiz-app.git
   

2. **install dependencies**
    ```bash
    pip install -r requirements.txt

3. **Run**
    ```bash
    python manage.py runserver


