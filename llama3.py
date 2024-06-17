import ollama

with open('groceries.txt', 'r') as file:
    groceries = file.read()

response = ollama.chat(model='llama3', messages=[
    {
        'role': 'user',
        'content': "You are preparing a grocery list, organize them by the most common categories found in a grocery store. " + groceries,
    }    
])

with open('sorted.txt', 'w') as file:
    file.write(response['message']['content'])