class Cinema:
    pass


class Hall:
    def __init__(self, cinema, capacity):
        self.cinema = cinema
        self.cap = capacity


class Seats:
    def __init__(self, number):
        self.number = number


class Sens:
    def __init__(self, cinema, movie, hall):
        self.movie = movie
        self.hall = hall
        self.cinema = cinema
        self.customer = list()
        self.prototype_sens()

    def prototype_sens(self):
        for i in range(self.hall.cap):
            self.customer.append(Seats(i))




hall = Hall('bahman', 40)
cinema = Cinema
sens = Sens(cinema,'casabelanca', hall)
print(len(sens.customer))