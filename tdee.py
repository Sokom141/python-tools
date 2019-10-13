class Tdee(object):
    """
    Simple class that lets you calculate an approximation of your total
    daily energy expenditure.
    Set lbs=True to insert a weight in pounds.
    """

    def __init__(self, weight, activity, lbs=False):
        super(Tdee, self).__init__()
        self.weight = weight
        self.activity = activity
        self.lbs = lbs
        self.kcals = None

    def convert_to_lbs(self):
        self.converted_weight = self.weight * 2.205
        return self.converted_weight

    def calculate(self):

        if not self.lbs:
            self.weight = self.convert_to_lbs()

        if self.activity == "1":
            self.kcals = self.weight * 11
        elif self.activity == "2":
            self.kcals = self.weight * 13
        elif self.activity == "3":
            self.kcals = self.weight * 19

        return int(self.kcals)


if __name__ == "__main__":
    use_lbs = None
    weight = None
    activity_level = None

    while use_lbs != "1" and use_lbs != "2":
        use_lbs = input("What do you use?\n1. Kgs\n2. Lbs\n")
    if use_lbs == "1":
        use_lbs = False
    else:
        use_lbs = True

    weight = float(input("\nWhat's your weight?\n"))

    while activity_level != "1" and activity_level != "2" and activity_level != "3":
        activity_level = input("\nWhat's your activity level?\n1.Sedentary\n2.Moderately Active (3 workouts a week)\n3.Very Active (daily heavy workouts)\n")

    expenditure = Tdee(weight, activity_level, use_lbs)
    print(f"\nYour TDEE is: {expenditure.calculate()}")
