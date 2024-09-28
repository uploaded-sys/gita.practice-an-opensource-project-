from gitautilities import *  # import utilities module
initialize()
import time # import time
import winsound # import winsound module
from gitagameaprentis import bhaktisystem as bks # import player definer module
loadscreen('importing pakages')
gitapic = """
 _______________________________________________________
|                                                       |   bhagwat gita the game
|             B   H   A   G   A   V   A   D             |   plat it 
|                   G   I   T   A                       |
|_______________________________________________________|


"""
time.sleep(2)
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


time.sleep(2)




settingthescenes1 = """

             ___________________________________________
           |             Bhagavad Gita Game             |
           |              hare krishna                 |
           |                                           |
          |            introduction                     |
          |                                             |    
            -------------------------------------------
                   |   ^__^
                    |  (oo)|_______
                       (__)|       )||
                         U  ||----w |
                            ||     ||


"""
print(settingthescenes1)
loadscreen('setting game ')

yes_scene(True,"so should we start the introduction")
player.showbhakta()

settingthescenes1= """

        the game now promes reading books than staying up on computers
        so ther is a folder named resourses which contains
        different docs that is names with a number like (1_preface)
        note that the chapter 1_preface has no resourses.
        so that nuber just defines which chapter it represent 
        you may find more than 1 resourse of a chapter 
        open it manualy and read it contents and then come 
        to the program to answer different questions of the resoures 
        well the game will say which resourse has to be completed to answer the 
        questions.

        we want most of you to print the resoures.
        then read.


"""
print(settingthescenes1)
time.sleep(4)
yes_scene(True,"if you have done reading the resourse 2_introduction lets start answering questions ")
# question 1
loadscreen('making questions ready!', col= '#f2ff00')
settingthescenes1 = """
    1       Who is Śrī Caitanya?
     opts:

     1 = a normal bussisman 
     2 = Śrī Caitanya is the figure who established the mission to fulfill Lord Caitanya’s desire on Earth.
     3 = Śrī Caitanya is a germothenalogis a partner of scaler.org
     4 = void
    
"""
print(settingthescenes1)

while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "2" in answer:
        print("thats correct 2 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

yes_scene(True,"next question!")
# question 2
settingthescenes1 = """
    2       What did the spiritual master do for the author?
     opts:

     1 = a tour of the universe. 
     2 = he gave him a lolipop.
     3 = The spiritual master opened the author's eyes with the torch of knowledge.
     4 = he motivated him. 
    
"""
print(settingthescenes1)

while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


yes_scene(True,"next question!")
# question 3
settingthescenes1 = """
    3       What is the significance of Śrīla Rūpa Gosvāmī Prabhupāda?
     opts:
     1 = Śrīla Rūpa Gosvāmī Prabhupāda established the mission to fulfill Lord Caitanya's 
         desire and the author seeks shelter under his lotus feet.
     2 = he gave him a lolipop and a macbook pro. 
     3 = The golden lassi.
     4 = his significance was to spread bhagbatgita game around the world. 
    
"""
print(settingthescenes1)

while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "1" in answer:
        print("thats correct 1 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


yes_scene(True,"next question!")
# question 4
loadscreen('making questions ready!', col= '#8800ff')
settingthescenes1 = """
     4       To whom does the author offer obeisances?
     opts:
     1 = question is incorrect. 
     2 = the author gathered   obeisances from his coleages.
     3 = shri krishna bhagbatgita. 
     4 = The author offers obeisances to the lotus feet of the spiritual master, all Vaiṣṇavas, and the associates of Lord Kṛṣṇa.
    
"""
print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "4" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

# question 5

loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     5       Who is Rādhārāṇī?
     opts:
     1 = both 2 and 3. 
     2 = void.
     3 = Rādhārāṇī is described as the Queen of Vṛndāvana, with a bodily complexion like molten gold, very dear to Lord Kṛṣṇa.
     4 = teacher of shri krishna. 
    
"""
print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 6 
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     6      What is Bhagavad-gītā also known as?
     opts:
     1 = both 2 and 3. 
     2 = Bhagavad-gītā is also known as Gītopaniṣad.
     3 = bhatbutyan.
     4 = shrimat bhagbatgita.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "2" in answer:
        print("thats correct 2 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


#question 7
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     7      Why is Bhagavad-gītā important?
     opts:
     1 = It is the essence of Vedic knowledge and one of the most important Upaniṣads in Vedic literature.
     2 = it helps us learn to code.
     3 = helps us know how life works.
     4 = none of the above.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "1" in answer:
        print("thats correct 1 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 8
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     8      What does the author say about other English commentaries on Bhagavad-gītā?
     opts:
     1 = It is the essence of Vedic knowledge and one of the most important Upaniṣads in Vedic literature.
     2 = he thinks the commentaries are good.
     3 = nothing.
     4 = The author believes that none of them are authoritative as they express 
         personal opinions without capturing the spirit of Bhagavad-gītā as it is.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "4" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 9
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     9      How should Bhagavad-gītā be accepted?
     opts:
     1 = it should be as a strict diet.
     2 = as a complement.
     3 = It should be accepted as directed by the speaker, Lord Śrī Kṛṣṇa, the Supreme Personality of Godhead.
     4 = as a history lecture.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


#question 10
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     10      Who confirms Lord Śrī Kṛṣṇa as the Supreme Personality of Godhead?.
     opts:
     1 = Great ācāryas like Śaṅkarācārya, Rāmānujācārya, Madhvācārya, and others confirm this.
     2 = the devloper confirms it.
     3 = prime mrimrminester modi confirms it.
     4 = fbi.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "1" in answer:
        print("thats correct 1 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


#question 11
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     11      What is the relationship between the living entities and the Supreme Lord?.
     opts:
     1 = dronenacharya conferms it.
     2 = in page 463.
     3 = at daily.dev.
     4 = The living entities have an eternal relationship with the Supreme Lord in one of five different ways.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "4" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 12
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     12      How did Arjuna accept the teachings of Bhagavad-gītā?
     opts:
     1 = because he watched a blog on it .
     2 = in page 167.
     3 = Arjuna accepted Kṛṣṇa as the Supreme Brahman and the teachings as the absolute truth.
     4 = who knows.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 13
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     13      What is the ultimate goal of Bhagavad-gītā?
     opts:
     1 = as it looks so cool.
     2 = to teach us bake a pizza italiano.
     3 = To deliver mankind from the nescience of material existence.
     4 = who knows as usual.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 14
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     14      What is the significance of remembering the Supreme Lord?
     opts:
     1 = Remembering the Supreme Lord enables one to transfer to the spiritual world.
     2 = go to heaven.
     3 = just for fun.
     4 = who knows as usual.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "1" in answer:
        print("thats correct 1 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()


#question 15
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     15      What is the result of reading Bhagavad-gītā sincerely?
     opts:
     1 = answer doesen`t exist.
     2 = gain knowledge.
     3 = just for fun.
     4 = none of the above.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "4" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 16 
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     16       How can one remember the Supreme Lord always?
     opts:
     1 = answer doesen`t exist.
     2 = By chanting His names and molding life’s activities to remember Him always.
     3 = just for fun.
     4 = none of the above.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "2" in answer:
        print("thats correct 2 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 17
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     17     What is the essence of all Vedic literatures?
     opts:
     1 = answer doesen`t exist.
     2 = Bhagavad-gītā is the essence of all Vedic literatures.
     3 = who knows.
     4 = search google.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "2" in answer:
        print("thats correct 2 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 18
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     18       What is the benefit of drinking the water of the Ganges or the nectar of Bhagavad-gītā?
     opts:
     1 = science.
     2 = to keep us pure.
     3 = One attains salvation and is freed from the cycle of rebirth.
     4 = none of the above.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "3" in answer:
        print("thats correct 3 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 19
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     19     What is the Gītopaniṣad?
     opts:
     1 = Gītopaniṣad is another name for Bhagavad-gītā, compared to a cow milked by Lord Kṛṣṇa.
     2 = a name of a river.
     3 = who knows.
     4 = search google.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "1" in answer:
        print("thats correct 1 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()

#question 20
loadscreen('making question ready!', col= '#A7F03E')
settingthescenes1 = """
     20       What is the recommended one scripture, one God, one hymn, and one work for the present age?
     opts:
     1 = science.
     2 = to keep us pure.
     3 = One attains salvation and is freed from the cycle of rebirth.
     4 = The recommended one scripture is Bhagavad-gītā, one \n God is Śrī Kṛṣṇa, one hymn is the chanting of His \n name, and one work is the service of the Supreme Personality of Godhead.
    
"""

print(settingthescenes1)


while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "4" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()




chapter_completion_sound()
settingthescenes1 = """
        hey you have sucessfully completed this interactive 
          python course on bhagbatgita
             well this was just the introduction time
                 for chapter one!!!!!! 
"""

print(settingthescenes1)
time.sleep(5)