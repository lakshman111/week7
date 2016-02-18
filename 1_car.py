class Car:

  def __init__(self):
    self.speed = 0
    self.odometer = 0

  def set_speed(self, new_speed):
    self.speed = new_speed

  def drive_for(self, minutes):
    self.odometer += (self.speed * minutes/60)

  def needs_oil_change(self):
    return (self.odometer >= 3000)


# Let's drive!
# Run this code to see it in action.

car1 = Car()
print("Odometer for car 1 starts at:", car1.odometer, "miles")
car1.set_speed(40)
car1.drive_for(30)
print("Odometer for car 1 is now:", car1.odometer, "miles")
if car1.needs_oil_change():
  print("Car 1 needs an oil change!")

car2 = Car()
print("Odometer for car 2 starts at:", car2.odometer, "miles")
car2.set_speed(80)
car2.drive_for(30)
print("Odometer for car 2 is now:", car2.odometer, "miles")
if car2.needs_oil_change():
  print("Car 2 needs an oil change!")

# Then rearrange the code to help see why we use
# classes and distinct object instances.

# CHALLENGE 1: Can we provide an option to begin each car at a certain odometer value?
# CHALLENGE 2: Can you assign a unique VIN to each car?
