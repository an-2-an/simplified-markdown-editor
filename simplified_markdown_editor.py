FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
COMMANDS = ['!help', '!done']
MSG_UNKNOWN = 'Unknown formatting type or command'

def get_formatter():
    return input('Choose a formatter: ')

def show_help():
    text = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done'''
    print(text)

def main():
    while True:
        f = get_formatter()
        if f not in FORMATTERS + COMMANDS:
            print(MSG_UNKNOWN)
        else:
            if f == COMMANDS[1]:
                break
            if f == COMMANDS[0]:
                show_help()


if __name__ == '__main__':
    main()
