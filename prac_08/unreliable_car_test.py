from prac_08.unreliable_car import UnreliableCar

good_car = UnreliableCar("good car", 100, 90)
unreliable_car = UnreliableCar("unreliable car", 100, 9)

for i in range(1, 12):
    print("Attempting to drive {}km:".format(i))
    print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
    print("{:12} drove {:2}km".format(unreliable_car.name, unreliable_car.drive(i)))
    print("")

print(good_car)
print(unreliable_car)
