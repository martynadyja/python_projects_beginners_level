#Text-based Adventure Game

while True:
    answer = input("Do you like playing games? (yes or no) ")

    if answer.lower().strip() == "yes":
        answer = input("Welcome to the Jurassic Park. Would you like to see herbivorous dinosaurs or carnivorous dinosaurs? (herbivorous/carnivorous) ").lower().strip()
        if answer == "carnivorous":
            answer = input("You meet a T-rex that escaped from its cage. Would you like to run or hide under the car? (run/hide) ")
            if answer == "hide":
                print("It wasn't the greatest idea. The T-rex sniffed you out and ate you, you lost!")
            else:
                 print("Good choice, you ran away safely.")
                 answer = input("You see a Museum in the Park and a ship by the beach. What would you like to choose? (Museum/ship) ")
                 if answer ==  "Museum":
                     print("Unfortunately there were Velociraptors. They tore you to pieces... Game over.")
                 else:
                    print("You won! Someone on the ship noticed you and took you on board.")
        elif answer == "herbivorous":
             answer = input("You encounter a Diplodocus. Would you like to take a mini elevator to its ridge or feed the Diplodocus? (take mini elevator/feed) ")
             if answer == "take mini elevator":
                 print("You climbed on its ridge and admired the Park.")
                 answer = input("Unfortunately, the Diplodocus was attacked by a herd of Pterodactyls. Would you like to wait for them to fly away or slide down the Diplodocus tail? (wait/slide away) ")
                 if answer == "wait":
                     print("Good choice. Diplodocus turned out to be their friend. They apologized to him and flew away. You won!")
                 else:
                     print("When you have been sliding off the Diplodocus tail, you broke your legs. You went to the hospital. Try to win the game next time!")
             else:
                 print("Diplodocus accidentally bit off your hand and you cannot continue. Game over.")
        else:
            print("Invalid choice, you lost!")
    else:
        print("That's to bad!")
    break