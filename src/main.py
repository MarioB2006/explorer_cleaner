import argparse
import os
import shutil

def main(p: str) -> None:
    if next(os.scandir(p), None) is None:
        print("Folder is empty")
    else:
        print(f"Files in this folder:\n")
        for i in os.listdir(p):
            print(f"{i}\n")
        user_input = input("Folder isnt empty, are you sure u want delete everything?\n")
        if user_input in ["y", "1", "yes"]:
            for i in os.listdir(p):
                full = os.path.join(p, i)
                if os.path.isfile(full):
                    os.remove(full)
                else:
                    shutil.rmtree(full)
        else:
            print("Folder will not be cleaned, end of task")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Folder to clean")
    args = parser.parse_args()
    main(args.path)
