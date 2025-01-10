import machine

from sensors import main

main()

if __name__ == '__main__':
    try:
        main()
    except:
        machine.restart()
