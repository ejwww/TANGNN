import json
import re

def clean_data(data):
    # Compile regex patterns
    sentiment_pattern = re.compile(r"^(Negative|Neutral|Positive):\s")
    citation_pattern = re.compile(r"\{\{[^}]*\}\}")

    # Process each entry in 'numbers_to_sentence'
    for entry in data:
        if 'numbers_to_sentence' in entry:
            for key, sentence in entry['numbers_to_sentence'].items():
                # Remove sentiment labels
                sentence = sentiment_pattern.sub("", sentence)
                # Remove citations
                sentence = citation_pattern.sub("", sentence)
                # Update the cleaned sentence back in the dictionary
                entry['numbers_to_sentence'][key] = sentence
    return data

# Load your JSON data
with open("C:\\Users\\admin\\Documents\\Tencent Files\\463996081\FileRecv\\3.txt", "r") as file:
    data = json.load(file)

# Clean the data
cleaned_data = clean_data(data)

# Save the cleaned data back to a file
with open("C:\\Users\\admin\\PycharmProjects\\pythonProject\\final_sentiment2.json", "w") as file:
    json.dump(cleaned_data, file, indent=4)

print("Data cleaning completed.")





