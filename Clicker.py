from pynput.mouse import Button, Listener, Controller
from threading import Timer

print("Started")

var = 0

mouse = Controller()

while True:

    def on_click(x, y, button, pressed):
        global var
        if str(button) == "Button.middle" and pressed == True: # Change what str(button) equals to change what pauses the clicker.
            var += 1
            return False
      

    with Listener(on_click=on_click) as l:
        Timer(0.0001, l.stop).start() # Change the first number to switch how fast it clicks.
        l.join()

    if var%2 == 1:
        mouse.click(Button.left, 1) # Switch "Button.left" to "Button.right" to switch the mouse button.
