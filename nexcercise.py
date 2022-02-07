import os
import time

NEXT_POSE_IN_MINUTE = 60

def main():
    os.system("say Lets get started!!!")
    with open("poses.txt") as file:
        poses = file.readlines()
        for pose in poses:
            print(pose)
            os.system("say " + pose)
            time.sleep(NEXT_POSE_IN_MINUTE)
        os.system("say Take a rest")


if __name__ == '__main__':
    main()
