import math as m

import numpy as np

endHeight = -200  # final height of the robot at the end of every demo programm

def circle(radius=48, resolution=50, robot_height=-180, n=2, dir_circ=1):
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
    circle_pos.append([0, 0, endHeight, 0, 0, 0, 'mov'])

    return circle_pos

if __name__ == '__main__':
    # Define return list values for demo sequences as this examples:
    # [x,y,z,a,b,c,'mov'] -> PTP
    # [x,y,z,a,b,c,'lin'] -> linear moving
     ans = square()
     print(ans)
