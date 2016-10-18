
file = open("stopwords.txt")
stopwords = file.readlines()

for( i=0; i < stopwords; i++) {
    if (stopwords == response){
        ""
    }
}
# for word in stopwords: print(word)

response = raw_input("What is your name ? ") 
print("Hello " + response)


response = raw_input("How are you?")
if (response == "Good"):
    print("Good to hear that")
elif (response == "Bad"):
    print("to bad")
else:
    print ("Fine to hear")

response = raw_input("What is your age ? ")
if ((int(response))>18):
    print("So you are an adult")
elif((int(response))<12):
    print("So you are still a child")
elif((int(response))>60):
    print("So you much older then me")

    
response = raw_input("Where do you come from ?")
if (response == "England"):
    print("So you from here")
    response = raw_input("Where exactly?")
    print("Nice city, I like to go there")
else:
    print("So you not from here")
    response = raw_input("What you're doing here?")
    print("That sounds interesting")

