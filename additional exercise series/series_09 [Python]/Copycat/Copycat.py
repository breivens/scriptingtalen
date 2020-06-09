def copycat(source: str, destination: str):
    ins, out = open(source, "r"), open(destination, "a")
    print(ins.read(), file=out, end="")
    ins.close(), out.close()


def copycat_shortened(source: str, destination: str):
    with open(source, 'r') as ins, open(destination, 'a') as out:
        out.write(ins.read())


def copycat_with_shutil(source: str, destination: str):
    from shutil import copy2
    copy2(source, destination)


copycat('original.txt', 'copy.txt')
