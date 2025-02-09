# Creating an Automatic car operation program
# Importing the libraries that are needed
import time
print("\n\n\t\t\t\t\t<--------🙏🏻 WELCOME TO AUTOMATIC CAR XTESLA 🙏🏻-------->") # Banner Message @Tesla CyberTruct
class Car:
    def __init__(self):
        self.name = "CyBeR_TrUcK"

    def auth_key(self):
        time.sleep(1)
        k = ["?Tesla"]
        for i in range(0, 4):
            self.user_key = input("Enter your key: ")
            self.check = self.user_key in k
            if self.check: # Checking that if check is true then it will print the message !
                time.sleep(1)
                print(f"\n\n\t\t\t\t\t✅ Provided key -> {self.name} (verified) !\n")
                break
            else: # Other wise it will terminate from the program and print this statement !!
                time.sleep(1)
                print("🚫 Wrong key provided\n")
                pass

    def Engine_started(self): # Engine started message are showing !!
        self.l = ["pes university","electronic city","jpnagar","orien mall","gopalan mall","hosker ali road","white field"]
        if self.check:
            time.sleep(1)
            print("\n\n\t\t\t\t\t  <-------- CAR ENGINE STARTED -------->\n") # Displaying the message about the 
            self.location = input("Enter your location: ").lower().strip()
            time.sleep(0.5) # Shorter time to be taken !
            if self.location in self.l:
                time.sleep(0.5)
                print(f"\n\n\t\t\t\t 📍 Your location {self.location} has been set, all set to go ✅\n\n")
            else:
                time.sleep(0.5)
                print("\n\n\t\t\t\t\t🚫 Sorry this location is not there in my database as per now\n")
                return

class Control(Car): # Inheritance concept !!
    def __init__(self): # All the controls in the car by the system is provided !!
        super().__init__()
    def animation(self):
        print("\n\n\t\t\t\t\t<-------- DISPLAYNG THE SYSTEM STATUS -------->\n")
        self.li = ["✅ Car system check", "✅ Engine started", "✅ Destination set in map", "✅ All action checked and ready to move"]
        if self.location in self.l:
            for i in self.li:
                time.sleep(1)
                print(f"{i}\n")
        print("\n\n\t\t<--------🚀 YOUR TESLA IS ON THE WAY TO YOUR DESTINATION PLEASE APPLY YOUR SEAT BELT -------->\n\n") # Displaying the message that your tesla is started and moving to your destination
        

    def music(self): # Taking the input from the user about that we should play the music or not
        music_choice = input("Do you want me to start your music playlist ? (y/n): ").lower() # Asking from the user !!
        if(music_choice == 'y'):
            time.sleep(1)
            print("\n\n\t\t\t\t\t<-------- 🎵🎧 PLAYING MUSIC (Volume 50%) -------->\n") # Displaying the True value
        else:
            time.sleep(1)
            print("\n\n\t\t\t\t\t<-------- ✅ THANKYOU FOR YOUR CHOICE -------->\n") # For the faise value

    def destination(self): # This is the destination method where the informations about the destination are provided
        time.sleep(1)
        print("\n\n\t\t\t\t<-------- 🚗 WE ARE JUST 5 MINUTES AWAY FROM THE DESTINATION -------->\n\n")
        for i in range(5 , -1 , -1):
            time.sleep(2)
            print(f"🔷 {i} minute remaining\n")
        time.sleep(0.5)
        print("\n\n\t\t\t\t<-------- 📍 ARRIVED YOUR DESTINATION -------->\n")
        time.sleep(0.5)
        print("\n\n\t\t\t<--------🙏🏻 THANKYOUR FOR TRAVELLING IN TESLA CYBERTRUCK 🙏🏻-------->\n")


# Object calling for the above class methods
obj = Control(); obj.auth_key(); obj.Engine_started(); obj.animation(); obj.music(); obj.destination()