import re

# Extract YouTube search term from command
def extract_yt_term(command):
    pattern = r'play\s+(.+?)\s+on\s+youtube'  # Extracts "kk song" from "play kk song on youtube"
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

# for removing unwanted words from the command
def remove_words(input_string, words_to_remove):
    words = input_string.split()
    filtered_words = [word for word in words if word.lower() not in words_to_remove]
    result_string =  ' '.join(filtered_words)
    return result_string