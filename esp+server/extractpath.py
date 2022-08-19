import time


def run():
    while True:
        f = open("path.txt", "r")
        print(f.readline())
        d = f.read().splitlines()
        exit1 = d[0].split(',')
        exit2 = d[1].split(',')
        if(exit1[1] < exit2[1]):

            exit_path = exit1[2]
        else:
            exit_path = exit2[2]

        print(exit_path)
        f.close()
        fp = open("path_final.txt", "w")
        fp.write(exit_path)
        time.sleep(2)
