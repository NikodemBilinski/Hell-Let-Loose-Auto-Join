import pyautogui
import keyboard
import time


Fullhd_join_x = 1334
Fullhd_join_y = 389

Fullhd_cancel_x = 1079
Fullhd_cancel_y = 609

join_color = (121,117,99) 
cancel_color = (116,113,96)

Quadhd_join_x = 1761
Quadhd_join_y = 519

Quadhd_cancel_x = 1502
Quadhd_cancel_y = 810

# Debugging, there is something wrong with matching color, it only works when i move around the button, when i stop it doesnt print good dunno why
# I guess i will stay for now with just clicking without checking the color

# while(not keyboard.is_pressed("p")):
#     time.sleep(1)
#     x , y = pyautogui.position()
#     if(pyautogui.pixel(x,y) == (224,207,126) or pyautogui.pixel(x,y) == (250,231,141)):
#         print("good")

# while(not keyboard.is_pressed("p")):
#     time.sleep(1)
#     x,y = pyautogui.position()
#     print(pyautogui.position())
#     print( pyautogui.pixel(x,y))

def Program_ForOlderVersion():
    print("\n Hell Let Loose AutoJoin Color Matching\n")
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
                x,y = pyautogui.position()
                if(pyautogui.pixel(x,y) == (join_color)):
                    pyautogui.click()

                time.sleep(5)

                pyautogui.moveTo(Fullhd_cancel_x,Fullhd_cancel_y)
                x,y = pyautogui.position()
                if(pyautogui.pixel(x,y) == (cancel_color)):
                    pyautogui.click()
                
                time.sleep(0.2)
            print("Program was stopped")

        case "b":
            print("Delay started")
            time.sleep(10)
            while(not keyboard.is_pressed("p")):
                pyautogui.moveTo(Quadhd_join_x,Quadhd_join_y)
                x,y = pyautogui.position()
                if(pyautogui.pixel(x,y) == (join_color)):
                    pyautogui.click()

                time.sleep(5)

                pyautogui.moveTo(Quadhd_cancel_x,Quadhd_cancel_y)
                x,y = pyautogui.position()
                if(pyautogui.pixel(x,y) == (cancel_color)):
                    pyautogui.click()
                    
                time.sleep(0.2)
            print("Program was stopped")

        case _:
            #code for default
            print("Write correct one dumbass")

def Program_ForNewerVersion():
    print("\n Hell Let Loose AutoJoin Just Clicking\n")
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

                time.sleep(0.2)

            print("Program was stopped")

        case "b":
            print("Delay started")
            time.sleep(10)
            while(not keyboard.is_pressed("p")):

                pyautogui.moveTo(Quadhd_join_x,Quadhd_join_y)
                pyautogui.click()

                time.sleep(5)

                pyautogui.moveTo(Quadhd_cancel_x,Quadhd_cancel_y)
                pyautogui.click()

                time.sleep(0.2)

            print("Program was stopped")

        case _:
            #code for default
            print("Write correct one dumbass")

    
print("\nChoose version of the code to use (if you have newer python color matching might not work)\n")
print("a) Color Matching: (safe to leave unwatched, the program won't click anything besides the join and cancel button")
print("b) Just  Clicking: (unsafe to leave unwatched, but it should be working on new python versions)")

result = input()

if(result == "a"):
    Program_ForOlderVersion()
if(result == "b"):
    Program_ForNewerVersion()


