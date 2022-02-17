FORMATTERS = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
COMMANDS = ['!help', '!done']
MSG_UNKNOWN = 'Unknown formatting type or command'
content = []

def get_formatter():
    return input('Choose a formatter: ')

def show_help():
    text = '''Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line
Special commands: !help !done'''
    print(text)

def show_content():
    for line in content:
        print(line)

def formatting(formatter):
    # plain
    if formatter == FORMATTERS[0]:
        line = input('Text: ')
        content.append(line)
    # bold
    if formatter == FORMATTERS[1]:
        line = input('Text: ')
        content.append(f'**{line}**')
    # italic
    if formatter == FORMATTERS[2]:
        line = input('Text: ')
        content.append(f'*{line}*')
    # header
    if formatter == FORMATTERS[3]:
        level = int(input('Level: '))
        line = input('Text: ')
        content.append('#' * level + ' ' + line)
    # link [title](https://www.example.com)
    if formatter == FORMATTERS[4]:
        label = input('Label: ')
        link = input('URL: ')
        content.append(f'[{label}]({link})')
    # inline-code
    if formatter == FORMATTERS[5]:
        line = input('Text: ')
        content.append(f'`{line}`')
    # ordered-list
    pass
    # unordered-list
    pass
    # new-line
    if formatter == FORMATTERS[8]:
        content.append('')

    show_content()


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
            else:
                formatting(f)


if __name__ == '__main__':
    main()
