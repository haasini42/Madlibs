#string concatenation (aka how to put strings together)
#suppose if we creat a string that says "subscribe to _______"
#youtuber = "Cosmic Eye" #some string variable

# a few ways to do this
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2= input("Verb: ")
famous_person = input("famous person: ")

madlib = f"Computer programming is so {adj}! It makes me feel so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2}. Like you are {famous_person}!"

print(madlib)


