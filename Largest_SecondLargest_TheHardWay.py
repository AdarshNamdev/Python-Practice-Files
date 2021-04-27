
wordlist = ['HelloBabaSikandar', 'Adarsh', 'MachineLearningEngineer', "qawsedrftgyhujikolpmnbv",'Mississipi', 'June', 'JuniperNetwork', 'MachineLearningEngineer']

largest = wordlist[0]   # "Adarsh"
second = ""

for word in wordlist[1:]:
    if len(word) >= len(largest):
        second = largest
        largest = word

    elif len(word) >= len(second):
        second = word

print("First Largest: ", largest)
print("Second Largest: ", second)
