# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="Travel Chatbot API")

# Input model
class Message(BaseModel):
    user_message: str
    user_id: str  # To track multi-step conversation per user

# Store conversation state per user
conversation_memory: Dict[str, Dict] = {}

# Multi-step logic
def generate_response(user_id: str, message: str) -> str:
    user_state = conversation_memory.get(user_id, {"step": 0, "data": {}})
    step = user_state["step"]
    data = user_state["data"]
    msg = message.lower()

    # Step 0: Ask destination type
    if step == 0:
        user_state["step"] = 1
        conversation_memory[user_id] = user_state
        return "Hi! I'm your Travel Advisor. Do you prefer **mountains**, **beaches**, or **cities**?"

    # Step 1: Save destination type
    elif step == 1:
        if any(x in msg for x in ["mountain", "beach", "city"]):
            data["destination_type"] = msg
            user_state["step"] = 2
            conversation_memory[user_id] = user_state
            return "Great! What's your **budget**? (low / medium / high)"
        else:
            return "Please choose **mountains**, **beaches**, or **cities**."

    # Step 2: Save budget
    elif step == 2:
        if any(x in msg for x in ["low", "medium", "high"]):
            data["budget"] = msg
            user_state["step"] = 3
            conversation_memory[user_id] = user_state
            return "Got it. How many **days** do you plan to travel?"
        else:
            return "Please choose a budget: **low**, **medium**, or **high**."

    # Step 3: Save duration
    elif step == 3:
        try:
            days = int(msg)
            data["days"] = days
            user_state["step"] = 4
            conversation_memory[user_id] = user_state
            return "Awesome! What are your **interests**? (culture / adventure / relaxation)"
        except ValueError:
            return "Please enter a number for days."

    # Step 4: Save interests and give recommendation
    elif step == 4:
        if any(x in msg for x in ["culture", "adventure", "relaxation"]):
            data["interest"] = msg
            user_state["step"] = 5
            conversation_memory[user_id] = user_state
            # Generate final recommendation
            return generate_final_recommendation(data)
        else:
            return "Please choose an interest: **culture**, **adventure**, or **relaxation**."

    # Step 5: Restart conversation
    else:
        conversation_memory[user_id] = {"step": 0, "data": {}}
        return "If you want, we can start planning a new trip! Type anything to begin."

def generate_final_recommendation(data: dict) -> str:
    dest = data["destination_type"]
    budget = data["budget"]
    days = data["days"]
    interest = data["interest"]

    # Simple example logic
    if dest == "mountain":
        place = "Himalayas, India"
    elif dest == "beach":
        place = "Goa, India" if budget != "high" else "Maldives"
    else:
        place = "Paris, France" if budget == "high" else "Bangkok, Thailand"

    return (f"Your recommended trip:\n"
            f"- Destination: {place}\n"
            f"- Duration: {days} days\n"
            f"- Interest: {interest}\n"
            f"- Budget: {budget}\n"
            f"Have a great trip! ✈️🏖️🏔️")

@app.post("/chat")
async def chat(msg: Message):
    response = generate_response(msg.user_id, msg.user_message)
    return {"bot_response": response}
