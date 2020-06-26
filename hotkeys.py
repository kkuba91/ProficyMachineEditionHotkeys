import signal

from pynput import mouse
from pynput.keyboard import Key, KeyCode, Listener, Controller
from pynput.mouse import Listener as MouseListener

#Exceptions from keybord system shortcuts:
#signal.signal(signal.SIGINT, signal_handler1)


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGSEGV, signal.SIG_IGN)
signal.signal(signal.SIGBREAK, signal.SIG_IGN)
signal.signal(signal.SIGTERM, signal.SIG_IGN)

# Your functions
keyboard = Controller()

def function_1():
        keyboard.type('NOCON')
        keyboard.type('\n')

def function_2():
        keyboard.type('NCCON')
        keyboard.type('\n')

def function_3():
        keyboard.type('COIL')
        keyboard.type('\n')

def function_4():
        keyboard.type('H_WIRE')
        keyboard.type('\n')

def function_5():
        keyboard.type('V_WIRE')
        keyboard.type('\n')

# Create a mapping of keys to function (use frozenset as sets are not hashable - so they can't be used as keys)
combination_to_function = {
    frozenset([Key.ctrl_l, Key.f2]): function_1, # NOCON
    frozenset([Key.ctrl_l, Key.f3]): function_2, # NCCON
    frozenset([Key.ctrl_l, Key.alt_l]): function_3, # COIL
    frozenset([Key.ctrl_l, Key.shift_l]): function_4, # h_wire
    frozenset([Key.ctrl_l, Key.f9]): function_5, # v_wire
}

# Currently pressed keys
current_keys = set()

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
        if frozenset(current_keys) in combination_to_function:
            # If the current set of keys are in the mapping, execute the function
            combination_to_function[frozenset(current_keys)]()
        current_keys.remove(key)

def on_click(x, y, button, pressed):
    if button == mouse.Button.middle:
        keyboard.type('\n')

with MouseListener(on_click=on_click) as listener:
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


