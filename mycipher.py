shift = int(input('What is your cipher number? '))
text = input('What is your message? ')
output = ''
punctuation = ['!', '?', '.', ',', ';']
for items in text:
    if ('A' <= items <= 'Z'):
        overrun = ord(items) + shift
        if (overrun > 90):
            overrun = overrun - 26
        output += chr(overrun)
    elif ('a' <= items <= 'z'):
        overrun = ord(items) + shift
        if (overrun > 122):
            overrun = overrun - 26
        output += chr(overrun)
    elif (items in punctuation or items == ' '):
        pass
    else:
        output += chr(ord(items))
format_output = ''
cols = 0
rows = 0
for char in output:
    if cols == 5:
        format_output += ' '
        cols = 0
        rows += 1
    if rows == 10:
        format_output += '\n'
        rows = 0
    format_output += char
    cols += 1
print(format_output.upper())
                
   
