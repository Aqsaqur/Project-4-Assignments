def mad_libs():
    print("Welcome to the Great Time-Traveling Adventure Mad Libs!")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    object1 = input("Enter an object: ")
    year = input("Enter a year: ")
    character = input("Enter a historical figure or fictional character: ")
    animal = input("Enter an animal: ")
    silly_phrase = input("Enter a silly phrase: ")
    made_up_place = input("Enter a made-up place name: ")
    clothing_item = input("Enter a weird clothing item: ")
    bizarre_food = input("Enter a bizarre food: ")
    creature = input("Enter a creature: ")
    song_title = input("Enter a random song title: ")
    strange_object = input("Enter a strange object: ")
    funny_command = input("Enter a funny command: ")
    friend_name = input("Enter a friend's name: ")
    mysterious_object = input("Enter a mysterious object: ")

    story = f'''
    One day, {name} was walking through {place} when they stumbled upon a {adjective} {object1}.
    Curious, they picked it up and suddenly, *POOF!*—they were transported to the year {year}!
    
    Confused but excited, they looked around and saw {character} riding a {animal} while yelling, "{silly_phrase}!"
    
    "Where am I?" {name} asked.
    
    "You're in the land of {made_up_place}, where everyone wears {clothing_item} and eats {bizarre_food} for breakfast!"
    
    Before {name} could react, a giant {creature} appeared and started dancing to "{song_title}".
    It handed them a {strange_object} and said, "{funny_command}!"
    
    Without thinking, {name} pressed a button and—ZAP! They were back home, holding a {mysterious_object} as proof of their adventure.
    
    From that day on, nobody believed their story... except for {friend_name}, who secretly had a {mysterious_object} of their own.
    
    The End... or is it?
    '''
    print("\nHere is your Mad Libs story:")
    print(story)

mad_libs()


