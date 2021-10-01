from django.db import models

# Stores all information regarding the a particular bus.
class Bus(models.Model):
    busNum = models.IntegerField()
    busAgencyName= models.CharField(max_length=64)
    busType = models.CharField(max_length=16)
    seats = models.IntegerField()

    def __str__(self):
        return f"Bus Number- {self.busNum}, Agency-{self.busAgencyName}, Type-{self.busType},Seats- {self.seats}"

# Stores all information about a bus stop
class BusStop(models.Model):

    StopName = models.CharField(max_length=64)
    StopLocation = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.StopLocation}"

# Stores information about particular routes
class Route(models.Model):
    
    origin = models.ForeignKey(BusStop, on_delete=models.CASCADE, related_name="departuresRoutes")
    destination = models.ForeignKey(BusStop,on_delete=models.CASCADE, related_name="arrivalsRoutes")
    
    def __str__(self):
        return f"{self.busId}: from {self.origin} to {self.destination} at {self.cost} rupee"

# Stores all information about a particular trip from origin to destination
class Schedule(models.Model):
    busInfo = models.ForeignKey(Bus, on_delete=models.CASCADE)
    origin = models.ForeignKey(BusStop,on_delete=models.CASCADE, related_name="departuresSchedule")
    destination = models.ForeignKey(BusStop, on_delete=models.CASCADE,related_name="arrivalsSchedule")
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    cost = models.IntegerField()
    seatsEmpty = models.IntegerField(blank = True, null=True)
    
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} at {self.time} on {self.date}"


# Stores information about the passenger
class Passenger(models.Model):
    username = models.CharField(max_length=161)
    custfName = models.CharField(max_length=64)
    custlName = models.CharField(max_length=64)
    custEmail = models.CharField(max_length=32)
    buses = models.ManyToManyField(Schedule, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.custfName} "

# Stores information about the particular ticket
class Ticket(models.Model):
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger,on_delete=models.CASCADE)
    number = models.IntegerField()
    def __str__(self):
        return f"{self.schedule}: {self.number}"


class NameForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField( max_length=100)
    message = models.CharField(max_length=500)


