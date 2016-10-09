from constants import g_date_ranges,g_month_names,g_start_year

class GameDate():

    def __init__(self):

        self.intdate = 0 
        self.day = 0
        self.month = 0
        self.year = g_start_year
        self.date_ranges = g_date_ranges
        self.month_names = g_month_names

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


