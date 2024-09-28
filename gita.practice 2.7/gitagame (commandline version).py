import time
import winsound
from gitagameaprentis import bhaktisystem as bks


def yes_scene(state,g = "would you like  continue "):
    if state == True:
        while True:
            answer = str(input(g))
            answer = answer.lower()
            if "yes" in answer:
                 print("your reply:"+ answer)
                 break
            else:
                print("your reply"+ answer)
                print("system:sorry but can you write corectly")


def play_conch():
    # Define frequencies for the notes of the conch sound
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

    # Play each note sequentially
    for note in notes:
        winsound.Beep(int(note), 500)  # Play the note for 500 milliseconds
        time.sleep(0.2)  # Add a small delay between notes


def correct_answer_sound():
    # Define the frequency and duration for the correct answer sound
    frequency = 1000  # Adjust frequency as needed
    duration = 300  # Adjust duration as needed

    winsound.Beep(frequency, duration)  # Play the correct answer sound


def chapter_completion_sound():
    # Define frequencies for a soothing and uplifting sound
    notes = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

    # Play the completion sound sequence
    for note in notes:
        winsound.Beep(int(note), 300)  # Play each note for 300 milliseconds
        time.sleep(0.1)  # Add a small delay between notes



gitapic = """
 _______________________________________________________
/                                                       \   bhagwat gita the game
|             B   H   A   G   A   V   A   D             |   plat it 
|                   G   I   T   A                       |
\_______________________________________________________/


"""
loadscreen = "loading..........."
print(gitapic)
time.sleep(2)
play_conch()
player_name = str(input("tell your name"))
player = bks(player_name,0)

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

      Setting the Scene

"""
print(settingthescenes1)
time.sleep(2)
settingthescenes1 = """

             Although widely published and read by itself,
             Bhagavad-gītā originally appears as an episode
            in the Mahābhārata, the epic Sanskrit history of the
            ancient world. The Mahābhārata tells of events leading
             up to the present Age of Kali. It was at the beginning 
            of this age, some fifty centuries ago, that Lord Kṛṣṇa
              spoke Bhagavad-gītā to His friend and devotee Arjuna.
"""
print(settingthescenes1)
time.sleep(1)
yes_scene(True,"say yes to learn more")
time.sleep(2)
settingthescenes1 = """
          Their discourse  one of the greatest philosophical 
          and religious dialogues known to man – took place just
          before the onset of war, a great fratricidal conflict
          between the hundred sons of Dhṛtarāṣṭra and on the opposing
          side their cousins the Pāṇḍavas, or sons of Pāṇḍu.
"""
print(settingthescenes1)
yes_scene(True)
settingthescenes1 = """

           Dhṛtarāṣṭra and Pāṇḍu were brothers born in the Kuru dynasty, 
           descending from King Bharata, a former ruler of the earth,
           from whom the name Mahābhārata derives. Because Dhṛtarāṣṭra,
           the elder brother, was born blind, the throne that otherwise
           would have been his was passed down to the younger brother, Pāṇḍu.
"""
print(settingthescenes1)
yes_scene(True)
while True:
    answer = str(input("lets start our first question should we"))
    answer = answer.lower()
    print("say yes to start")
    if "yes" in answer:
        print("your reply:"+ answer)
        player.showbhakta()
        break
    else:
        print("your reply"+ answer)
        print("system:sorry but can you write corectly ")
        

           
print("""q1:who are were the two brothers in the story 
         1: kalidas and robinson
         2: Dhṛtarāṣṭra and Pāṇḍu
      
        type either 1 or 2
      
      """)

time.sleep(3)
while True:
    answer = str(input("type the answer as 1 or 2"))
    answer = answer.lower()
    if "2" in answer:
        play_conch()
        print("thats correct Dhṛtarāṣṭra and Pāṇḍu where the two brothers")
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")


time.sleep(2)

settingthescenes1 = """
            When Pāṇḍu died at an early age, his five children – Yudhiṣṭhira,
            Bhīma, Arjuna, Nakula and Sahadeva – came under the care of Dhṛtarāṣṭra,
            who in effect became, for the time being, the king. Thus the sons of Dhṛtarāṣṭra 
            and those of Pāṇḍu grew up in the same royal household.
            Both were trained in the military arts by the expert Droṇa and counseled
            by the revered “grandfather” of the clan, Bhīṣma.

"""
print(settingthescenes1)
time.sleep(2)
print("""

       so, lets start with the preface



""")

settingthescenes1 = """
                                      Preface
Originally I wrote Bhagavad-gītā As It Is in the form in which it is presented now. 
When this book was first published, the original manuscript was, unfortunately,
cut short to less than 400 pages, without illustrations and without explanations for 
most of the original verses of the Śrīmad Bhagavad-gītā. In all of my other books – Śrīmad-Bhāgavatam,
Śrī Īśopaniṣad, etc. – the system is that I give the original verse, its English transliteration, 
word-for-word Sanskrit-English equivalents, translations and purports. This makes the 
book very authentic and scholarly and makes the meaning self-evident. I was not very happy, 
therefore, when I had to minimize my original manuscript. But later on, when the demand for 
Bhagavad-gītā As It Is considerably increased, I was requested by many scholars and devotees to present
 the book in its original form. Thus the present attempt is to offer the original manuscript of this 
 great book of knowledge with full paramparā explanation in order to establish the Kṛṣṇa consciousness 
 movement more soundly and progressively.

Our Kṛṣṇa consciousness movement is genuine, historically authorized, natural and transcendental 
due to its being based on Bhagavad-gītā As It Is. It is gradually becoming the most popular 
movement in the entire world, especially amongst the younger generation. It is becoming more and 
more interesting to the older generation also. Older gentlemen are becoming interested, 
so much so that the fathers and grandfathers of my disciples are encouraging 
us by becoming life members of our great society, the International Society for Krishna Consciousness. 
In Los Angeles many fathers and mothers used to come to see me to express their feelings of gratitude for 
my leading the Kṛṣṇa consciousness movement throughout the entire world. Some of them said that it is greatly 
fortunate for the Americans that I have started the Kṛṣṇa consciousness movement in America. But actually 
the original father of this movement is Lord Kṛṣṇa Himself, since it was started a very long time ago but is 
coming down to human society by disciplic succession. If I have any credit in this connection, 
it does not belong to me personally, but it is due to my eternal spiritual master, His Divine Grace 
Oṁ Viṣṇupāda Paramahaṁsa Parivrājakācārya 108 Śrī Śrīmad Bhaktisiddhānta Sarasvatī Gosvāmī Mahārāja Prabhupāda.

If personally I have any credit in this matter, it is only that I have tried to present Bhagavad-gītā as it is, 
without any adulteration. Before my presentation of Bhagavad-gītā As It Is, almost all the English editions of 
Bhagavad-gītā were introduced to fulfill someone’s personal ambition. But our attempt, in presenting Bhagavad-gītā 
As It Is, is to present the mission of the Supreme Personality of Godhead, Kṛṣṇa. Our business is to present the will 
of Kṛṣṇa, not that of any mundane speculator like the politician, philosopher or scientist, for they have 
very little knowledge of Kṛṣṇa, despite all their other knowledge. When Kṛṣṇa says, man-manā bhava mad-bhakto 
mad-yājī māṁ namaskuru, etc., we, unlike the so-called scholars, do not say that Kṛṣṇa and His inner spirit are 
different. Kṛṣṇa is absolute, and there is no difference between Kṛṣṇa’s name, Kṛṣṇa’s form, Kṛṣṇa’s 
qualities, Kṛṣṇa’s pastimes, etc. This absolute position of Kṛṣṇa is difficult to understand for any 
person who is not a devotee of Kṛṣṇa in the system of paramparā (disciplic succession). Generally the 
so-called scholars, politicians, philosophers and svāmīs, without perfect knowledge of Kṛṣṇa, try to 
banish or kill Kṛṣṇa when writing commentary on Bhagavad-gītā. Such unauthorized commentary upon Bhagavad-gītā 
is known as māyāvāda-bhāṣya, and Lord Caitanya has warned us about these unauthorized men. Lord Caitanya clearly 
says that anyone who tries to understand Bhagavad-gītā from the Māyāvādī point of view will commit a great blunder. 
The result of such a blunder will be that the misguided student of Bhagavad-gītā will certainly be bewildered on the 
path of spiritual guidance and will not be able to go back to home, back to Godhead.

Our only purpose is to present this Bhagavad-gītā As It Is in order to guide the conditioned student 
to the same purpose for which Kṛṣṇa descends to this planet once in a day of Brahmā, or every 8,600,000,000 years. 
This purpose is stated in Bhagavad-gītā, and we have to accept it as it is; otherwise there is no point in trying to 
understand the Bhagavad-gītā and its speaker, Lord Kṛṣṇa. Lord Kṛṣṇa first spoke Bhagavad-gītā to the sun-god some hundreds 
of millions of years ago. We have to accept this fact and thus understand the historical significance of Bhagavad-gītā, without 
misinterpretation, on the authority of Kṛṣṇa. To interpret Bhagavad-gītā without any reference to the will of Kṛṣṇa is 
the greatest offense. In order to save oneself from this offense, one has to understand the Lord as the Supreme Personality 
of Godhead, as He was directly understood by Arjuna, Lord Kṛṣṇa’s first disciple. Such understanding of Bhagavad-gītā is 
really profitable and authorized for the welfare of human society in fulfilling the mission of life.

The Kṛṣṇa consciousness movement is essential in human society, for it offers the highest perfection of life. 
How this is so is explained fully in the Bhagavad-gītā. Unfortunately, mundane wranglers have taken advantage of 
Bhagavad-gītā to push forward their demonic propensities and mislead people regarding right understanding of the 
simple principles of life. Everyone should know how God, or Kṛṣṇa, is great, and everyone should know the factual 
position of the living entities. Everyone should know that a living entity is eternally a servant and that unless 
one serves Kṛṣṇa one has to serve illusion in different varieties of the three modes of material nature and thus 
wander perpetually within the cycle of birth and death; even the so-called liberated Māyāvādī speculator has to 
undergo this process. This knowledge constitutes a great science, and each and every living being has to hear it 
for his own interest.

People in general, especially in this Age of Kali, are enamored by the external energy of Kṛṣṇa, and they 
wrongly think that by advancement of material comforts every man will be happy. They have no knowledge that 
the material or external nature is very strong, for everyone is strongly bound by the stringent laws of 
material nature. A living entity is happily the part and parcel of the Lord, and thus his natural function 
is to render immediate service to the Lord. By the spell of illusion one tries to be happy by serving his 
personal sense gratification in different forms which will never make him happy. Instead of satisfying his 
own personal material senses, he has to satisfy the senses of the Lord. That is the highest perfection of life. 
The Lord wants this, and He demands it. One has to understand this central point of Bhagavad-gītā. Our Kṛṣṇa consciousness 
movement is teaching the whole world this central point, and because we are not polluting the theme of 
Bhagavad-gītā As It Is, anyone seriously interested in deriving benefit by studying the Bhagavad-gītā must 
take help from the Kṛṣṇa consciousness movement for practical understanding of Bhagavad-gītā under the direct
guidance of the Lord. We hope, therefore, that people will derive the greatest benefit by studying Bhagavad-gītā 
As It Is as we have presented it here, and if even one man becomes a pure devotee of the Lord, we shall consider 
our attempt a success.

A. C. Bhaktivedanta Swami
12 May 1971
Sydney, Australia

"""
print(settingthescenes1)
yes_scene(True,"read the preface and then say yes to proceed")
time.sleep(2)
settingthescenes1 = """

         now we shall move with a little test
         be carefull if you think you need more time then please 
         read the preface again so that you wont lose your 
         bhakti reputation

"""
print(settingthescenes1)
time.sleep(2)
player.showbhakta()
yes_scene(True,"system:are you ready for the test 1") # test 1
settingthescenes1 = """
                     the Original Formats
              q:   How was “Bhagavad-gītā As It Is” originally written?
                   or simply the language written [hint: learnt in the preface]  

                 options: 1 hindi
                          2 odia
                          3 korean
                          4 sanskrit
                          5 english transliterations
                          6 german
                          7 japanese

                          "write the correct answer in no like 1,7,9,8 "
                          

"""
print(settingthescenes1)
time.sleep(3)
while True:
    answer = str(input("type the answer "))
    answer = answer.lower()
    if "5" in answer:
        print("thats correct english transliterations is the correct option ")
        correct_answer_sound()
        player.morebhakti(10)
        player.showbhakta()
        break
    elif "english" in answer:
        print("thats correct english transliterations is the correct option ")
        correct_answer_sound()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(5)
        player.showbhakta()

time.sleep(3)
player.showbhakta()
yes_scene(True,"system:are you ready for the test 2")#test 2
settingthescenes1 = """
                  Authors Sentiment

                  Q: Was the author happy with the first published version of the book?

                  opt: 1 yes
                       2 no

                 "write the correct answer in no like 1,7,9,8 "


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
    elif "original manuscript" in answer:
        print("thats correct 2 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(5)
        player.showbhakta()

settingthescenes1 = """
                     Movement’s Popularity

          Q: Is the Kṛṣṇa consciousness movement becoming popular?
          
          1: yes its too popular that every person even from the other follower joind in mater
             of years

          2: well who knows the ans

          3: no, its not popular espicialy among the military

          4: Yes, it is becoming popular, especially among the younger generations.

          5: none of the above

"""
print(settingthescenes1)
time.sleep(2)


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
    elif "younger" in answer:
        print("thats correct 4 is the correct option ")
        correct_answer_sound()
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(5)
        player.showbhakta()

yes_scene(True,"shall we proceed to the next question" )

settingthescenes1 = """
       
                     Absolute Position
             

          Q: What is the absolute position of Kṛṣṇa according to the author?


        1: very down baddddd   useless 
        2: Kṛṣṇa is absolute, and there is no difference between His name, form, qualities, and pastimes

             type 1 or 2 only


"""
print(settingthescenes1)
time.sleep(3)

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
    elif "1" in answer:
        print("how did you enven thought of picking that option ")
        print()
        player.morebhakti(10)
        player.showbhakta()
        break
    else:
        print("the answer is incorrect ")
        player.lessbhakti(10)
        player.showbhakta()
          

time.sleep(2)

settingthescenes1 = """
   you have compled the preface 
   have a good day

"""
print(settingthescenes1)
chapter_completion_sound()
chapter_completion_sound()
time.sleep(4) 