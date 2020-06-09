chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?!.-()<>%$',:other/\\"
chars180 = "ɐqɔpǝɟƃɥᴉɾʞ˥ɯuodbɹsʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀΌɹS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86 ¿¡˙-)(><%$,':‾\\/"


def for_loop():
    text = ""
    for _ in range(int(input())):
        for char in input():
            text += chars180[chars.index(char)]
        text += "\n"
    print(text.strip()[::-1])


def gen_n_join():
    for line in [input()[::-1] for _ in range(int(input()))][::-1]:
        print("".join(chars180[chars.index(char)] for char in line))


def gen_n_trans():
    for line in [input()[::-1] for _ in range(int(input()))][::-1]:
        print(line.translate(str.maketrans(chars, chars180)))
