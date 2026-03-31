def get_advice(symptoms):
    advice_db = {
        "fever": "You have fever. Drink water and take rest.",
        "cough": "You have cough. Try honey and warm water.",
        "headache": "You have headache. Rest in a quiet place.",
        "stomach pain": "You have stomach pain. Avoid heavy food.",
        "sore throat": "You have sore throat. Gargle with warm salt water.",
        "cold": "You have cold. Take vitamin C and stay warm.",
        "fatigue": "You feel tired. Take rest and eat healthy.",
        "vomiting": "You are vomiting. Drink fluids slowly.",
        "diarrhea": "You have diarrhea. Drink ORS and stay hydrated.",
        "chest pain": "Chest pain is serious. Please go to a hospital immediately!",
        "difficulty breathing": "Difficulty breathing is an emergency. Call a doctor now!"
    }

    for symptom in symptoms:
        if symptom in ["chest pain", "difficulty breathing"]:
            return advice_db[symptom]

    advice = []
    for symptom in symptoms:
        if symptom in advice_db:
            advice.append(advice_db[symptom])

    if not advice:
        return "Sorry, I did not understand your symptoms. Please see a doctor."

    return " ".join(advice) + " If you do not feel better, please consult a doctor."


def chatbot():
    print("Hi! I am a symptom checker bot.")
    print("Please enter your symptoms separated by commas (e.g. fever, cough):")
    
    user_input = input().lower()
    symptoms = [sym.strip() for sym in user_input.split(",")]
    
    response = get_advice(symptoms)
    print("\nAdvice:")
    print(response)
    print("\nThank you! Stay healthy.")


if __name__ == "__main__":
    chatbot()
