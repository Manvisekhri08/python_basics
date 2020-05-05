def sentence_maker(phrase):
    interrogatives = ("how","why","what","when","whom","whose")
    captilised = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(captilised)
    else:
        return "{}.".format(captilised)

results=[]
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))


print(" ".join(results))                
