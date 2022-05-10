"""
This module defines functions implementing algorithms in SPM

Here you want the get_spm_globals function from the earlier
``four_dimensions_exercise``, with anything that function imports and other
definitions that the function needs.

See:
    https://bic-berkeley.github.io/psych-214-fall-2016/four_dimensions_exercise.html

In the same directory as this file, you will find a 'tests' directory.

Test this module with:

    python3 findoutlie/tests/test_spm_funcs.py

or better, in IPython::

    %run findoutlie/tests/test_spm_funcs.py
"""

# Any imports you need
import nipraxis
import numpy as np
import nibabel as nib


def spm_global(vol):
    """ Calculate SPM global metric for array `vol`

    Parameters
    ----------
    vol : array
        Array giving image data, usually 3D.

    Returns
    -------
    g : float
        SPM global metric for `vol`
    """

    # - Calculate threshold
    T = np.mean(vol) / 8
    # - Select voxels greater than T
    voxels_within = vol > T
    # - Calculate mean
    mean_over_T = np.mean(vol[voxels_within])
    # Return the result
    return (mean_over_T)


def get_spm_globals(fname):
    """ Calculate SPM global metrics for volumes in image filename `fname`

    Parameters
    ----------
    fname : str
        Filename of file containing 4D image

    Returns
    -------
    spm_vals : array
        SPM global metric for each 3D volume in the 4D image.
    """
    # - Load the image given by "fname".
    img = nib.load(fname)
    # - Get the data
    data = img.get_fdata()
    # - Calculate the SPM global value for each volume.
    spm_vals = []
    for i in range(data.shape[-1]):
        spm_vals.append(spm_global(data[:, :, :, i]))

    return spm_vals  # Return the result.