from mover.mover import FileMover
from plyer import notification
import time 


if __name__ == "__main__":
    move = FileMover()
    while True:
        time.sleep(10)
        notification.notify(
            title="*** File moving start ***",
            message="File is moving now wait for next notification",
            timeout=5
        )
        move.moving()
        notification.notify(
            title="*** File Moving End ***",
            message="File is moved now",
            timeout=3
        )
        time.sleep(10)
