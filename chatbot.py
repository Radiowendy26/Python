import wikipedia

file = open("stopwords.txt")
stopwords = file.read().split('\n')

# for word in stopwords: print(word)

response = raw_input("What is your name ? ") 
wordsFromUser = response.split(' ')

for word in stopwords:
    if word in wordsFromUser:
        response = response.replace(word, "")

print("Hello " + response)

response = raw_input("How are you?")
if (response == "good"):
    print("Good to hear that")
elif (response == "bad"):
    print("to bad")
else:
    print ("Fine to hear")

response = raw_input("What is your age ? ")
if((int(response))<12):
    print("So you are still a child")
elif ((int(response))<60):
    print("So you are an adult")
else:
    if ((int(response))>60):
        print("So you much older then me")
    else:
        print("That a nice age")

    
response = raw_input("Where do you come from ?")
if (response == "england"):
    print("So you from " + response)
    response = raw_input("Where exactly?")
    print("Nice city, I like to go there")
else:
    print("So you're from " + response + ", wauw")
    response = raw_input("What you're doing here?")
    print("That sounds interesting")
    
response = raw_input("Do you have brothers or sisters?")
if (response == "brother"):
    print(response + " are so nice to have")
elif (response == "sister"):
    print(response + " are so nice to have")
else: 
    if (response == "yes"):
        print("Nice to have them")
    else: 
        print("So you are on you're own")
    
response = raw_input("What are you doing, study or working?")
if (response == "study"):
    print("So you're studying")
    response = raw_input("What are you studying?")
    print("Ohw, thats cool")
elif (response == "working"):
    print("Alright that's good")
    response = raw_input("What are you doing for living?")
    print("Ohw, thats sounds like good work to do")
else:
    print("interesting")

response = raw_input("What is you're favorite movie?")
print response
print ("Do you mean " + wikipedia.summary(response,sentences=2))    

response = raw_input("What for sports do you play?")
print response
print ("Do you mean " +  wikipedia.summary(response,sentences=2))
response = raw_input("How many times are you doing " + response + " ?")
print ("That's good for you")

response = raw_input("What are you're hobby's?") 
print response
print ("Do you mean " + wikipedia.summary(response,sentences=2))
response = raw_input("In which city are you doing " + response + " ?")
print ("That's a beautiful place. I want to go there")

response = raw_input("Who is you're favorite artist?") 
print response
print ("Do you mean " + wikipedia.summary(response,sentences=2))
          
response = raw_input("Do you like to play a game?")
if (response == "yes"):
    print ("let's begin")
    response = raw_input("What is the longest word in the English language? ")
    print ("there is a mile between the first and last letters!")
else:
    print ("then not")
    

