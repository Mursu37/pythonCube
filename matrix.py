import math


class Cube:
    def __init__(self, scale):
        self.scale = scale
        self.corners = []
        for i in range(1, 3):
            for j in range(1, 3):
                for k in range(1, 3):
                    vector = Vector(i, j, k)
                    self.corners.append(vector)

        self.check_for_connections()
        self.scale_cube(self.scale)

    def print_vectors(self):
        for corner in self.corners:
            corner.print_vector()

    def check_for_connections(self):
        for corner in self.corners:
            for comparison in self.corners:
                if corner != comparison:
                    matching_coordinates = 0
                    for i in range(len(corner.coordinates)):
                        if corner.coordinates[i][0] == comparison.coordinates[i][0]:
                            matching_coordinates += 1
                    if matching_coordinates >= 2:
                        corner.connections.append(comparison)
        return

    def scale_cube(self, scale):
        for corner in self.corners:
            corner.scale(scale)

    def print_cube(self):
        compstring = None
        for i in self.corners:
            if compstring is None:
                compstring = i.print_char()
            else:
                compstring += i.print_char()

        print(compstring)

    def rotate_cube(self):
        for corner in self.corners:
            corner.rotate_matrix(0.05, 0.05, 0.05)

    def connect_cube(self):
        for corner in self.corners:
            corner.draw_connections()


class Vector:

    def __init__(self, i, j, k):
        self.coordinates = [[i], [j], [k]]
        self.connections = []

    def multiply(self, matrix):
        new_matrix = [[0],
                      [0],
                      [0]]
        for column in range(len(matrix)):
            for i in range(len(matrix[column])):
                multiplication = matrix[column][i] * self.coordinates[i][0]
                new_matrix[column][0] += multiplication

        return new_matrix

    def rotate_matrix(self, a, b, c):
        rotation_matrix = [[math.cos(a) * math.cos(c), math.cos(a) * math.sin(b) * math.sin(c) - math.sin(a) * math.cos(c), math.cos(a) * math.sin(b) * math.cos(c) + math.sin(a) * math.sin(c)],
                           [math.sin(a) * math.cos(b), math.sin(a) * math.sin(b) * math.sin(c) + math.cos(a) * math.cos(c), math.sin(a) * math.sin(b) * math.cos(c) - math.cos(a) * math.sin(c)],
                           [- math.sin(b), math.cos(b) * math.sin(c), math.cos(b) * math.cos(c)]]

        rotated_matrix = self.multiply(rotation_matrix)
        self.coordinates = rotated_matrix
        return

    def scale(self, scale):
        scale_matrix = [[scale, 0, 0],
                        [0, scale, 0],
                        [0, 0, scale]]

        scaled_matrix = self.multiply(scale_matrix)
        self.coordinates = scaled_matrix

    def print_vector(self):
        print(self.coordinates)

    def print_char(self):
        compstring = "\033[" + str(int(self.coordinates[0][0]) - 5) + ";" + str(int(self.coordinates[1][0]) + 25) + "f" + "#"
        return compstring

    def draw_connections(self):
        line_point_count = 10
        connection_line = None
        for connection in self.connections:
            differential_x = connection.coordinates[0][0] - self.coordinates[0][0]
            differential_y = connection.coordinates[1][0] - self.coordinates[1][0]
            increment_x = differential_x / line_point_count
            increment_y = differential_y / line_point_count
            for n in range(line_point_count):
                if connection_line is None:
                    connection_line = "\033[" + str(int(self.coordinates[0][0] + increment_x * n - 5)) + ";" + str(int(self.coordinates[1][0] + increment_y * n + 25)) + "f" + "."
                else:
                    connection_line += "\033[" + str(int(self.coordinates[0][0] + increment_x * n - 5)) + ";" + str(int(self.coordinates[1][0] + increment_y * n + 25)) + "f" + "."

        print(connection_line)

        return
