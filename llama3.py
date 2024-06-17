import ollama

# Read the list of groceries from groceries.txt
with open('groceries.txt', 'r') as file:
    groceries = file.read()

# Pass the list of groceries as the content to the chat model
response = ollama.chat(model='llama3', messages=[
  {
    
    'role': 'user',
    'content': "You are preparing a grocery list, organize them by the most common categories found in a grocery store. " + groceries,
  },
])

# Write the organized list from the chatbot response to sorted.txt
with open('sorted.txt', 'w') as file:
    file.write(response['message']['content'])