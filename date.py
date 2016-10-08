class GameDate():

    def __init__(self):

        self.intdate = 0 
        self.day = 0
        self.month = 0
        self.year = 2016
        self.date_ranges = [[0,30],[31,58],[59,89],[90,119],[120,150],[151,180],[181,211],[212,242],[243,272],[273,303],[304,333],[334,365]]
        self.month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    def getStringRep(self):

        return str(self.day) + "/" + self.month_names[self.month] + "/" + str(self.year)

    def update(self):

        if self.intdate == 365:

            self.year += 1
            self.day = 0
            self.month = 0
            self.intdate = 0

        else:

            self.intdate += 1

        if self.intdate > self.date_ranges[self.month][1]:

            self.month = (self.month + 1) % 12

        self.day = self.intdate - self.date_ranges[self.month][0]


