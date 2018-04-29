from random import choice

direction = ["left", "middle", "right"]
score = [0, 0]


def kickandsave():
    human = input("which direction do you want to shoot?")
    com = choice(direction)
    if human != com:
        print("you win")
        score[0] += 1
    else:
        print("you lose,computer choose", com)

    human = input("which direction do you want to save?")
    com = choice(direction)
    if human == com:
        print("you win")
    else:
        print("you lose,computer choose", com)
        score[1] += 1
    print("final goal:%d(human)VS %d(computer)" % (score[0], score[1]))


for i in range(3):
    print("Round", i + 1)
    kickandsave()
while i >= 2 and score[0] == score[1]:
    i += 1
    print("round$d" % (i + 1))
    kickandsave()
if i >= 2 and score[0] > score[1]:
    print("winner is human")
elif i >= 2 and score[0] < score[1]:
    print("winner is computer")
