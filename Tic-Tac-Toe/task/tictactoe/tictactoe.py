text = input('Enter cells ').replace('_', ' ')
a = [[text[0], text[1], text[2]],
     [text[3], text[4], text[5]],
     [text[6], text[7], text[8]]
     ]
# per = 'X'
# print('---------')
# print('|', a[0][0], a[0][1], a[0][2], '|')
# print('|', a[1][0], a[1][1], a[1][2], '|')
# print('|', a[2][0], a[2][1], a[2][2], '|')
# print('---------')


def valid():
    per = 'X'

    if per == 'X':
        print('---------')
        print('|', a[0][0], a[0][1], a[0][2], '|')
        print('|', a[1][0], a[1][1], a[1][2], '|')
        print('|', a[2][0], a[2][1], a[2][2], '|')
        print('---------')
        while True:
            b = input('Enter the coordinates ').split()

            if len(b) != 2:
                print("You should enter numbers!")
            else:
                x, y = b[0], b[1]
                if str(x).isdigit() == False or str(y).isdigit() == False:
                    print("You should enter numbers!")
                elif int(x) <= 0 or int(x) > 3 or int(y) <= 0 or int(y) > 3:
                    print("Coordinates should be from 1 to 3!")
                # if X = 1
                elif x == '1':
                    if y == '1':
                        if a[2][0] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[2][0] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '2':
                        if a[1][0] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[1][0] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '3':
                        if a[0][0] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[0][0] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    # break
                # if X = 2
                elif x == '2':
                    if y == '1':
                        if a[2][1] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[2][1] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '2':
                        if a[1][1] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[1][1] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '3':
                        if a[0][1] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[0][1] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    # break
                # if X = 3
                elif x == '3':
                    if y == '1':
                        if a[2][2] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[2][2] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '2':
                        if a[1][2] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[1][2] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    if y == '3':
                        if a[0][2] != ' ':
                            print("This cell is occupied! Choose another one!")
                        else:
                            a[0][2] = per
                            break
                        # else:
                        #     print("This cell is occupied! Choose another one!")
                    # break

    print('---------')
    print('|', a[0][0], a[0][1], a[0][2], '|')
    print('|', a[1][0], a[1][1], a[1][2], '|')
    print('|', a[2][0], a[2][1], a[2][2], '|')
    print('---------')



def main():
    valid()


main()


# a = 0
# b = 0
#
# if text[0] == text[1] == text[2] and text[0] != '_':
#     if a == 0:
#         a = text[0]
#     else:
#         b = text[3]
# if text[3] == text[4] == text[5] and text[3] != '_':
#     if a == 0:
#         a = text[3]
#     else:
#         b = text[3]
# if text[6] == text[7] == text[8] and text[6] != '_':
#     if a == 0:
#         a = text[6]
#     else:
#         b = text[6]
# if text[0] == text[3] == text[6] and text[0] != '_':
#     if a == 0:
#         a = text[0]
#     else:
#         b = text[6]
# if text[1] == text[4] == text[7] and text[1] != '_':
#     if a == 0:
#         a = text[1]
#     else:
#         b = text[1]
# if text[2] == text[5] == text[8] and text[2] != '_':
#     if a == 0:
#         a = text[2]
#     else:
#         b = text[2]
# if text[0] == text[4] == text[8] and text[0] != '_':
#     if a == 0:
#         a = text[0]
#     else:
#         b = text[0]
# if text[2] == text[4] == text[6] and text[2] != '_':
#     if a == 0:
#         a = text[2]
#     else:
#         b = text[2]
#
# x_count = text.count('X')
# o_count = text.count('O')
# x_o = x_count - o_count
#
# if a != 0 and b == 0:
#     print(f"{a} wins")
# elif a != 0 and b != 0 or x_o > 1 or x_o < -1:
#     print('Impossible')
# elif a == 0 and b == 0 and '_' not in text:
#     print('Draw')
# elif '_' in text:
#     print("Game not finished")

# elements = input('Enter cells: ')
# straights =[elements[:3], elements[3:6], elements[6:], elements[0:9:3], elements[1:9:3], elements[2:9:3], elements[0:9:4],
# elements[2:7:2]]
# print('---------')
# print('|', ' '.join(elements[:3]), '|')
# print('|',' '.join(elements[3:6]),'|')
# print('|',' '.join(elements[6:]),'|')
# print('---------')
# if abs(elements.count('X') - elements.count('O')) > 1 or ('XXX' in straights and 'OOO' in straights):
#     print('Impossible')
# elif 'XXX' in straights:
#     print('X wins')
# elif 'OOO' in straights:
#     print('O wins')
# elif elements.count('_') > 0:
#     print('Game not finished')
# elif elements.count('_') == 0:
#     print('Draw')
