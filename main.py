AlphaNum = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7, 'i' : 8, 'j' : 9, 'k' : 10, 'l' : 11, 'm' : 12, 'n' : 13, 'o' : 14, 'p' : 15, 'q' : 16, 'r' : 17, 's' : 18, 't' : 19, 'u' : 20, 'v' : 21, 'w' : 22, 'x' : 23, 'y' : 24, 'z' : 25, ' ' : 26, '.' : 27, ',' : 28, 'A' : 29, 'B' : 30, 'C' : 31, 'D' : 32, 'E' : 33, 'F' : 34, 'G' : 35, 'H' : 36, 'I' : 37, 'J' : 38, 'K' : 39, 'L' : 40, 'M' : 41, 'N' : 42, 'O' : 43, 'P' : 44, 'Q' : 45, 'R' : 46, 'S' : 47, 'T' : 48, 'U' : 49, 'V' : 50, 'W' : 51, 'X' : 52, 'Y' : 53, 'Z' : 54, '1' : 55, '2' : 56, '3' : 57, '4' : 58, '5' : 59, '6' : 60, '7' : 61, '8' : 62, '9' : 63, '0' : 64, '-' : 65, '/' : 66}

numToLetter = {"a": 13, "b": 49, "c": 2, "d": 62, "e": 47, "f": 10, "g": 15, "h": 55, "i": 24, "j": 56, "k": 59, "l": 34, "m": 61, "n": 54, "o": 60, "p": 4, "q": 42, "r": 30, "s": 58, "t": 21, "u": 5, "v": 57, "w": 23, "x": 48, "y": 65, "z": 20, ".": 26, " ": 27, ',' : 12, 'A' : 64, 'B' : 51, 'C' : 35, 'D' : 31, 'E' : 43, 'F' : 50, 'G' : 44, 'H' : 38, 'I' : 8, 'J' : 9, 'K' : 53, 'L' : 16, 'M' : 29, 'N' : 45, 'O' : 32, 'P' : 3, 'Q' : 11, 'R' : 41, 'S' : 39, 'T' : 46, 'U' : 0, 'V' : 33, 'W' : 63, 'X' : 14, 'Y' : 28, 'Z' : 40, '1' : 7, '2' : 22, '3' : 37, '4' : 19, '5' : 18, '6' : 1, '7' : 17, '8' : 6, '9' : 52, '0' : 36, '-' : 25, '/' : 66}

def encryptMIT(msgs):
    for dat in date:
        CipherText5 = AlphaNum[dat]
        CipherText6 = inverseNumToLetter[CipherText5]
        CipherText7 = rev_str(CipherText6)
        i = open("isaiah_log.txt", "a+")
        i.write(CipherText7)
    i.write('//')
    for msg in msgs:
        CipherText1 = AlphaNum[msg]
        CipherText2 = inverseNumToLetter[CipherText1]
        CipherText3 = rev_str(CipherText2)
        i.write(CipherText3)
    i.write('\n')
    i.close()

def encryptHARVARD(msgs):
    for msg in msgs:
        CipherText1 = AlphaNum[msg]
        CipherText2 = inverseNumToLetter[CipherText1]
        CipherText3 = rev_str(CipherText2)
        i = open("resume.txt", "a+")
        i.write(CipherText3)
    i.write('\n')
    i.close()

def encryptDARTMOUTH(msgs):
    for msg in msgs:
        CipherText1 = AlphaNum[msg]
        CipherText2 = inverseNumToLetter[CipherText1]
        CipherText3 = rev_str(CipherText2)
        i = open("essay_ideas.txt", "a+")
        i.write(CipherText3)
    i.write('\n')
    i.close()

def decryptMIT(smth):
    org_msg = open('isaiah_log.txt', 'r')
    Ct = org_msg.read()          
    for x in Ct:
        if x == '\n':
            l.append('\n')
    
        else:
            rev_msg = rev_str(x)
            msg = numToLetter[rev_msg]
            CipherText4 = inverseAlphaNum[msg]
            l.append(CipherText4)
            message_final = ''.join(l)
    print(message_final)
    org_msg.close()

def decryptHARVARD(smth):
    org_msg = open('resume.txt', 'r')
    Ct = org_msg.read()          
    for x in Ct:
        if x == '\n':
            l.append('\n')
    
        else:
            rev_msg = rev_str(x)
            msg = numToLetter[rev_msg]
            CipherText4 = inverseAlphaNum[msg]
            l.append(CipherText4)
            message_final = ''.join(l)
    print(message_final)
    org_msg.close()

def decryptDARTMOUTH(smth):
    org_msg = open('essay_ideas.txt', 'r')
    Ct = org_msg.read()          
    for x in Ct:
        if x == '\n':
            l.append('\n')
    
        else:
            rev_msg = rev_str(x)
            msg = numToLetter[rev_msg]
            CipherText4 = inverseAlphaNum[msg]
            l.append(CipherText4)
            message_final = ''.join(l)
    print(message_final)
    org_msg.close()


inverseNumToLetter = {v: k for k, v in numToLetter.items()}
inverseAlphaNum = {v: k for k, v in AlphaNum.items()}

import datetime
date_object = datetime.date.today()
print(date_object)
date = str(date_object)

def rev_str(s):
    return s[::-1]

l = []

password = input('Password:')

if password == 'communist':
    print('password accepted')
    q = input('Future:')
    if q == 'MIT':
        print('authentication accepted')
        print('Welcome, Isaiah')
        command = input('read or write:')
        if command == 'write':
            encryptMIT(input('LOG:'))
        elif command == 'read':
             decryptMIT('isaiah_log.txt')
        else:
             print('unexpected command, try again')
    elif q == 'HARVARD':
        print('authentication accepted')
        print('Welcome, Isaiah')
        command = input('read or write:')
        if command == 'write':
            encryptHARVARD(input('RESUME:'))
        elif command == 'read':
             decryptHARVARD('resume.txt')
        else:
            print('unexpected command, try again')
    elif q == 'DARTMOUTH':
        print('authentication accepted')
        print('Welcome, Isaiah')
        command = input('read or write:')
        if command == 'write':
            encryptDARTMOUTH(input('IDEA:'))
        elif command == 'read':
             decryptDARTMOUTH('quotes.txt')
        else:
          print('unexpected command, try again')
    else:
        print('leave, you sit on a throne of lies.')
else:
  print('wrong password, try again')
