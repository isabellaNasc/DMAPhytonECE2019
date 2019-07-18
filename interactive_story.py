print("Welcome to the interactive story")

print("You fall in a hole")

userschoice = input("type 1 to explore, type 2 to check your phone ")

if userschoice == "1":
    print("you decide to explore")
    userschoice= input("type 1 to go right, type 2 to go left")
    if userschoice == "1":
        print("you decide to go right")
        print("you see a glowing light...")
        userschoice = input("type 1 to explore it, type 2 to keep walking")
        if userschoice == "1":
            print("you decide to follow the light")
            print("the light leads you to a maze")
            userschoice = input("type 1 to go right, type 2 to go left")
            if userschoice == "1":
                print("you decide to go right")
                print("you are lost")
            if userschoice == "2":
                print("you decide to left")
                userschoice = input("type 1 to go right, type 2 to go left")
                if userschoice == "1":
                    print("you decide to go right")
                    print("you are lost")
                if userschoice == "2":
                    print("you decide to left")
                    userschoice = input("type 1 to go right, type 2 to go left")
                    if userschoice == "1":
                        print("you decide to go right")
                        userschoice = input("type 1 to go right, type 2 to go left")
                        if userschoice == "1":
                            print("you decide to go right")
                            print("you are lost")
                        if userschoice == "2":
                            print("you decide to go left")
                            print("you find an exit")
                    if userschoice == "2":
                        print("you decide to go left")
                        print("you are lost")
        if userschoice == "2":
            print("you decide to keep walking")
    if userschoice == "2":
        print("you decide to go left")
        print("you see a cat")
        userschoice = input("type 1 one chase it, type 2 to ignore it")
        if userschoice == "1":
            print("you decide to chase the cat")
            print("the cat takes you to a tunnel")
            userschoice = input("type 1 to follow the tunnel, type 2 to pet the cat")
            if userschoice == "1":
                print("you follow the tunnel...")
                print("it leads you to an empty room...strange")
                userschoice = input("type 1 to leave, type 2 to look around")
                if userschoice == "1":
                    print("you walk towards the exit but its closed...strange")
                    userschoice = input("type 1 to call someone, type 2 to try to dig your way out")
                    if userschoice == "1":
                        print("you try to call someone...")
                        print("someone picks up...")
                        print("they dont say anything...")
                        userschoice = input("type 1 to hang up, type 2 to ask for help")
                        if userschoice == "1":
                            print("you hang up...")
                            print("you are trapped")
                        if userschoice == "2":
                            print("you ask for help")
                            print("they end the call...")
                            print("you are trapped")
                    if userschoice == "2":
                        print("you try to dig your way out")
                        print("it doesnt work...")
                        print("you are trapped")
                if userschoice == "2":
                    print("you look around and notice the exit is closed...strange")
                    userschoice = input("type 1 to try to dig youur way out, type 2 to ask for help")
                    if userschoice == "1":
                        print("you try to dig your way out, it doesnt work...")
                        print("you are trapped")
                    if userschoice == "2":
                        print("you ask for help")
                        print("someone answers...")
                        userschoice = input("type 1 to ask them for help, type 2 to ask them how they got here")
                        if userschoice == "1":
                            print("you ask them for help...")
                            print("the door opens...")
                            userschoice = input("type 1 to leave, type 2 to ask them how they did they did that")
                            if userschoice == "1":
                                print("you leave the room...")
                                userschoice = input("type 1 to go right, type 2 to go left")
                                if userschoice == "1":
                                    print("you decide to go right")
                                    print("you are lost")
                                if userschoice == "2":
                                    print("you decide to go left")
                                    print("you see another door...")
                                    userschoice = input("type 1 to go inside, type 2 to ignore it")
                                    if userschoice == "1":
                                        print("you walk through the door...")
                                        print("it leads you outside")
                                        print("good job")
                                    if userschoice == "2":
                                        print("you choose to ignore the door")
                                        print("you keep walking and now you are lost")
                            if userschoice == "2":
                                print("you ask them how they oppened the door")
                                print("the door closes and they dissapear...strange")
                                print("you are trapped")
                            
                        if userschoice == "2":
                            print("you ask them how they got here")
                            print("they dissapear...")
                            print("you are trapped")
                    
        if userschoice == "2":
            print("'i wonder how it got here...' you keep walking")
            print("you hear something moving")
            userschoice = input("type 1 to follow the sound, type 2 to ignore it")
            if userschoice == "1":
                print("you follow the sound...")
                print("the sound leads you to an empty room")
                userschoice = input("type 1 to enter the room, type 2 to walk away")
                if userschoice
            if userschoice == "2":
                print("'its probably the cat from before...'")
                print("you keep walking")
                print("you found an exit")
                print("good job")
            
        


if userschoice == "2":
    print("you decide to check your phone")
    userschoice = input("type 1 to call someone, type 2 to explore")
    if userschoice == "1":
        print("you decide to call someone, no one picks up...")
        print("you decide to explore...")
        userschoice = input("type 1 to go right, type 2 to go left")
    if userschoice =="1":
        print("you decide to go right")
        print("you hear something moving")
        userschoice = input("type 1 to follow it, type 2 to ignore it")
        if userschoice == "1":
            print("you decide to follow the sound")
        if userschoice == "2":
            print("'its probably a bat...' you keep walking")
    if userschoice == "2":
        print("you decide to go left")
        print("you hear someones voice")
        userschoice = input("type 1 to follow it, type 2 to walk away, type 3 to talk to it")
        if userschoice == "1":
                print("you decide to follow the voice...")
                print("it leads you to an empty room...")
                userschoice = input("type 1 to speak, type 2 to leave and keep exploring")
                if userschoice == "1":
                    print("you speak to it but it doesnt respond")
                if userschoice == "2":
                    print("you keep exploring and hear the voice again")
                    userschoice = input("type 1 to speak to it, type 2 to be scared")
                    if userschoice == "1":
                        print("you try to speak to it, it doesnt respond...")
                    if userschoice == "2":
                        print("you are scared")
                        
        if userschoice == "2":
                print("'strange...'you walk away from the voice")
                print("you see a glowing light")
                userschoice = input("type 1 to follow it, type 2 to keep exploring")
                if userschoice == "1":
                    print("the light leads you to the exit")
                    print("good job!")
                if userschoice == "2":
                    print("you choose to ignore it...")
                    print("you kept walking and now you are lost")
                    userschoice = input("type 1 to be sad, type 2 to try to find a way out")
                    if userschoice == "1":
                        print("you choose to be sad but it doesnt help")
                        print("you are lost")
                    if userschoice == "2":
                        print("you try to find a way out")
                        print("it doesnt work")
        if userschoice == "3":
                print("you try to speak to it, it goes quiet")
                userschoice = input("type 1 to try again, type 2 to keep exploring")
                if userschoice == "1":
                    print("you try to speak to it again")
                    print("it doesnt respond")
                    userschoice = input("type 1 to try again, type 2 to explore")
                    if userschoice == "1":
                        print("you try to talk to it again...")
                        print("it doesnt respond")
                    if userschoice == "2":
                        print("you choose to go back to exploring...")
                        userschoice = input("type 1 to go right, type 2 to go left")
                        if userschoice == "1":
                            print("you decide to go right...")
                            print("you see a tunnel")
                            userschoice = input("type 1 to follow it, type 2 to keep walking")
                            if userschoice == "1":
                                print("you decide to go in the tunnel")
                            if userschoice == "2":
                                print("you decide to keep walking")
                        if userschoice == "2":
                            print("you decide to go left")
                            print("you see a person")
                            userschoice = input("type 1 to speak to them, type 2 to run")
                            if userschoice == "1":
                                print("you ask them how they got here")
                                print("they walk away...")
                                userschoice = input("type 1 to follow them, type 2 to walk away")
                                if userscchoice == "1":
                                    print("you decide to follow them...")
                                if userschoice == "2":
                                    print("you walk away...")
                                    userschoice = input("type 1 to wonder why there are lights, type 2 to explore")
                                    if userschoice == "1":
                                        print("'i wonder how the lights got here...strange'")
                                        userschoice = input("type 1 to go right, type 2 to go left")
                                        if userschoice == "1":
                                            print("you decide to go right")
                                            print("you are lost...")
                                            userschoice = input("type 1 to check your phone, type 2 to find a way out")
                                            if userschoice == "1":
                                                print("you decide to check your phone")
                                                userschoice = input("type 1 to call someone, type 2 to listen to spotify")
                                                if userschoice == "1":
                                                    print("someone picks up")
                                                    userschoice = input("type 1 to say hello, type 2 to end call")
                                                    if userschoice == "1":
                                                        print("you say hello, they dont respond...weird")
                                                        userschoice = input("type 1 to end call, type 2 to try again")
                                                        if userschoice == "1":
                                                            print("you end the call...")
                                                            print("you are still lost")
                                                        if userschoice == "2":
                                                            print("you try again...")
                                                            print("they dont respond, you end the call...")
                                                            userschoice = input("type 1 to find a way out, type 2 to ask for help")
                                                            if userschoice == "1":
                                                                print("you try to find a way out")
                                                                print("you are lost")
                                                            if userschoice == "2":
                                                                print("you decide to ask for help")
                                                                print("someone responds, but you dont see anyone...")
                                                                userschoice = input("type 1 to look for them, type 2 to ask them how to leave")
                                                                if userschoice == "1":
                                                                    print("you look for them but still dont see anything...")
                                                                    print("you try to speak to them again")
                                                                    print("no one responds")
                                                                    print("you are still lost")
                                                                if userschoice == "2":
                                                                    print("you ask them how to leave, they give you directions..")
                                                                    userschoice = input("type 1 to follow the directions, type 2 to stay still")
                                                                    if userschoice == "1":
                                                                        print("you follow the directions...")
                                                                        print("you find an exit")
                                                                    if userschoice == "2":
                                                                        print("you stay still but it doesnt help")
                                                                        print("you are lost")
                                                    if userschoice == "2":
                                                        print("you end the call...")
                                                        print("you are still lost")
                                                if userschoice == "2":
                                                    print("you listen to spotify but it doesnt help, you are still lost...")
                                            if userschoice == "2":
                                                print("you decide to find a way out")
                                                print("it doesnt work...")
                                                print("you are still lost")
                                        if userschoice == "2":
                                            print("you decide to go left")
                                            print("you are lost")
                                            
                if userschoice == "2":
                    print("you choose to keep exploring")
                    print("you are now lost")
