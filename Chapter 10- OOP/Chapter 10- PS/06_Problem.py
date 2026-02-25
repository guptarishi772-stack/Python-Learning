from random import randint

class Train:
    def __init__(golu, trainNo):
        golu.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no. {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare for the Train no {self.trainNo} from {fro} to {to} is {randint(500, 2500)}")

t = Train(342301)
t.book("Pune", "Katni")
t.getStatus()
t.getfare("Pune", "katni")                