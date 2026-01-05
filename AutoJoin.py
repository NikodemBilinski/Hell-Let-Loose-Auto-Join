import pyautogui
import keyboard
import time


Fullhd_join_x = 1334
Fullhd_join_y = 389

Fullhd_cancel_x = 1100
Fullhd_cancel_y = 609

#Quadhd_x =
#Quadhd_y =


# Debugging, there is something wrong with matching color, it only works when i move around the button, when i stop it doesnt print good dunno why
# I guess i will stay for now with just clicking without checking the color

# while(not keyboard.is_pressed("p")):
#     time.sleep(1)
#     x , y = pyautogui.position()
#     if(pyautogui.pixel(x,y) == (224,207,126) or pyautogui.pixel(x,y) == (250,231,141)):
#         print("good")
                

def Program():

    print("Hell Let Loose has to be full screen or borderless for autoclick to work")
    print("Select the server that you want to join and choose correct resolution")
    print("When you select the resolution there will be a 10s delay before the program begins for users that have only one monitor")
    print("Hold button 'p' for a few seconds to stop the program\n\n")
    print("What resolution do you have?")
    print("a) 1920x1080")
    print("b) 2560x1440")

    result = input()

    match result:
        case "a":

            print("Delay started")
            time.sleep(10)
            while(not keyboard.is_pressed("p")):

                pyautogui.moveTo(Fullhd_join_x,Fullhd_join_y)
                pyautogui.click()

                time.sleep(5)

                pyautogui.moveTo(Fullhd_cancel_x,Fullhd_cancel_y)
                pyautogui.click()

                time.sleep(5)

            print("Program was stopped")

        case "b":
            #code for b
            print("not done yet")

        case _:
            #code for default
            print("Write correct one dumbass")

    
Program()




