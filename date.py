class GameDate():

    def __init__(self):

        self.intdate = 0 
        self.date_ranges = [[0,30],[31,59],[60,90],[91,110],[111,141],[142,171],[172,202],[203,233],[234,263],[264,294],[295,324],[325,365]]
        #that is not correct, yet

    def getStringRep(self):

        month = 0 
        day = 0

        for ind, rang in enumerate(self.date_ranges):

            if self.intdate in rang:

                month = ind + 1
                day = self.intdate - min(rang) + 1
                break

        return str(day) + "/" + str(month)

    def update(self):

        self.intdate = (self.intdate + 1) % 365 
