import requests

from pynput import keyboard

KEYS_INTERESTED = "wasdqe"


def sendKey(address, key):
    data = {"key": key}
    print(data)
    requests.post(address, data={"key": key}, timeout=1.0)

def keyDown(key):
    return f"KEY DOWN: {key}"

def keyUp(key):
    return f"KEY UP: {key}"

def _onPress(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in KEYS_INTERESTED:
        print(f"sending keydown {k}")
        sendKey("http://localhost:7000", keyDown(k))

    return True


def _onRelease(key):
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys

    if k in KEYS_INTERESTED:

        print(f"sending keyup {k}")
        sendKey("http://localhost:7000", keyUp(k))

    return True


listener = keyboard.Listener(on_press=_onPress, on_release=_onRelease)
listener.start()
listener.join()
