from PIL import Image

char_set = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''

im = Image.open('E:\Git-Files\Python\MiddleLevel\qq.png')
im = im.resize((80, 50), Image.ANTIALIAS)
im = im.convert('L')
# im.save('E:\Git-Files\Python\MiddleLevel\t.jpeg')

def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray/((256.0 + 1) / len(char_set)))]

text = ''
for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j, i))
        if isinstance(gray, tuple):
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])

        text += get_char(gray)
    text += '\n'

with open('E:\Git-Files\Python\MiddleLevel\pic.txt', 'w')as f:
    f.write(text)