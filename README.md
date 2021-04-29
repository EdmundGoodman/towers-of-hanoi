# towers-of-hanoi
A set of programs showing the approach I took to solving the [towers of hanoi problem](https://en.wikipedia.org/wiki/Tower_of_Hanoi), written as an extra-curricular school project, in Python.

Below is a short write-up of the reasoning behind doing, the approach taken to, and the conclusions drawn from this excercise

### Introduction
I attempted this project over an afternoon to try and excersise my ability to take an unknown problem, and produce an algorithmic approach to solving it.

Firstly, I wrote an object to model the towers of hanoi set, which is a wrapper for a 2d list, a list of 3 stacks. It includes methods to print the board, move the peices, and check if the game has been won "gameboard.py".

### First steps
Next, I considered how I would approach solving cases of it for small stacks. "examples.py" contains a function which stores a hard-coded approach to solving stacks of height one to five.

### Halfway houses
From this, I looked for patterns in my hard-coded approaches to the small test cases. It turned out that the solution to a given height can be expressed as moving all but the bottom disc to the middle tower, then the bottom disc to the far tower, then all but the bottom disc to the far tower. I wrote this as a half hard-coded function in "halfrecursive.py". It is worth noting even incompletely implemented, this is much shorter than the initial testing code.

### The final algorithm
The final algorithm took the recursive approach above, and generalised it to any tower height, forming a recursive stack call, and switching the target post as it traversed it. This worked perfectly for all tower heights, hence acheiving better results in ~5 lines than the first attempt did in ~65 lines.

### Conclusions
My final solution was satisfyingly close the the accepted recursive solution, with the only difference being variable names, despite the fact I had never seen it before. The fact that effective solutions can be achieved independently to the same problem makes me hopeful in the beauty of nature. Furthermore, the approach of considering simple cases to the problem, and turning them stepwise into a general solution is a useful technique to be exposed to.
