# 0x08-python-more_classes

This folder contains Python scripts and classes that define a `Rectangle` class based on various programming tasks.

## Task 1

1. `Empty Class Rectangle:`
   - Write an empty class `Rectangle` that defines a rectangle.

## Task 2

2. `Rectangle with Width and Height:`
   - Private instance attribute: `width` with getter and setter methods.
   - Private instance attribute: `height` with getter and setter methods.
   - Instantiation with optional width and height.

## Task 3

3. `Rectangle with Area and Perimeter:`
   - Extends Task 2.
   - Public instance method: `area()` that returns the rectangle area.
   - Public instance method: `perimeter()` that returns the rectangle perimeter.

## Task 4

4. `Enhanced Rectangle Printing:`
   - Extends Task 3.
   - Improved print representation of the rectangle using the character `#`.

## Task 5

5. `Rectangle Representation:`
   - Extends Task 4.
   - Implemented `__str__` and `__repr__` methods for string representation.
   - Customized `__repr__` to allow recreation of a new instance using `eval()`.

## Task 6

6. `Rectangle Deletion:`
   - Extends Task 5.
   - Added a message, "Bye rectangle...", when an instance of Rectangle is deleted.

## Task 7

7. `Rectangle Counting Instances:`
   - Extends Task 6.
   - Introduced a public class attribute `number_of_instances` to count instances.
   - Implemented a static method to find the bigger rectangle based on area.

## Task 8

8. `Rectangle Class Attributes:`
   - Extends Task 7.
   - Added a public class attribute `print_symbol` for customized string representation.
   - Improved print() and str() methods to use the symbol defined in `print_symbol`.

## Task 9

9. `Rectangle Static and Class Methods:`
   - Extends Task 8.
   - Implemented a class method `square` to create a square Rectangle instance.

## Task 10

10. `Rectangle Bigger or Equal:`
    - Extends Task 9.
    - Enhanced the static method to handle cases where rectangles have equal area values.
