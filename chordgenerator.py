import random

dic = {-11:"C3",-10:"C#3",-9:"D3",-8:"D#3",
       -7:"E3",-6:"F3",-5:"F#3",-4:"G3",-3:"G#3",
       -2:"A3",-1:"A#3",0:"B3",1:"C4",2:"C#4",3:"D4",
       4:"D#4",5:"E4",6:"F4",7:"F#4",8:"G4",9:"G#4",
       10:"A4",11:"A#4",12:"B4",13:"C5",14:"C#5",15:"D5",
       16:"D#5",17:"E5",18:"F5",19:"F#5",20:"G5",21:"G#5",
       22:"A5",23:"A#5",24:"B5",25:"C6"}

major = [2,2,1,2,2,2,1]

dic_keys = list(dic.keys())
dic_values = list(dic.values())

chordn = int(input("How many chords do you want?: "))

lst = [[0,0,0,0]]*chordn
notes_lst = []

def main():

    for chordnum in range(chordn):

        isSame = True #처음에 4성부에서 같은 음 없음
        isGap = True #베이스와 소프라노의 음정 차이는 적어도 단7도
        isUnstable = True #감5도, 증4도 음정 배제

        while isSame == True or isGap == True or isUnstable == True:

            isSame = False
            isGap = True
            isUnstable = False
        
            for i in range(4):
                lst[chordnum][i] = random.choice(notes_lst)

            for x in range(4):
                for y in range(x+1,4):
                    if lst[chordnum][x] == lst[chordnum][y]:
                        isSame = True

            lst[chordnum].sort()

            for x in range(4):
                for y in range(x+1,4):
                    if lst[chordnum][x]-lst[chordnum][y] == 6 or lst[chordnum][x]-lst[chordnum][y] == 18 or lst[chordnum][x]-lst[chordnum][y] == 30:
                        isUnstable = True

            if  24 >= lst[chordnum][3]-lst[chordnum][0] >= 10:
                isGap = False

        for i in range(4):
            print(dic[(lst[chordnum][i])], end=' ')

        print()

    tryAgain = False
    
    print()

    while tryAgain == False:
        tryagain = input("Try Again? ('yes' to try again. 'no' to stop.): ")

        if tryagain == 'yes':
            tryAgain = True
            print()
            main()
        elif tryagain == 'no':
            tryAgain = True
            print()
            print("There ya go!")
        else:
            print("wrong answer...")
            print()

def key_setting(lst_here):

    key = dic_keys[dic_values.index(input("What key do you want to be in? (type in C3~B3): "))]
    print()
    
    notes = key

    while notes <= max(dic_keys):
        for i in major:
            lst_here.append(notes)
            notes += i

            if notes > max(dic_keys):
                break

key_setting(notes_lst)

main()
