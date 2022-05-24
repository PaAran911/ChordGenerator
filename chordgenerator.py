import random
import musicalbeeps

dic = {-11:"C3",-10:"C3#",-9:"D3",-8:"D3#",
       -7:"E3",-6:"F3",-5:"F3#",-4:"G3",-3:"G3#",
       -2:"A3",-1:"A3#",0:"B3",1:"C4",2:"C4#",3:"D4",
       4:"D4#",5:"E4",6:"F4",7:"F4#",8:"G4",9:"G4#",
       10:"A4",11:"A4#",12:"B4",13:"C5",14:"C5#",15:"D5",
       16:"D5#",17:"E5",18:"F5",19:"F5#",20:"G5",21:"G5#",
       22:"A5",23:"A5#",24:"B5",25:"C6"}
major = [2,2,1,2,2,2,1]
dic_keys = list(dic.keys())
dic_values = list(dic.values())

chordn = int(input("How many chords do you want?: "))
lst = [[0,0,0,0] for count in range(chordn)]
progress = [[0,0,0,0] for count in range(chordn-1)]
gap = [[0,0,0,0,0,0] for count in range(chordn)]
notes_lst = [] #notes from the key go here
chordone = [[] for count in range(3)]


def key_setting(lst_here):
    key = dic_keys[dic_values.index(input("What key do you want to be in? (type in C3~B3): "))]
    print()
    notes = key
    while notes <= max(dic_keys):
        for i in major:
            lst_here.append(notes)
            notes += i
            if notes > max(dic_keys):
                return key

def genChord(chordNum):
    for i in range(4):
            lst[chordNum][i] = random.choice(notes_lst)

def sameNote(chordNum):
    for x in range(4):
        for y in range(x+1,4):
            if lst[chordNum][x] == lst[chordNum][y]:
                return True
    return False

def genFirstChord(key):
    for i in range(key, 26, 12):
        chordone[0].append(i)
    for i in range(key+4, 26, 12):
        chordone[1].append(i)
    for i in range(key+7, 26, 12):
        chordone[2].append(i)

    for i in range(3):
        lst[0][i] = random.choice(chordone[i])
    
    while True:
        lst[0][3] = random.choice(chordone[random.choice([0, 1, 2])])
        if not sameNote(0):
            break
    lst[0].sort()

def unstableInt(chordNum):
    for x in range(4):
        for y in range(x+1,4):
            if lst[chordNum][x]-lst[chordNum][y] == 6 or lst[chordNum][x]-lst[chordNum][y] == 18 or lst[chordNum][x]-lst[chordNum][y] == 30:
                return True
    return False

def gapNotes(chordNum):
    if  24 >= lst[chordNum][3]-lst[chordNum][0] >= 10:
        return True
    else:
        return False

def printChord():
    for j in range(chordn):
        for i in range(4):
            print(dic[(lst[j][i])], end=' ')
        print()

def getProgress():
    for i in range(chordn-1):
        for j in range(4):
            progress[i][j] = lst[i+1][j] - lst[i][j]

def getGap():
    for a in range(chordn):
        gap[a][0] = lst[a][1] - lst[a][0]
        gap[a][1] = lst[a][2] - lst[a][0]
        gap[a][2] = lst[a][3] - lst[a][0]
        gap[a][3] = lst[a][2] - lst[a][1]
        gap[a][4] = lst[a][3] - lst[a][1]
        gap[a][5] = lst[a][3] - lst[a][2]

def byeong(chordNum): #병행 1, 5, 8도
    for j in range(6):
        if (gap[chordNum-1][j] in [0, 12, 24, 36] and gap[chordNum][j] in [0, 12, 24, 36]) or (gap[chordNum-1][j] in [7, 19, 31] and gap[chordNum][j] in [7, 19, 31]):
            return True

def eunbok(chordNum): #은복 5, 8도
    if (progress[chordNum-1][0] * progress[chordNum-1][3] > 0) or (progress[chordNum-1][0] * progress[chordNum-1][3] == 0 and progress[chordNum-1][0] + progress[chordNum-1][3] == 0):
        if (gap[chordNum][2] in [12, 24, 36]) or (gap[chordNum][2] in [7, 19, 31]):
            return True

def getMove(chordNum):
    for j in range(4):
        if abs(progress[chordNum-1][j]) > 4:
            return True

def oneMore():
    print()
    tryagain = input("Try Again? ('yes' to try again. 'no' to stop.): ")
    if tryagain == 'yes':
        print()
        main()
    elif tryagain == 'no':
        print()
        print("There ya go!")
        print()
    else:
        print()
        print("Wrong answer...")
        oneMore()

########################

def main():

    genFirstChord(key)

    for chordnum in range(1, chordn):

        isSame = True #4성부에서 같은 음 없음
        isUnstable = True #감5도, 증4도 음정 배제
        isGap = False #베이스와 소프라노의 음정 차이는 적어도 단7도
        isParalle = True
        isEunbok = True
        isMove = True

        while isSame == True or isUnstable == True or isGap == False or isParalle == True or isEunbok == True or isMove == True:
                    
            isSame = False
            isUnstable = False
            isGap = True
            isParalle = False
            isEunbok = False
            isMove = False
                
            genChord(chordnum) # Generates a chord
            lst[chordnum].sort()
            isSame = sameNote(chordnum) # False = same notes don't exist
            isUnstable = unstableInt(chordnum) # False = it's unstable
            isGap = gapNotes(chordnum) # True = gap between the notes is okay
        
            getProgress()
            getGap()
            isParalle = byeong(chordnum)
            isEunbok = eunbok(chordnum)
            isMove = getMove(chordnum)

    printChord()

    player1 = musicalbeeps.Player(volume = 0.05, mute_output = False)
    player2 = musicalbeeps.Player(volume = 0.05, mute_output = False)
    player3 = musicalbeeps.Player(volume = 0.05, mute_output = False)
    player4 = musicalbeeps.Player(volume = 0.05, mute_output = False)

    for i in range(chordn):
        print()
        player1.play_note(dic[(lst[i][0])], 1)
        player2.play_note(dic[(lst[i][1])], 1)
        player3.play_note(dic[(lst[i][2])], 1)
        player4.play_note(dic[(lst[i][3])], 1)

    print()
    player1.play_note(dic[(lst[0][0])], 1)
    player2.play_note(dic[(lst[0][1])], 1)
    player3.play_note(dic[(lst[0][2])], 1)
    player4.play_note(dic[(lst[0][3])], 1)    

    oneMore()

########################

key = key_setting(notes_lst)

main()