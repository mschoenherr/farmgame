class GameDate():

    def __init__(self):

        self.intdate = 0 
        self.year = 2016
        self.date_ranges = [[0,30],[31,58],[59,89],[90,119],[120,150],[151,180],[181,211],[212,242],[243,272],[273,303],[304,333],[334,365]]
        self.month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def getStringRep(self):

        month = 0 
        day = 0

        for ind, rang in enumerate(self.date_ranges):

            if rang[0] <= self.intdate <= rang[1]:

                month = self.month_names[ind]
                day = self.intdate - min(rang) + 1
                break

        return str(day) + "/" + month + "/" + str(self.year)

    def update(self):

        if self.intdate == 365: self.year += 1

        self.intdate = (self.intdate + 1) % 365 
