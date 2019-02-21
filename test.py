from vampire import Vampire

# test out the class
dracula = Vampire.create("Dracula", 600)
deacon = Vampire.create("Deacon", 150)
balthazar = Vampire.create("Balthazar", 250)
anton = Vampire.create("Anton", 25)
# send everyone home first
for vampire in Vampire.coven:
    vampire.go_home()
# see the result
print("Before sunset:")
for vampire in Vampire.coven:
    print("*", "Name: {}\t In Coffin: {}\t Drank Blood Today: {}".format(vampire.name, vampire.in_coffin, vampire.drank_blood_today))
# let the night begin
Vampire.sunset()
print()
print("After sunset:")
# check the difference
for vampire in Vampire.coven:
    print("*", "Name: {}\t In Coffin: {}\t Drank Blood Today: {}".format(vampire.name, vampire.in_coffin, vampire.drank_blood_today))
dracula.drink_blood()
dracula.go_home()
deacon.drink_blood()
deacon.go_home()
print()
print("When the night is over:")
for vampire in Vampire.coven:
    print("*", "Name: {}\t In Coffin: {}\t Drank Blood Today: {}".format(vampire.name, vampire.in_coffin, vampire.drank_blood_today))
# let the sun rise
Vampire.sunrise()
print()
print("Vampires left in the coven after sunrise:")
for vampire in Vampire.coven:
    print("*", "Name: {}\t In Coffin: {}\t Drank Blood Today: {}".format(vampire.name, vampire.in_coffin, vampire.drank_blood_today))
dracula.drink_blood()
print(len(Vampire.coven))
