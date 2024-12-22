from pynput import keyboard, mouse

# Create a mouse controller
mouse_controller = mouse.Controller()

def on_press(key):
    try:
        # Check if the key pressed corresponds to \x03
        if (hasattr(key, 'char') and key.char == '\x03') or (key == keyboard.Key.enter):
            # Simulate a left mouse button click
            mouse_controller.click(mouse.Button.left, 1)
            print("Giant Enter key (\x03) pressed - Simulating mouse click")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop listener on specific key combination, e.g., Esc
    if key == keyboard.Key.esc:
        print("Exiting...")
        return False

# Start listening to keyboard inputs
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
