import string as s

class PlayFair:
    def __init__(self):
        # 1st row missing chars [A, J, W, I]
        # 2nd row missing chars [E, F, J, T, V, Y]
        # 3rd row missing chars [P, T, X]
        # 4th row missing chars [D, J, M, N, T, W, Y, Z]
        # 5th row missing chars [O, R, S, W, X]
        # 5th row missing chars [C, F, J, T]
        self.text = ['VUDGHVBBONOVZRKHNIBDLNCVGRPDEXZEVMGKSVBTLIFGITQQO',
                     'BZBLARLZDLHBURHARLCPIBIZMKQBGXAIMRPNOLWHMCSQ',
                     'RLZMKUGADGHIQONJDHFMKERLWYDGWVGLBSKQBHCUNUQE',
                     'ICSOQRRSPBIKRSIEQOGHHAAPLBVGKXAFGFUSVIILKREG',
                     'TDHABADKVPUZNAGQHVCFHJHDBFYEULITMYHQEIMNGKGU',
                     'SQKBDYKLMKANURGKGNWYYOOENRIINVXUHPARKKZEHBAE'
                    ]

        self.grids = None

    def fillGrid(self, key, removed_letter='X'):
        grids = [[],[]]

        # Fills the list of values
        for i in range(25):
            grids[0].append(i+1)

        # Fills the first squares of the grid with the key
        for letter in key:
            if letter not in grids[1]:
                grids[1].append(letter)

        # Fills the rest of the grid with alphabetical characters that aren't in the key
        for i, letter in enumerate(s.ascii_uppercase):
            if len(grids[1]) > 24:
                self.grids.append(grids[1])
                break

            if letter not in grids[1] and letter != removed_letter:
                grids[1].append(s.ascii_uppercase[i])

    def encryptPlayfair(self):
        pass

    def decryptPlayfair(self):

        #----#----#----#----#----#
        # 1  # 2  # 3  # 4  # 5  #
        #----#----#----#----#----#
        # 6  # 7  # 8  # 9  # 10 #
        #----#----#----#----#----#
        # 11 # 12 # 13 # 14 # 15 #
        #----#----#----#----#----#
        # 16 # 17 # 18 # 19 # 20 #
        #----#----#----#----#----#
        # 21 # 22 # 23 # 24 # 25 #
        #----#----#----#----#----#

        encrypted_text = self.text[0]

        if len(encrypted_text) % 2 != 0:
            encrypted_text += f'{encrypted_text[len(encrypted_text)-1]}'

        decrypted_text = ''

        pair_index = 0
        while pair_index < range(len(encrypted_text)):
            encrypted_pair = '' + encrypted_text[pair_index] + encrypted_text[pair_index + 1]
            encrypted_values = self.letterToValue(encrypted_pair)
            decrypted_pair = self.decrypt(encrypted_values)
            decrypted_text.append(decrypted_pair)
            pair_index += 2

    def letterToValue(self, encrypted_pair):
        index_X = self.grids[1].index(encrypted_pair[0])
        index_Y = self.grids[1].index(encrypted_pair[1])

        return [self.grids[index_X], self.grids[index_Y]]

    def decrypt(self, encrypted_values):
        X = encrypted_values[0]
        Y = encrypted_values[1]

        X_Y_swap = False

        if X > Y:
            temp = X
            X = Y
            Y = temp
            X_Y_swap = True

        left_edge = [1, 6, 11, 16, 21]
        top_edge  = [1, 2, 3,  4,  5]

        # Check if letters are in the same row
        if (X-1) // 5 == (Y-1) // 5:
            if X in left_edge:
                X = X + 4
            else:
                X = X - 1

            if Y in left_edge:
                Y = Y + 4
            else:
                Y = Y - 1

        # Check if letters are in the same column
        elif Y % 5 == X % 5:
            if X in top_edge:
                X = X + 20
            else:
                X = X - 5

            if Y in top_edge:
                Y = Y + 20
            else:
                Y = Y - 5

        # Check if letters are the opposite corners of a box
        else:
            for j in range(1, 5):
                for i in range(1, 5):
                    if (X % 5 == 0) or (X % 5 > Y % 5 and Y % 5 != 0):
                        if Y == (X - j) + (i * 5):
                            X -= j
                            Y += j
                    else:
                        if Y == (X + j) + i * 5:
                            X += j
                            Y -= j

        if X_Y_swap:
            print(f'{Y}, {X}') # Debug purposes
            return [Y, X]

        print(f'{X}, {Y}') # Debug purposes
        return [X, Y]

