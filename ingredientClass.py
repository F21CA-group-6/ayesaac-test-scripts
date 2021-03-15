dairy = ["dairy", "milk", "butter", "cream", "cheese", "yogurt"]
nuts = ["nuts", "peanuts", "pecans", "walnuts", "almonds", "brazil nuts", "cashews",
	"chesnuts", "filberts", "hazelnuts", "macadamia nuts", "pine nuts", "pistachios"]
meat = ["meat", "chicken", "pork", "beef", "veal"]

text = "blah blah blah blah peanuts blah blah milk blah blah blah veal"

# extract words from string
split_text = text.split()

for word in split_text:
	if word in dairy:
		print("Dairy " + word)
	if word in nuts:
		print("nuts " + word)
	if word in meat:
		print("meat " + word)
