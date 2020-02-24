import os
import time

from past.builtins import execfile

if __name__ == "__main__":
    success = False

    while not success:
        filename = input("Enter project id ")

        if os.path.exists(f"projects/{filename}.py"):
            success = True

            print()

            # time the code
            timer = time.time()

            execfile(f"projects/{filename}.py")

            print(f"\ntook {round(time.time() - timer, 5)} seconds")

        else:
            print(f"File projects/{filename}.py not found!")
            success = False
