# AFIA ZAMAN, PROJECT NUMBER - 04
"""
you & your friend is playing hide & seek online. Now to find your friend
who is hiding, the game will provide you some questions & you have
to answer them with 'yes/no/maybe'. If your guess is right you'll find her.
If you are wrong you'll be trapped or lose

"""
# Let's start with giving the first hint.
print("Do you think she is hiding in the terrace? ")
choice = input("yes/no? ") .lower()
if choice == "yes":
    print("Yoo! You found her. ")
    exit()
else:
    pass
# You've fallen into the trap. Now you've to go through the next step to find her. Try to answer them correctly.
direction = input("OHHOO!! You have came to the wrong way. Now you'll have to play the hide & seek with more steps! so,do you think she is hiding in-door? ") .lower()
if direction == "yes":
    pass
# Keep going! Maybe you are going to find her soon.
    cupboard = input("Okay! Is she hiding in the cupboard? ") .lower()
    if cupboard == "yes":
        pass
# if you can answer this step correctly you'll win!!
        sure = input("She has changed her hiding place & you are searching for her for a long time. Are you sure you still wanna find her? ") .lower()
        if sure == "yes":
            print("Yahoo! Finally you find her.  ")
            exit()
        elif sure == "no":
            print("Game over! Unfortunately you couldn't find her.  ")
            exit()
# You've come to another way. This way is just for your distraction. No matter what you choose now, you'll defeat!
    elif cupboard == "no":
         pass
         bed = input("Do you think she is under the bed? ") .lower()
         if bed == "yes":
            print("Yahoo! You have come to the end, but unfortunately you couldn't find her.  ")
            exit()
         elif bed == "maybe":
            print("Yahoo! You have come to the end, but unfortunately you couldn't find her  ")
            exit()
# Keep going! Maybe you are going to find her soon or you'll defeat soon!
elif direction == "no":
    pass
left = input("Ooppss! you have chosen the wrong answer! Think carefully now.. DO you wish to go to the left? ") .lower()
if left == "maybe":
    print("Yahoo! Finally you find her. ")
else:
    print("Game over! Unfortunately you couldn't find her. ")





