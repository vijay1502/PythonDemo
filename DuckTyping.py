class Altroz:
    def gearing(self):
        print("5 gears and non-Automatic")


class Celerio:
    def gearing(self):
        print("5 gears, non automatic and flexible driving")

class Car:
    def typeOfGear(self,carType):
        carType.gearing();

class Vehicle:
    def typeOfVehicle(self,vehicleType):
        vehicleType.typeOfGear();


car=Car();
carType=Altroz();
vehicleType=Vehicle();
car.typeOfGear(carType)



class Game:
    def numbeROfPlayers(self,giveCount):
        print (giveCount);

class Cricket:
    def teamOut(self,players):
        players.numbeROfPlayers(11);

class Tennis:
    def teamOut(self,gamePlayers):
        gamePlayers.numbeROfPlayers(2)


team=Game();
cricket=Cricket();
cricket.teamOut(team)
tennis=Tennis();
tennis.teamOut(team)