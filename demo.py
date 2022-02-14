import math as m

import numpy as np

class Quattro:

    def circle(radius=48, resolution=50, robot_height=-180, n=2, dir_circ=1, end_height = -200):
        """Calculates coordinates for a 2D-circle
            `radius`: Radius of the circle
            `resolution`: Number of circlepoints
            `robotHeight`: z-Coordinate for 2D model (have to be a negative value)
            `n`: Number of rotations
            `dir`: Direction of the circle
            `return`: List of positions and driving mode. Exmaple: [x,y,z,a,b,c,'mov'] for PTP or [x,y,z,a,b,c,'lin'] for
            linear moving
            """

        t = np.linspace(0, n * 2 * m.pi, resolution * n)
        circle_pos = []
        
        circle_pos.append([0, 0, robot_height, 0, 0, 0, 'mov'])
        circle_pos.append([radius, 0, robot_height, 0, 0, 0, 'lin'])

        for num in t:
            if dir_circ == 0:
                x = m.cos(num) * radius
                y = m.sin(num) * radius
            else:
                x = m.cos(num) * radius
                y = m.sin(num - m.pi) * radius

            circle_pos.append([x, y, robot_height, 0, 0, 0, 'mov'])

        circle_pos.append([0, 0, robot_height, 0, 0, 0, 'lin'])
        circle_pos.append([0, 0, end_height, 0, 0, 0, 'mov'])

        return circle_pos

class Delta:
    
    def triangle(half_side_length=30, robot_height=-100, n=2):
        """Calculates coordinates for a samesided triangle
            `halfSideLength`: half sidelength of the triangle
            `robotHeight`: z-Coordinate for 2D model (have to be a negative value)
            `return`: List of positions and driving mode. Exmaple: [x,y,z,a,b,c,'mov'] for PTP or [x,y,z,a,b,c,'lin'] for
            linear moving
            """
        #     ^
        #    / \
        #   /   \
        #  /     \
        # /_______\
        #
        # | a |
        # a = halfSideLength

        h_half = (half_side_length * m.sqrt(3) / 2) / 2
        pos_triangle = []

        for _ in range(n):
            pos_triangle.append([-h_half, half_side_length, robot_height, 0, 0, 0, 'mov'])
            pos_triangle.append([-h_half, -half_side_length, robot_height, 0, 0, 0, 'lin'])
            pos_triangle.append([h_half, 0, robot_height, 0, 0, 0, 'lin'])

        pos_triangle.append([-h_half, half_side_length, robot_height, 0, 0, 0, 'lin'])
        pos_triangle.append([0, 0, endHeight, 0, 0, 0, 'mov'])
        return pos_triangle


class sixRUS:
    def square(half_side_length=25, robot_height=-100, n=2):
        """Calculates coordinates for a square
            `halfSideLength`: half length of the edge
            `robotHeight`: z-Coordinate for 2D model (have to be a negative value)
            `n`: Number of rotations
            `return`: List of positions and driving mode. Exmaple: [x,y,z,a,b,c,'mov'] for PTP or [x,y,z,a,b,c,'lin'] for
            linear moving
            """
        #  _______
        # |       |
        # |       |
        # |_______|
        #
        # | a |
        # a = halfSideLength
        pos_square = [[half_side_length, half_side_length, robot_height, 0, 0, 0, 'mov']]

        for _ in range(n):
            pos_square.append([half_side_length, half_side_length, robot_height, 0, 0, 0, 'lin'])
            pos_square.append([-half_side_length, half_side_length, robot_height, 0, 0, 0, 'lin'])
            pos_square.append([-half_side_length, -half_side_length, robot_height, 0, 0, 0, 'lin'])
            pos_square.append([half_side_length, -half_side_length, robot_height, 0, 0, 0, 'lin'])

        pos_square.append([half_side_length, half_side_length, robot_height, 0, 0, 0, 'lin'])
        pos_square.append([0, 0, endHeight, 0, 0, 0, 'mov'])

        return pos_square


if __name__ == '__main__':
    # Define return list values for demo sequences as this examples:
    # [x,y,z,a,b,c,'mov'] -> PTP
    # [x,y,z,a,b,c,'lin'] -> linear moving
     ans = square()
     print(ans)
