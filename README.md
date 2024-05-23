# LMS algorithm Python

Functionality:

Takes four input arguments:
d: Desired signal (numpy array)
x: Input signal (numpy array)
mu: Learning rate (float)
M: Number of filter coefficients (int)
Uses the LMS algorithm to adapt the filter coefficients to minimize the mean squared error between the desired signal and the filter output.
Returns three outputs:
y: Filtered signal (numpy array)
e: Filtering error (numpy array)
w: Adapted filter coefficients (numpy array)

Example Usage:
Generates test signals: random input signal x and a desired signal d which is a convolution of x with a known impulse and additional noise.
Sets LMS algorithm parameters: learning rate mu and number of filter coefficients M.
Applies the LMS filter to the input signal x to obtain filtered signal y and error e.
Visualizes the results: desired signal, filter output, error.

Additional Information:
The LMS algorithm is a simple and effective method for adaptive filtering.
It can be used for various tasks such as noise reduction, channel equalization, and system identification.
Parameters mu and M significantly affect the filter's performance. Their values are chosen empirically or through theoretical methods.
