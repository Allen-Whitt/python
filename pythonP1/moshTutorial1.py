# Convert text into emojis, just some fun with dictionaries 
def emojify(msg):
	words = msg.split(' ')
	output = ""
	for word in words:
		output += emojis.get(word, word) + " "
	return output

emojis = { 
    ":)" : "😃",
    ":(" : "🙁"
}

print(emojify(input('>')))
