def mood_response(mood):
    if mood.lower() == "happy":
        return "Glad to hear it!"
    elif mood.lower() == "sad" or mood.lower() == "terrible" or mood.lower() == "upset":
        return "I'm sorry to hear that."
    elif mood.lower() == "angry":
        return "Let's take a deep breath together."
    elif mood.lower() == "ok" or mood.lower() == "good" or mood.lower() == "fine":
        return "All right, let me know if you need anything."
    else:
        return "I'm not sure what to say."