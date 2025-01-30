import random

animals_to_chase = ["squirrel", "chipmunk", "cat", "crow", "fox", "skunk"]

class Dog:

    def __init__(self, name, breed, color, favorite_toy, favorite_treat):
        happiness = "low"
        speed = 10
        self.name = name
        self.breed = breed
        self.color = color
        self.fav_toy = favorite_toy
        self.speed = speed
        self.happiness = happiness
        self.fav_treat = favorite_treat

    def introduce_dog(self):
        print(f"{self.name} is a {self.color} {self.breed}. {self.name} loves playing with {self.fav_toy}, "
              f"his favorite toy. And loves it even more when its owner gives it a {self.fav_treat}.")

    def zoomies(self):
        """Gives the dog a boost of energy."""
        rand_anim = random.choice(animals_to_chase)
        self.speed *= 2
        print(f"{self.name} got the zoomies and is chasing a {rand_anim} at {self.speed}mph in the yard.")

    def check_happiness(self):
        """Checks the dog's level of happiness."""
        if self.happiness == "low":
            print(f"Oh, no! {self.name}'s level of happiness is {self.happiness}.\nPerhaps playing with {self.name} "
                  f"or giving it a {self.fav_treat} will get its spirits up!")
        elif self.happiness == "medium":
            print(f"{self.name}'s level of happiness is {self.happiness}. I'm sure a {self.fav_treat} could make "
                  f"things better for {self.name}.")

        else:
            print(f"{self.name}'s level of happiness is {self.happiness}. {self.name} loves you!")

    def play_with_dog(self):
        """Helps the dog level up its happiness level if not high."""
        if self.happiness == "low":
            self.happiness = "medium"
            print(f"You got {self.name}'s favorite toy and you two played together. {self.name}'s level of "
                  f"happiness is now {self.happiness}. Perhaps it could use a snack to feel happier.")
        elif self.happiness == "medium":
            self.happiness = "high"
            print(f"You got {self.name}'s favorite toy and you two played together. {self.name}'s level of "
                  f"happiness is now {self.happiness}. Great job!")
        else:
            print(f"You got {self.name}'s favorite toy and you two played together. {self.name}'s loves your company.")

    def give_treat(self):
        """Gives dog its favorite treat/snack."""
        if self.happiness == "low":
            self.happiness = "medium"
            print(f"You gave {self.name} a {self.fav_treat}, its favorite! {self.name}'s level of happiness is now "
                  f"{self.happiness}. Perhaps playing or another snack will make it all better.")
        elif self.happiness == "medium":
            self.happiness = "high"
            print(f"You gave {self.name} a {self.fav_treat}, its favorite! {self.name}'s level of happiness is now "
                  f"{self.happiness}. You're an excellent dog owner!")
        else:
            print(f"You gave {self.name} a {self.fav_treat}, its favorite! {self.name} loves you!")