import os

from past.builtins import execfile

if __name__ == "__main__":
    success = False

    while not success:
        filename = input("Enter project id ")

        if os.path.exists(f"projects/{filename}.py"):
            success = True
            execfile(f"projects/{filename}.py")

        else:
            print(f"File projects/{filename}.py not found!")
            success = False


