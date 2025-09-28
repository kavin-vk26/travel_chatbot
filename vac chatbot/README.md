# 🤖 AI Chatbot with Streamlit + FastAPI + LangGraph

This project implements a chatbot system with the following architecture:

* **Frontend:** Streamlit (User Interface)
* **Backend:** FastAPI (API service)
* **Conversation Flow Management:** LangGraph
* **Model Integration:** OpenAI (can be replaced with HuggingFace, etc.)

It demonstrates how to build a modular chatbot with separate concerns for UI, API, and logic.

---

## 📂 Project Structure

```
chatbot-project/
│── backend/
│   └── main.py         # FastAPI backend
│── frontend/
│   └── app.py          # Streamlit frontend
│── conversation/
│   └── graph.py        # LangGraph conversation flow
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/kavin-vk26/travel_chatbot.git
cd chatbot-project
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows (PowerShell):**

  ```powershell
  venv\Scripts\activate
  ```
* **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

## 🚀 Running the Project

### Step 1: Start the FastAPI backend

```bash
python -m uvicorn backend.main:app --reload
```

The backend will run at:
👉 `http://127.0.0.1:8000`

### Step 2: Start the Streamlit frontend

In another terminal (with venv activated):

```bash
streamlit run frontend/app.py
```

The frontend will run at:
👉 `http://localhost:8501`

---

## 🛠 Features

* Streamlit UI for user-friendly interaction
* FastAPI backend to handle requests
* LangGraph for structured conversation flow
* OpenAI (or any LLM) integration
* Modular architecture for scalability

---

## 💡 Example Use Case

We implemented a **“Vacation Planner Chatbot”** as a creative demo.
It helps users plan trips by suggesting destinations, activities, and budgets.

Example conversation:

```
User: I want to plan a vacation in December
Bot: Great! Do you prefer mountains or beaches?
```

---

## 📌 Requirements

* Python 3.9+
* Internet connection (for OpenAI API or external models)

---

## 📝 Future Improvements

* Add memory for long conversations
* Integrate with a vector database (Pinecone, FAISS, etc.)
* Add authentication for secure usage
* Deploy on cloud platforms (Render, Railway, etc.)

---

## 👨‍💻 Author

Built with ❤️ by [Your Name]
Feel free to contribute or open issues!

---
