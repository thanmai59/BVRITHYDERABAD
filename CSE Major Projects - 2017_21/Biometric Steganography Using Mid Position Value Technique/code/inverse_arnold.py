import numpy as np
import math, time, sys
from PIL import Image
from arnold import Arnold

def main(argv):
    image_name = "hidden.png"
    image_path = image_name
    a = 6
    b = 40
    rounds = 33

    scrambled = np.array(Image.open(image_path).convert("L"))
    arnold = Arnold(a, b, rounds)
    start_time = time.time()
    reconstructed = arnold.applyInverseTransformTo(scrambled)
    exec_time = time.time() - start_time
    #print("Inverse T. execution time: %.6f " % exec_time, "sec")
    im = Image.fromarray(reconstructed).convert("L")
    im.save("reconstructed.png")


if __name__ == "__main__":
    main(sys.argv[1:])
