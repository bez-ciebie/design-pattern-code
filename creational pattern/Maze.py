class MapSite(object):
    def __init__(self) -> None:
        pass

    def entry(self):
        isEntry = 0
        return isEntry()

    def direction(self):
        self.direction=['North', 'South', 'East', 'West']

class Room(MapSite):
    def __init__(self, roomNo) -> None:
        super().__init__()
        self.__roomNo = roomNo
        self.__side = []

    def getSide(self, Direction):
        return Direction

    def setSide(self, Direction, MapSite):
        self.Direction = Direction

    def entry(self):
        return super().entry()
    
class Wall(MapSite):
    def __init__(self) -> None:
        super().__init__()

    def entry(self):
        return super().entry()
    
class Door(MapSite):
    def __init__(self, room1, room2) -> None:
        super().__init__()
        self.__room1 = room1
        self.__room2 = room2
        self.__isOpen = 0
    
    def entry(self):
        isEntry = 1
        return isEntry
    
    def OtherSideFrom(self, Room):
        if Room == self.__room1:
            return self.__room2
        elif Room == self.__room2:
            return self.__room1
        else:
            print("no such room")

class Maze():
    def __init__(self) -> None:
        roomList = []
        pass

    def AddRoom(Room):
        roomList += Room.__roomNo
    
class MazeGame():
    def MazeGame():
        aMaze = Maze()
        r1 = Room(1)
        r2 = Room(2)
        theDoor = Door(r1, r2)

        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)

        r1.setSide("North", Wall)
        r1.setSide("East", theDoor)
        r1.setSide("South", Wall)
        r1.setSide("West", Wall)

        r2.setSide("North", Wall)
        r2.setSide("East", Wall)
        r2.setSide("South", Wall)
        r2.setSide("West", theDoor)       

        return aMaze

game1 = MazeGame()



       



