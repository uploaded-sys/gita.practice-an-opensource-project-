import time # import time
import winsound # import winsound module
from gitagameaprentis import bhaktisystem as bks # import player definer module
from gitautilities import *  # import utilities module

gitapic = """
 _______________________________________________________
/                                                       \   bhagwat gita the game
|             B   H   A   G   A   V   A   D             |   plat it 
|                   G   I   T   A                       |
\_______________________________________________________/


"""
time.sleep(2)
loadscreen = "loading..........."
print(gitapic)
player_name = str(input("tell your name"))
player = bks(player_name,0) 
player.showbhakta()
play_conch()


while True:
    answer = str(input("continue"))
    answer = answer.lower()
    if "yes" in answer:
        print("your reply:"+ answer)
        break
    else:
        print("your reply"+ answer)
        print("system:sorry but can you write corectly")


play_conch()
for i in range(0,5):
    print(loadscreen)
    time.sleep(.5)


time.sleep(2)




settingthescenes1 = """

             ___________________________________________
           /             Bhagavad Gita Game             |
           \              hare krishna                 /
           /                                           |
          /            introduction                     |
          \                                             /    
            -------------------------------------------
                   \   ^__^
                    \  (oo)\_______
                       (__)\       )\/
                         U  ||----w |
                            ||     ||


"""
print(settingthescenes1)


yes_scene(True,"so should we start the introduction")
player.showbhakta()

def choselearning_resource():
    settingthescenes1 = """

       type 1 for (introduction chapter)

     """
    print(settingthescenes1)
