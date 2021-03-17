import random as ran
class Myasset:
    score=0
    life=3
    def __init__(self):
        pass

def intro():
    import time
    print("Welcome to")

    time.sleep(0.2)
    print("Rock")

    time.sleep(0.2)
    print("paper")

    time.sleep(0.2)
    print("Scissor")

    print("___________________________")


def game():
    while Myasset.life!=0:
        sr=ran.randrange(1,3)
        print("life:",Myasset.life)
        print("score:",Myasset.score)
        print("1.Rock \n2.Paper \n3.Scissor")
        ui=int(input("Enter your option:"))
        if(sr==1 and ui==2) or (sr==2 and ui==3) or (sr==3 and ui==1):
            Myasset.score+=1
            print("life:",Myasset.life)
            print("score:",Myasset.score)
            print("___________________________")
        else:
            Myasset.life-=1
            print("life:",Myasset.life)
            print("score:",Myasset.score)
            print("___________________________")
    print("""
         _____       ___       ___  ___   _____  
        /  ___|     /   |     /   |/   | |  ___| 
        | |        / /| |    / /|   /| | | |__   
        | |  _    / ___ |   / / |__/ | | |  __|  
        | |_| |  / /  | |  / /       | | | |___  
        \_____/ /_/   |_| /_/        |_| |_____|
         
         _____   _     _   _____   _____   
        /  _  \ | |   / / |  ___| |  _  \  
        | | | | | |  / /  | |__   | |_| |  
        | | | | | | / /   |  __|  |  _  /  
        | |_| | | |/ /    | |___  | | \ \  
        \_____/ |___/     |_____| |_|  \_\

        """)


intro()
game()

