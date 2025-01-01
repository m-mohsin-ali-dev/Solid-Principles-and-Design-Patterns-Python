"""
Liskov Substitution Principle

It states that objects of a superclass should be replaceable with objects of a subclass without altering the correctness
of the program. This means a subclass must respect the behavior expected from the superclass, ensuring substitutability.
In other words, a subclass should be able to replace its superclass without breaking the program's functionality.
"""


class Bird:
    """
    A base class for birds.
    """

    def fly(self) -> str:
        """
        Return a flying message for the bird.
        """
        return "I can fly!"

class Sparrow(Bird):
    """
    A class representing a sparrow.
    """

    def fly(self) -> str:
        return "Sparrow flying high!"

class Ostrich(Bird):
    """
    A class representing an ostrich, which cannot fly.
    """

    def fly(self) -> str:
        """
        Ostriches can't fly, so this violates LSP when used as a Bird.
        """
        raise NotImplementedError("Ostriches cannot fly.")

# Example Usage
def make_bird_fly(bird: Bird):
    """
    Makes a bird fly and prints its flying ability.
    """
    print(bird.fly())

birds = [Sparrow(), Ostrich()]  # Mixing both flying and non-flying birds

for bird in birds:
    make_bird_fly(bird)  # This will fail for Ostrich, violating LSP


"""
The Ostrich class violates the Liskov Substitution Principle because it does not adhere to the behavior expected from the
Bird superclass, specifically the ability to fly. When make_bird_fly calls bird.fly(), it fails for Ostrich.

We can apply liskov substitution principle to the above class as follows
"""

class Bird:
    """
    A base class for birds.
    """

    def make_sound(self) -> str:
        """
        Return a generic bird sound.
        """
        raise NotImplementedError("Subclasses must implement this method.")

class FlyingBird(Bird):
    """
    A base class for birds that can fly.
    """

    def fly(self) -> str:
        """
        Return a flying message for the bird.
        """
        return "I can fly!"

class Sparrow(FlyingBird):
    """
    A class representing a sparrow.
    """

    def make_sound(self) -> str:
        return "Chirp chirp!"

class Ostrich(Bird):
    """
    A class representing an ostrich.
    """

    def make_sound(self) -> str:
        return "Boom boom!"

# Example Usage
def describe_bird(bird: Bird):
    """
    Describes the bird's behavior, ensuring LSP is not violated.
    """
    print(bird.make_sound())
    if isinstance(bird, FlyingBird):
        print(bird.fly())

birds = [Sparrow(), Ostrich()]

for bird in birds:
    describe_bird(bird)  # Works correctly for both flying and non-flying birds


"""
In this corrected version, we adhere to the Liskov Substitution Principle by restructuring the class hierarchy.

The base class Bird includes behavior common to all birds, while a subclass FlyingBird defines flying-specific behavior.

The Sparrow and Ostrich subclasses implement only the behaviors relevant to them.

The above code now conforms to the LSP principle.
"""
