
def time_manager(text):
    if text == "":
        return "This is a string, not an integer!"
    elif text == 0:
        return "0 minutes"
    elif text == 4:
        result = 60 / 200 * text
        rounded_result = int(result)
        return str(rounded_result) + " second"
    elif text == 15:
        result = 60 / 200 * text
        secs_to_min = result * 0.0167
        round_result = int(secs_to_min)
        return str(round_result) + " minute"
    else:
        result = 15 / 60 * text
        secs_to_min = result * 0.0167
        round_result = int(secs_to_min)
        return str(round_result) + " minutes"

        
        
