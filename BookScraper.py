import requests
import json
import time

# This script scrapes the full text of a book from the Turath website and saves it to a file.

start_time = time.time()

payload = {}

headers = {
    'Cookie': '__cfduid=d0b2a5a6c4a4e1e9b3f2d9b8b9a6b9c6c1617158574; _ga=GA1.2.1253656535.1617158577; _gid=GA1.2.175145893.1617158577; _gat_gtag_UA_153738851_1=1'
}

fullText = ''
error_flag = False  # Flag to check for errors

book_id = 147927

for i in range(3, 67):
    print(f"Page {i}")
    url = f"https://api.turath.io/page?book_id={book_id}&pg={i}&ver=3"
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code != 200:
        error_flag = True
        print(f"Error on page {i}. Status code: {response.status_code}")
        break

    text = response.text
    json_data = json.loads(text)
    text = json_data['text']

    fullText += text

# Save the full text to a file
book_name = 'الأربعون النووية'
with open(f'data/{book_name}.txt', 'w', encoding='utf-8') as f:
    f.write(fullText)

# Measure the time of the script
print("--- %s seconds ---" % (time.time() - start_time))

if error_flag:
    print("Script stopped due to an error.")
else:
    print("Script completed successfully.")