# Visualize equimaterial zones on a rolled cylinder

import numpy as np
import matplotlib.pyplot as plt

def product_remaining(r, R_new=3):
    """Fraction of product remaining by visible roll radius.

    Parameters
    ----------
    r : float, 1 <= r
        Visible radius of roll in units of r0, the cardboard cylinder radius.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0.

    Returns
    -------
    Current remaining length as fraction of original length of new roll.
    """

   
    r_0 = R_new / 3

    f_x = (r**2 - r_0**2) / (R_new**2 - r_0**2)

    return f_x 

def product_visible(el_frac, R_new=3):
    """Visible roll radius by fraction of remaining product.

    Parameters
    ----------
    el_frac : float, 0 <= el_frac <= 1
        Current remaining length as fraction of original length of new roll.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.

    Returns
    -------
    Current visible radius of roll, in units of r0, the cardboard cylinder
    radius.
    """
    r_0 = R_new / 3

    r = np.sqrt((R_new**2 - r_0**2) * el_frac + r_0**2)

    return r

def visualize_danger(n, R_new=3, saveas=''):
    """Use n line segments of equal product to visualize paradox of the roll.

    Parameters
    ----------
    n : int scalar
        Number of line segments to display.
    R_new : scalar, optional, default: 3
        Radius of roll when new, in units of r0, the cardboard cylinder radius.
    saveas : str, optional, default: empty
        If not empty save figure to file 

    Returns
    -------
    None
    """

    # Start with a new figure window
    plt.close('all') # this helps get rid of old figures you forgot to close
    fh = plt.figure(figsize=(8,6)) # my favorite figure size

    ### YOUR CODE HERE ###
    ax = fh.add_subplot()
    fh.subplots_adjust(top=0.88, bottom=0.18)  # room for header and caption

    # Do the core plotting commands here
    ## use the functions defined above to calculate the line segments to plot
    theta = np.linspace(0, 2 * np.pi, 400)
    r_tube = product_visible(0, R_new)  # empty roll = bare cardboard tube
    ax.fill(r_tube * np.cos(theta), r_tube * np.sin(theta), color='dimgray')
    label_size = max(5, 14 - n)  # labels shrink as rings crowd together
    for k in range(1, n + 1):
        r_k = product_visible(k / n, R_new)  # ring k holds k/n of the roll
        ax.plot(r_k * np.cos(theta), r_k * np.sin(theta), color='black', lw=1.2)
        ax.text(r_k, 0, str(k), rotation=90, ha='center', va='center',
                fontsize=label_size,
                bbox=dict(facecolor='white', edgecolor='none', pad=1))

    # Set axes properties here for a better view
    ## things like axis limits and tick marks
    lim = 1.1 * R_new
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')  # circles stay circles, frame stays square

    # Stylize and annotate
    ## things like axes labels, font sizes, or any other finishing touches
    ax.set_xlabel('core radii', loc='left', fontsize=12)
    ax.set_title(f'Toilet Paper Roll of {n} Equal Layers of Paper', fontsize=14)  # EDIT HERE: your header text
    fh.text(0.5, 0.04, 'A representation of what a toilet paper roll with a center tube of 1/3 total radius looks like with n layers, spaced in such a manner that reflects the visible product.', ha='center', fontsize=10, wrap=True)  # EDIT HERE: your caption

    ######################

    # Finally, show on screen and/or save to file
    if saveas:
        plt.savefig(saveas)
    plt.close()   # figures in this course are files: look at the saved PNG (plt.show() would pop a window instead)

if __name__ == '__main__':
    visualize_danger(5, saveas='roll_paradox_5.png')
    visualize_danger(3, saveas='roll_paradox_3.png')
    visualize_danger(9, saveas='roll_paradox_9.png')