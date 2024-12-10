letter = '''Dear <|name|>,
You are Selected!
<|date|>'''

print(letter.replace("<|name|>", "Vivan").replace("<|date|>", "15th October,2024"))  #chaining of a replace function