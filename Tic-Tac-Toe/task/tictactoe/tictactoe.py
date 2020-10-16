text = input()
print('---------')
for _ in range(0, 9, 3):
    print(f'| {text[_]} {text[_ + 1]} {text[_ + 2]} |')
print('---------')
