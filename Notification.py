from pynotifier import Notification
import time
what = input("what would you want to be notified about")
test = int(input("in how long do you want to be notified - time in seconds"))
time.sleep(test)


def notify():
    Notification(
        title='Notification',
        description=what,
        icon_path='/absolute/path/to/image/icon.png',
        duration=5,  # Duration in seconds
        urgency='normal'
    ).send()
notify()