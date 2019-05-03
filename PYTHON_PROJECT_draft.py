print("WELCOME TO ESCAPE ROOM....")
print("You wake up in a haze....your head is pounding and your vision is blurry. You have no idea where you are.")
print("You are in a room that is filled with strange items. You immediately run to the door to try and escape.")
print("You reach the door and see that there are three padlocks on the door. Each one is unique and should be analyzed.")
print("press 1 to analyze the padlocks or 2 to continue exploring the room")

userInput = input("")
analyze = "analyze padlocks"
nullOption = "That is not a wise decision. Please input something else. Look at the previous statement for clues."
optionOne = "1"
optionTwo = "2"
optionThree = "3"
subOptionOne = "one"
subOptionTwo = "two"
subOptionThree = "three"

while userInput != optionOne:
    print(nullOption)
    userInput = input("")

if userInput == optionOne:
    print("One looks like a classic padlock that will take a key. The other one looks like it is voice activated. The last one seems to have two strange key entries. ")
    print("Press 1 to continue exploring the roon.")
    print("Press 2 to continue to anazlyze the padlocks.  ")
    userInput = input("")

while userInput != optionOne:
    print(nullOption)
    userInput = input("")

if userInput == optionOne:
    print("You continue to explore the room......")
    print("You see a strange poster with the number 5 written five times. There is also a small box with some markings on them. Lastly you see a key ring with 6 different keys on it.")
    print("Input 1 to walk up to the poster.")
    print("Input 2 to explore the box.")
    print("Input 3 to examine the key ring.")
    userInput = input("")

    if userInput == optionOne:
        print("You walk up to the poster and stare at it for a few seconds. The only thing written on this poster is the number 5 written five times.")
        print("Input 1 to count to five.")
        print("Input 2 if you want to read the number 5 five times.")
        print("Input 3 if you want to continue to explore the room.")
        userInput = input("")
    if userInput == optionTwo:
        print("You walk up to this strange 4x4 box. It has a strange texture that you can only describe as flesh. There is also a smell so putrid and strong that it can only be described as death.")
        print("You see a label in small fine print that says WARNING! WARNING! WARNING! - PANDORA PANDORA PANDORA - DO NOT OPEN THIS BOX BY ANY MEANS!")
        print("Input 1 if you wish to open the box.")
        print("Input 2 if you want to walk away.")
        print("Input 3 if you want to continue to explore the room.")
        userInput = input("")
    if userInput == optionThree:
        print(nullOption)
        subOptionThree = "three"
        userInput = input("")





while userInput != optionTwo and userInput != optionOne and userInput != optionThree:
    print(nullOption)
    userInput = input("")

if userInput == optionOne:
    print("You walk up to the poster and stare at it for a few seconds. The only thing written on this poster is the number 5 written five times.")
    print("Input 1 to count to five.")
    print("Input 2 if you want to read the number 5 five times.")
    print("Input 3 if you want to continue to explore the room.")
    userInput = input("")



if userInput == optionTwo:
    print("You walk up to this strange 4x4 box. It has a strange texture that you can only describe as flesh. There is also a smell so putrid and strong that it can only be described as death.")
    print("You see a label in small fine print that says WARNING! WARNING! WARNING! - PANDORA PANDORA PANDORA - DO NOT OPEN THIS BOX BY ANY MEANS!")
    print("Input 1 if you wish to open the box.")
    print("Input 2 if you want to walk away.")
    print("Input 3 if you want to continue to explore the room.")
    userInput = input("")

if userInput == optionThree:
    print("You walk up to this key ring. As you saw before there are 6 rings on this particualr key ring.")
    print("As you take a close look at the patterns on the key ring you start to see some similarities. They all come in pairs. ")
    print("Input 1 if you wish to pick up the key chain ring.")
    userInput = input("")


while userInput != optionTwo and userInput != optionOne and userInput != optionThree:
    print(nullOption)
    userInput = input("")




if userInput == optionTwo and userInput == subOptionTwo:
    print("As you open the box the foul odor and strange flesh texture disappear and the box turns into steel. ")
    print("You feel the magic in the air. There must be a warlock near.")
    print("Inside this box is the golden goose key. This must be the key for one of the locks.")
    print("Input 1 to grab the golden goose key")
    print("Input 2 to close the box and walk away")
    print("Input 3 if you want to just walk away. ")
    userInput = input(" ")








