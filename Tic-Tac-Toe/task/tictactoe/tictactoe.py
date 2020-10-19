text = input()
print('---------')
for _ in range(0, 9, 3):
    print(f'| {text[_]} {text[_ + 1]} {text[_ + 2]} |')
print('---------')

a = 0
b = 0

if text[0] == text[1] == text[2] and text[0] != '_':
    if a == 0:
        a = text[0]
    else:
        b = text[3]
if text[3] == text[4] == text[5] and text[3] != '_':
    if a == 0:
        a = text[3]
    else:
        b = text[3]
if text[6] == text[7] == text[8] and text[6] != '_':
    if a == 0:
        a = text[6]
    else:
        b = text[6]
if text[0] == text[3] == text[6] and text[0] != '_':
    if a == 0:
        a = text[0]
    else:
        b = text[6]
if text[1] == text[4] == text[7] and text[1] != '_':
    if a == 0:
        a = text[1]
    else:
        b = text[1]
if text[2] == text[5] == text[8] and text[2] != '_':
    if a == 0:
        a = text[2]
    else:
        b = text[2]
if text[0] == text[4] == text[8] and text[0] != '_':
    if a == 0:
        a = text[0]
    else:
        b = text[0]
if text[2] == text[4] == text[6] and text[2] != '_':
    if a == 0:
        a = text[2]
    else:
        b = text[2]

x_count = text.count('X')
o_count = text.count('O')
x_o = x_count - o_count

if a != 0 and b == 0:
    print(f"{a} wins")
elif a != 0 and b != 0 or x_o > 1 or x_o < -1:
    print('Impossible')
elif a == 0 and b == 0 and '_' not in text:
    print('Draw')
elif '_' in text:
    print("Game not finished")
