import math


def is_within_distance(x1, y1, x2, y2):

	# TODO
	# Create check for edge of grid

	# Use the Pythagorean theorem to calculate the distance
	# between the two points (x1, y1) and (x2, y2)
	distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

	# Return true if the distance is less than or equal to 2,
	# and false otherwise
	return distance <= 2


# 1st case user (1,2)  and carA (3,2)
# Return True
print(is_within_distance(1, 2, 3, 2))

# 1st case user (1,2)  and carA (3,2)
# Return False
print(is_within_distance(1, 2, 2, 4))


def points_within_2_units(x, y):
	# Calculate the minimum and maximum x and y coordinates of the square
	# of size 4 centered at the point
	min_x = x - 2
	max_x = x + 2
	min_y = y - 2
	max_y = y + 2

	# Loop through all the points in the square and add their coordinates
	# to a list
	points = []
	for x_inner in range(min_x, max_x + 1):
		for y_inner in range(min_y, max_y + 1):

			if is_within_distance(
			    x, y, x_inner, y_inner) and not (x, y) == (x_inner, y_inner):
				points.append((x_inner, y_inner))

	return points


x = -200
y = 300

points = points_within_2_units(x, y)

# for point in points:
#   if ((point[0] - x + point[1] - y) > 2):
#     print("End")

print(points)
