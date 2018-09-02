import os


def main():
    with open('test2.lrc', "r") as f:
        print(1)
        lrc = f.read()
    print(len(lrc))
    print(type(lrc))
    lrc_now = lrc

    with open('test_new.lrc', "w",encoding='utf-8') as f:
        f.write(lrc_now)

if __name__ == "__main__":
    main()
