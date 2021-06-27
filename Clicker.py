from pynput.mouse import Button, Listener, Controller
from threading import Timer

print("Started")

el = 0

mouse = Controller()

while True:

    def on_click(x, y, button, pressed):
        global el
        if str(button) == "Button.middle" and pressed == True:
            el += 1
            return False
      

    with Listener(on_click=on_click) as l:
        Timer(0.0001, l.stop).start()
        l.join()

    if el%2 == 1:
        mouse.click(Button.left, 1) # Switch "Button.left" to "Button.right" to switch the mouse button.