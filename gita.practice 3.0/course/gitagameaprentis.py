import time
# class frame work
class bhaktisystem:
    def __init__(self,player,bhaktimeter):
        self.player = player
        self.bhaktimeter = bhaktimeter
        
    def showbhakta(self):
        print("bhaktaname:",self.player)
        print("bhaktimeter:",self.bhaktimeter)


    def showbhakti(self) -> int: #shows bhatas bhatimeter
        print("bhaktimeter:",self.bhaktimeter)

    def lessbhakti(self,minus) -> int: #defame bhaktas bhakti 
        self.bhaktimeter -= minus
        print("bhaktimeter:",self.bhaktimeter)

    def morebhakti(self,num) -> int: #makes bhata more closer to bhakti
        self.bhaktimeter += num
        print("bhaktimeter:",self.bhaktimeter)

    print("working..................")    
    time.sleep(5)

