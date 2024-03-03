import random

response = ["Better not tell you now", "Outlook Good", "Signs Point to ye-s", "Ask Again Later", "Yes", "Concentrate and Ask Again", "Very Doubtful", "Most Likely", "My sources say NO!", "It is Certain", "Without a Doubt", "As I See it, Yes!", "It is Decidedly so", "Outlook not so Good", "You may rely on it", "Reply Hazy, Try Again", "Yes, Definately!", "My reply is no"]

response_count = int(len(response)) - 1

random_number = random.randint(0, response_count)

comp_response = response[random_number]

print(comp_response)