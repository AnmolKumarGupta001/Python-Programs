from random import randint
class train:
    def __init__(self, trainno):
       self.trainno = trainno
    def book(self, fro, to):
        print(f"Yout ticket is booked on train number {self.trainno} from {fro} to {to}")

    def getstatus(self):
        print(f"Your train number {self.trainno} is on time")

    def getfare(self, fro , to):
        print(f"ticket fare in train number {self.trainno} from {fro} to {to} is {randint(222,5555)}")

t= train(225588)
t.book("bangalore", "gkp")
t.getstatus()
t.getfare("bangalore", "gkp")

