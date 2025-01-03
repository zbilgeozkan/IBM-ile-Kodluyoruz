import math

# Formula Representation
def euclideanDistance(first_point, second_point):
    """
    Calculate the Euclidean distance between two points in 2D space.

    Args:
        first_point (tuple): A tuple representing the first point (x1, y1).
        second_point (tuple): A tuple representing the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    return math.sqrt( (second_point[0] - first_point[0])**2 + (second_point[1] - first_point[1])**2 )

# Defining the points
points = [(0, 2), (1, 4), (3, 6), (5, 8)]

# Calculating distances
distances = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[j]))

# Final value
minimum_distance = min(distances)
print(f"The minimum Euclidean distance is: {minimum_distance}")