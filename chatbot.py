
# chatbot.py
def get_response(message):
    message = message.lower()
    if "health" in message:
        return "Health insurance covers medical expenses. Want info about plans?"
    elif "car" in message:
        return "Car insurance protects you in case of accidents or theft."
    elif "life" in message:
        return "Life insurance offers financial support to your family after you."
    elif "claim" in message:
        return "To file a claim, contact your provider and submit required documents."
    else:

# chatbot.py
def get_response(message):
    message = message.lower()
    if "health" in message:
        return "Health insurance covers medical expenses. Want info about plans?"
    elif "car" in message:
        return "Car insurance protects you in case of accidents or theft."
    elif "life" in message:
        return "Life insurance offers financial support to your family after you."
    elif "claim" in message:
        return "To file a claim, contact your provider and submit required documents."
    else:

        return "I'm your insurance assistant! Ask me about health, car, life or claims."