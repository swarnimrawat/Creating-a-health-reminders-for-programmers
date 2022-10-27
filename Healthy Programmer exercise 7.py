from pygame import mixer
from time import time
from time import sleep

def getdate():
    import datetime
    return (str(datetime.datetime.now()))

def musicloop(stopper):
    mixer.init()
    mixer.music.load("music.mp3")

    mixer.music.play()
    while True:
        x = input("Please type STOP to stop the alarm or exit to stop the program : ")

        if (x.upper() == stopper):
            print("\n Great! Now lets get back to work:)\n")
            mixer.music.stop()
            return True
            break

        elif (x.upper() == "EXIT"):
            return False

total_water = 0
total_phy_exercises = 0
total_eye_exercises = 0
if __name__ == '__main__':
    print("\n\t\t\t\tHey Programmer! This is your Health-Clock to make youself healthy \n")
    time_phy = time()
    time_drink = time()
    time_eyes = time()

    eyes_delay = 10
    drink_delay = 20
    phy_delay = 35

    while(True):
        #drink water condition
        if (time() - time_drink > drink_delay):
            print("Hey! Please drink some water (at least 200 ml).")

            #checking the user input so that music
            #can be stopped
            if (musicloop("STOP")):
                pass
            else:
                break
            #reinitializing the variable
            time_drink = time()
            #incrementing the value
            total_water += 200

            # opening the file and putting the data
            # into the file
            f = open("drank.txt", "at")
            f.write("[" + getdate() + "] \n")
            f.close()
        # eye exercise condition

        if (time() - time_eyes > eyes_delay):
            print("Hey! PLease do an Eye exercise,"
                  "If you dont know how to do it just search eye exercise in the youtube dont be lazy:) ")
            if (musicloop("STOP")):
                pass
            else:
                break

            time_eyes = time()
            total_eye_exercises += 1
            f = open("phy_exer.txt", "at")
            f.write("[" + getdate()+ "] \n")
            f.close()
       #eye exercise done
        if (time() - time_phy > phy_delay):
            print("Hey Please do a Physical Exercise")
            if (musicloop("STOP")):
                pass
            else:
                break
            time_phy = time()
            total_phy_exercises +=1
            f = open ("pjy_exer.txt", "at")
            f.write("[" + getdate() + "]\n")
    print()
    print(f"Total water taken today : {total_water}.")
    try:
        f = open("drank.txt", "rt")
        print("\nDetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found")
    print(f"Total eye exercise done todya :{total_eye_exercises}.")
    try:
        f = open("eye.txt", "rt")
        print("\ndetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found!")
    print(f"Total physical exercises done today : {total_phy_exercises}.")

    try:
        f = open("phy_exer.txt", "rt")
        print("\ndetails :")
        print(f.read())
        f.close()
    except:
        print("Details not found")

    sleep(5)