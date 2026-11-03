#------------------------------------------------------------------------------
# pixelfixer.py: a command-line utility that fixes red-corrupted pixels in an
# RGB image.
#
# Run with:
#   python pixelfixer.py easy_corrupt_io_small.png
# which writes fixed_easy_corrupt_io_small.png next to the input.
#------------------------------------------------------------------------------
import sys
import numpy as np
from matplotlib.pyplot import imread, imsave


def pixelfix(I):
    """Replace bad pixels with the color averaged from their neighbors.

    Parameters
    ----------
    I : ndarray, shape (M, N, 3)
        A color image array in RGB format, values between 0 and 1.
        A bad pixel has red = 1, green = 0, blue = 0.

    Returns
    -------
    Iq : ndarray, same shape as I
        A copy of the image with the bad pixels fixed.
    """
    Iq = I.copy()

    ### YOUR WORK GOES HERE (with the agent, under the Protocol, in stages:
    ### 1. find the bad pixels and print how many;
    ### 2. paint them white and look at the result;
    ### 3. replace the white with the average of the up/down/left/right
    ###    neighbors. Then try solo_corrupt_io_small.png.)

    # find the bad pixels using boolean conditions 
    bad_pixels =  ((Iq[:,:,0] == 1) & (Iq[:,:,1] == 0) & (Iq[:,:,2] == 0))
    # print how many there are 
    print(f"There are {bad_pixels.sum()} bad pixels")
    # set all the bad pixel color values to 1, which makes them white
    Iq[bad_pixels] = 1

    # TODO(human): stage 3 -- replace each bad pixel with the average of its
    # up/down/left/right neighbors.
    #   1. Get the row and column indices of the bad pixels: np.where(bad_pixels)
    #   2. Loop over the (row, col) pairs.
    #   3. Grab the 4 neighbor colors: (r-1, c), (r+1, c), (r, c-1), (r, c+1).
    #      Decide: read them from I or from Iq? What if a neighbor is also bad?
    #   4. Average those 4 RGB values and store the result in Iq[r, c].
    #   5. (Think) What happens at r = 0 or c = N-1? Do any bad pixels sit there?
   
    # make two arrays rows, cols, where the bad pixels are
    rows, cols = np.where(bad_pixels)
    # index through both using the zip function
    for r, c in zip(rows, cols):
        # initiate an empty list of neighboring pixels to average from
        neighbors = []
        # a sequence of 4 if's that check whether a neighbor can be used
        # inside the image bounds as well as if it is not a bad pixel
        # if those coniditions are met the color channel values are added to 
        # neighbors
        if (r < I.shape[0] - 1) and not (bad_pixels[r+1, c]):
            neighbors.append(I[r+1, c]) 
        if (r >= 1) and not (bad_pixels[r-1, c]):
            neighbors.append(I[r-1, c])
        if (c < I.shape[1] - 1) and not (bad_pixels[r, c+1]):
            neighbors.append(I[r, c+1])
        if (c >= 1) and not (bad_pixels[r, c-1]):
            neighbors.append(I[r, c-1])
        # a check to see if there is a chance that no good neighbors exist
        if len(neighbors) == 0:
            print("no good neighbors at", r, c)
        # average the color channels of good neighbors, and only the colors
        color_channels_average = np.mean(neighbors, axis = 0)
        # put them over the bad pixels in copy of image
        Iq[r, c] = color_channels_average

    return Iq


def _main():
    image_file = sys.argv[1]
    I = imread(image_file)
    I = pixelfix(I)
    imsave('fixed_' + image_file, I)
    print(f"Wrote fixed_{image_file}")


if __name__ == '__main__':
    _main()
