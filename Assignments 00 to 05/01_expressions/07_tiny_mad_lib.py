SENTENCE_START: str = "GIAIC is amazimg. I learned to program and used Python to make my " 

def tiny_madlibs():
    # Get the three inputs from the user to make the adlib
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    # This code will join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")



if __name__ == '__main__':
    tiny_madlibs()