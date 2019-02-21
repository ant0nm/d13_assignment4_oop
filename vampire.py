class Vampire:

    """ A class representing a vampire. """

    # class variables
    coven = []

    # class methods
    @classmethod
    def create(cls, name, age):
        new_vampire = Vampire(name, age)
        cls.coven.append(new_vampire)
        return new_vampire

    @classmethod
    def sunrise(cls):
        print(len(cls.coven))
        # list() creates a copy of the list passed to it
        # this way we can remove items from a list (mutate it) while iterating through it
        for vampire in list(cls.coven):
            if not (vampire.in_coffin and vampire.drank_blood_today):
                cls.coven.remove(vampire)

    @classmethod
    def sunset(cls):
        for vampire in cls.coven:
            vampire.drank_blood_today = False
            vampire.in_coffin = False

    # instance methods
    def __init__(self, name, age, in_coffin = False, drank_blood_today = False):
        # instance variables
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today

    def __str__(self):
        return "Vampire: {}".format(self.name)

    def drink_blood(self):
        self.drank_blood_today = True

    def go_home(self):
        self.in_coffin = True
