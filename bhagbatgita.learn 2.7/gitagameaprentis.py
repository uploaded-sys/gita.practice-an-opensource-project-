class bhaktisystem:
    def  __init__ (self,player,bhaktimeter):#creat a bhakta 
        self.player = player
        self.bhaktimeter = bhaktimeter

    def showbhakta(self):
        print("bhaktaname:",self.player)
        print("bhaktimeter:",self.bhaktimeter)


    def showbhakti(self): #shows bhatas bhatimeter
        print("bhaktimeter:",self.bhaktimeter)

    def lessbhakti(self,minus): #defame bhaktas bhakti 
        self.bhaktimeter = self.bhaktimeter - minus
        print("bhaktimeter:",self.bhaktimeter)

    def morebhakti(self,add): #makes bhata more closer to bhakti
        self.bhaktimeter = self.bhaktimeter + add
        print("bhaktimeter:",self.bhaktimeter)