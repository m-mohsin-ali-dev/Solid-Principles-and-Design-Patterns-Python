"""
Open-Closed Principle

It states that a software entity (like a class, module, or function) should be open for extension but
closed for modification. In other words, we should be able to extend the functionality of a class or
module without altering its existing code.
"""


class Shape:
    """
    A class for managing different shapes and calculating their areas.

    This class violates the Open-Closed Principle because it requires modification
    whenever a new shape is added.
    """

    def __init__(self, shape_type: str, dimension1: float, dimension2: float = None):
        """
        Initialize the Shape with its type and dimensions.

        Args:
            shape_type (str): The type of the shape (e.g., rectangle, circle).
            dimension1 (float): The first dimension (width/radius).
            dimension2 (float, optional): The second dimension (height), if applicable.
        """
        self.shape_type = shape_type
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    def calculate_area(self):
        """
        Calculate the area based on the shape type.

        Returns:
            float: Area of the shape based on its type.
        """
        if self.shape_type == "rectangle":
            return self.dimension1 * self.dimension2  # Area of rectangle
        elif self.shape_type == "circle":
            return 3.14 * self.dimension1 * self.dimension1  # Area of circle
        else:
            raise ValueError("Unknown shape type")

shapes = [
    Shape("rectangle", 5, 10),
    Shape("circle", 7),
    Shape("triangle", 6, 8)
]


for shape in shapes:
    print(f"Area: {shape.calculate_area()}")

"""
The above class Shape violates open-closed principle because it cannot be closed against new type of shapes.If we add 
a new shape (e.g., triangle) we would need to modify the calculate_area function. You see, for every new shape, a new 
logic is added to the calculate_area function. This is quite a simple example. When your application grows and becomes
complex, you will see that the if statement would be repeated over and over again in the calculate_area function each 
time a new shape is added, all over the application.

We can apply open-closed principle to the above class as follows
"""

class Shape:
    """
    A base class for shapes that defines a method to calculate area.
    This class is designed to be extended by other shape classes.
    """

    def calculate_area(self):
        """
        Calculate the area of the shape.
        This method should be overridden by subclasses.

        Returns:
            float: Area of the shape.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """
    A class representing a rectangle shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns:
            float: Area of the rectangle.
        """
        return self.width * self.height


class Circle(Shape):
    """
    A class representing a circle shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: Area of the circle.
        """
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    """
    A class representing a triangle shape.

    Attributes:
        base (float): The base of the triangle.
        height (float): The height of the triangle.
    """

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        """
        Calculate the area of the triangle.

        Returns:
            float: Area of the triangle.
        """
        return 0.5 * self.base * self.height


# Example Usage
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(4, 8)  # Adding a triangle shape
]

for shape in shapes:
    print(f"Area: {shape.calculate_area()}")

"""
Shape now has a virtual method calculate_area. We have each shape extend the
Shape class and implement the virtual calculate_area method.

Every shape adds its own implementation on how it calculates an area in the
calculate_area. We iterate through the array of shape and just calls its
calculate_area method.

Now, if we add a new shape, calculate_area doesn’t need to change.  All we need
to do is add the new shape to the shape array.

calculate_area now conforms to the OCP principle.
"""
