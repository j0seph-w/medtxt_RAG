import anthropic

client = anthropic.Anthropic(
    api_key="YOUR-API-KEY"
)

file_path = 'all_txt.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()
    context_string = ''.join(lines)

question = 'I have excised a lesion on the lateral aspect of a patients nose, the defect it is about 1.5cm in diameter. What closure technique should I use? What factors do I need to consider when choosing this technique'

message = client.messages.create(
 model="claude-3-haiku-20240307",
 max_tokens=3000,
 temperature=0.0,
 system="You are a medical Question Answering tool, provide clear answers referencing the context provided. You may collate relevant material to build an answer. Admit if you are unsure or cannot provide an answer.",
 messages=[
 {
 "role": "user",
 "content": f"The following context is the content of a medical textbook titled 'Fundamental Techniques of Plastic Surgery'. <context>{context_string}</context><instructions>Using the information from the context above, please answer the following question: '{question}'.<\instructions>"
 }
 ]
)  

print(message.content)