from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        print(key)

def run():
    # Collect events until released
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    run()