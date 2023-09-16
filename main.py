import matrix
import os
import time
os.system("")

if __name__ == '__main__':
    print("Running")
    cube = matrix.Cube(20)
    while 1:
        cube.connect_cube()
        cube.print_cube()
        cube.rotate_cube()
        time.sleep(0.01)
        os.system("cls")
