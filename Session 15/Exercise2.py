import math

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

class Circle:
    """Represents a point in 2-D space.

    attributes: center, radius
    """

class Rectangle:
    """Represents a rectangle with corner as bottom left point.

    attributes: width, height, corner.
    """

def get_corner(rect, corner):
    """Returns a Point object for a particular corner of a Rectangle object

    arguments: Rectangle rect, String corner
    
    corner options include:
        - 'top left'
        - 'top right'
        - 'bottom left'
        - 'bottom right'
    """

    pt = Point()

    if corner == 'top left':
        pt.x = rect.corner.x
        pt.y = rect.corner.y + rect.height
    elif corner == 'top right':
        pt.x = rect.corner.x + rect.width
        pt.y = rect.corner.y + rect.height
    elif corner == 'bottom left':
        pt.x = rect.corner.x
        pt.y = rect.corner.y
    elif corner == 'bottom right':
        pt.x = rect.corner.x + rect.width
        pt.y = rect.corner.y
    else:
        pt.x = 0
        pt.y = 0
        print("Invalid corner, defaulting to (0,0)")

    return pt

def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.

    p1: Point
    p2: Point

    returns: float
    """
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circ, pt):
    """Returns whether a point lies on or within the boundary of a circle.
    
    arguments: Circle circ, Point pt
    """

    return distance_between_points(circ.center, pt) <= circ.radius

def rect_in_circle(circ, rect):
    """Returns whether a rectangle lies entirely in or on the boundary of the circle.
    
    arguments: Circle circ, Rectangle rect
    """
    # Check each corner and all in

    top_left = point_in_circle(circ, get_corner(rect,'top left'))
    top_right = point_in_circle(circ, get_corner(rect,'top right'))
    bottom_left = point_in_circle(circ, get_corner(rect,'bottom left'))
    bottom_right = point_in_circle(circ, get_corner(rect,'bottom right'))

    return top_left and top_right and bottom_left and bottom_right

def rect_circle_overlap(circ, rect):
    """Returns whether any part of the rectangle falls within or on the circle

    arguments: Circle circ, Rectangle rect
    """
    # Check corners (for when rectangle's x or y range does not include the center of the circle)
    top_left = point_in_circle(circ, get_corner(rect,'top left'))
    top_right = point_in_circle(circ, get_corner(rect,'top right'))
    bottom_left = point_in_circle(circ, get_corner(rect,'bottom left'))
    bottom_right = point_in_circle(circ, get_corner(rect,'bottom right'))

    # Check edges (for when rectangle's x or y range includes the center of the circle) and set flags for edges
    cross_vertical = False
    cross_horizontal = False
    # Check x bounds when y range includes radius, checked by evaluating if in y is in range between any top point and any bottom point 
    # When the above sentence is true check the left side of the rectangle x-distance to the circles's center is less than radius
    # Also check if right side of rectangle's x-distance to the circle's center is less than radius
    # This works because if the condition is true, the rectangle will have a with at least one point at the height of the radius
    # so since the closest point to the center would be the side of the rectangle at the same y-value as the radius, we just use the distance to the side
    # This process is used to check both sides with the x-value for any left or right corner
    if circ.center.y <= get_corner(rect, 'top left').y and circ.center.y >= get_corner(rect, 'bottom left').y:
        cross_vertical = abs(circ.center.x - get_corner(rect, 'bottom left').x) <= circ.radius or abs(circ.center.x - get_corner(rect, 'bottom right').x) <= circ.radius
    # Check y bounds when x range includes radius, checked by evaluating if x in range between any left point and any right point 
    # Repeat the same process above
    if circ.center.x <= get_corner(rect, 'top right').x and circ.center.x >= get_corner(rect, 'top left').x:
        cross_horizontal = abs(circ.center.y - get_corner(rect, 'top left').y) <= circ.radius or abs(circ.center.y - get_corner(rect, 'bottom left').y) <= circ.radius

    # If any flag is set to True, than that means there is an overlap for that flag
    # Check that the rectangle is not entirely in the circle, since that could have also set the same flags
    # Do this because overlap is not the same as being fully inside the shape
    return (top_left or top_right or bottom_left or bottom_right or cross_vertical or cross_horizontal) and not rect_in_circle(circ, rect)


circle_center = Point()
circle_center.x = 150
circle_center.y = 100

my_circle = Circle()
my_circle.center = circle_center
my_circle.radius = 75

my_point = Point
my_point.x = 80
my_point.y = 20

# Rectangle should be in circle
r_corner_in = Point()
r_corner_in.x = 100
r_corner_in.y = 80
r_in = Rectangle()
r_in.corner = r_corner_in
r_in.width = 100
r_in.height = 40

# Rectangle should be overlapping circle
r_corner_overlap = Point()
r_corner_overlap.x = 200
r_corner_overlap.y = 80
r_overlap = Rectangle()
r_overlap.corner = r_corner_overlap
r_overlap.width = 100
r_overlap.height = 40

# Rectangle should be outside circle
r_corner_out = Point()
r_corner_out.x = 300
r_corner_out.y = 80
r_out = Rectangle()
r_out.corner = r_corner_out
r_out.width = 100
r_out.height = 40

# Rectangle should be outside circle
r_corner_overlap_ = Point()
r_corner_overlap_.x = 220
r_corner_overlap_.y = 60
r_overlap_ = Rectangle()
r_overlap_.corner = r_corner_overlap_
r_overlap_.width = 80
r_overlap_.height = 80

print("In circle (it is)")
print(rect_in_circle(my_circle,r_in))
print("In circle (it is not)")
print(rect_in_circle(my_circle,r_out))

print("Overlap circle (overlaps but fully inside)")
print(rect_circle_overlap(my_circle,r_in))
print("Overlap circle (it is, two corners of rectangle are in circle)")
print(rect_circle_overlap(my_circle,r_overlap))
print("Overlap circle (it is, left side of rectangle crosses right side of circle, no corners inside)")
print(rect_circle_overlap(my_circle,r_overlap_))
print("Overlap circle (it is not, completely outside)")
print(rect_circle_overlap(my_circle,r_out))
