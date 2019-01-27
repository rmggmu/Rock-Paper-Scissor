import random
def game_logic(user_move,comp_move):
    if (user_move==1):
        if (comp_move==2):
            return(2)
        elif (comp_move == 3):
            return(1)
        else:
            return(0)
    elif(user_move==2):
        if(comp_move==1):
            return(1)
        elif(comp_move==3):
            return (2)
        else:
            return(0)
    elif(user_move==3):
        if(comp_move==1):
            return(2)
        elif(comp_move==2):
            return (1)
        else:
            return(0)
    else:
        return(0)

def winner(prev_move):
        if(prev_move==1):
            return(2)
        elif(prev_move==2):
            return (3)
        else:
            return(1)

def computer_move(win,lose,prev_move,win_change,win_same,lose_change,lose_same,draw_change,draw_same):
    change_prob=same_prob=0.33
    if(win==1):
        change_prob=win_change/(win_same+win_change)
        same_prob=1-change_prob
    elif(lose==1):
        change_prob=lose_change/(lose_same+ lose_change)
        same_prob=1-change_prob
    else:
        if draw_same!=0 or draw_same!=0:
            change_prob=draw_change/(draw_same+draw_change)
            same_prob=1-change_prob

    print(change_prob,same_prob)
    if(prev_move==1):
        ret=random.choices([1,2,3],[change_prob,same_prob,change_prob])
    elif(prev_move==2):
        ret=random.choices([1,2,3],[change_prob,change_prob,same_prob])
    else:
        ret=random.choices([1,2,3],[same_prob,change_prob,change_prob])
    if(ret[0]==1):
        print("Rock")
    elif((ret[0]==2)):
        print("Paper")
    else:
        print("Scissor")

    return ret[0]








win_change=0
win_same=0
lose_same=0
lose_change=0
draw_change=draw_same=0
win=0
lose=0
prev_move=0
control=1
win_flag=lose_flag=draw_flag=0
while (control!=0):
    print("Enter your move: \n 1:Rock 2:Paper 3:Scissor ")
    move= int(input())
    if (move>3):
        print("Wrong Entry")
        continue
    elif(move<1):
        print("Wrong Entry")
        continue

    if(win==1):
        if(prev_move==move):
            win_same=win_same+1
        elif(prev_move!=0):
            win_change=win_change+1

    elif(lose==1):
        if (prev_move == move):
            lose_same = lose_same + 1
        elif (prev_move != 0):
            lose_change= lose_change + 1
    else:
        if (prev_move == move):
            draw_same +=1
        elif (prev_move != 0):
            draw_change= draw_change + 1

    comp_move=computer_move(win,lose,prev_move,win_change,win_same,lose_change,lose_same,draw_change,draw_same)
    result= game_logic(move,comp_move)
    prev_move=move
    if (result==1):
        print("You Won")
        win=1
        lose=0
        win_flag+=1
    elif(result==2):
        print("Computer Won")
        win=0
        lose=1
        lose_flag+=1
    else:
        print("Draw")
        win=lose=0
        draw_flag+=1
    control=int(input("Want to play again? \n 1:Yes 0:No "))


print("Win Change = "+str(win_change))
print("Lose Change = "+ str(lose_change))
print("Win Same = " + str(win_same))
print("Lose Same = "+str(lose_same) )
print(win_flag,lose_flag,draw_flag)