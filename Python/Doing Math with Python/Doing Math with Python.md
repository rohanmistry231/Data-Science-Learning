 Doing Math with Python

Sample solutions of program challenges:https://nostarch.com/doingmathwithpython


# 00 Introduction

## Tip: how to clear screen

### Terminal in VS Code

#### import os
# Clearing the Screen
os.system('cls')

### Python IDLE (tricky way)

#### def cls(): print("\n" * 40)
cls()

# 01 Working with Numbers

Within this chapter:

- you learn to write programs that recognize integers, floating point numbers, fractional numbers (expressed as a fraction or a floating point number), and complex numbers.
- you write programs that generate multiplication tables, perform unit conversions, and find the roots of a quadratic equation


## 01-01 Basic Mathematical Operations

### addition (+)

### subtraction (-)

### multiplication (*)

### division (/)

#### floor division (//)

#### modulo (%)

### exponential (**)

#### square root: x ** (1/2)

#### cube root: x ** (1/3)

### Python will evaluate the expression following the standard PEMDAS rule for the order of calculations

#### PEMDAS: Parentheses, Exponents, Multiplications, division, addition, subtraction

## 01-02 Labels: Attaching Names to Numbers

## 01-03 Different Kinds of Numbers

### Data Type

#### Use type() to check the kind of number (or variable)

#### int(), float(), etc.. used to convert the data type

### 01-03-01 Working with Fractions

#### from fractions import Fraction

#### <class 'fractions.Fraction'>

#### Fraction(a,b) or Fraction(a/b) ==>
Fraction(numerator, denominator)

### 01-03-02 Complex Numbers

#### <class 'complex'>: a+bj

#### .real and .imag: get real and imaginary part separately

#### .conjugate(): same real part but an imaginary part with an equal magnitude and an opposite sign

#### magnitude of a complex number:
(z.real ** 2 + z.imag ** 2) ** 0.5  <--> abs(z)

## 01-04 Getting User Input

### 01-04-01 Handling Exceptions and Invalid Input

#### try:
    STATEMENT
except ErrorType:
    print("customized error message")

### 01-04-02 Fractions and Complex Numbers as Input

#### a = Fraction(input('Enter a fraction: '))

#### z = complex(input('Enter a complex number: '))

## 01-05 Writing Programs that Do the Math for you

### 01-05-01 Calculating the Factors of an Integer

#### 01-01_is_factor_checking.py

#### 01-02_factors-finder.py

### 01-05-02 Generating Multiplication Tables

#### 01-03_linear-multiplication-table.py

#### 01-04_Chinese-multiplication-table.py

#### 01-05_Chinese-multiplication-table-new.py

### 01-05-03 Converting Units of Measurement

#### 01-06_mile-km-converter.py

#### 01-07_temperature-converter.py

### 01-05-04 Finding the Roots of a Quadratic Equation

#### 01-08_quadratic-equation-roots-calculator.py

## 01-06 Programming Challenges

### 1. Even-Odd Vending Machine

#### 01-09_even-odd-vending-machine.py

### 2. Enhanced Multiplication Table Generator

#### 01-10_enhanced-multiplication-table.py
 (see:01-05-02 Generating Multiplication Tables)
### 3. Enhanced Unit Converter

#### 01-11_enhanced-unit-converter.py
 (see:01-05-03 Converting Units of Measurement)
### 4. Fraction Calculator

#### 01-12_fraction-calculator.py
 (see:01-03-01 Working with Fractions)
### 5. Give Exit Power to the User

#### 01-13_run-until-exit.py

#### 01-14_enhanced-unit-converter-with-exit.py
 (see:3. Enhanced Unit Converter)
# 02 Visualizing Data with Graphs

In this chapter, you'll learn a powerful way to present numerical data: by drawing graphs with Python.

- We'll start by discussing the number line and the Cartesian plane.
- Next, we'll learn about the powerful plotting librarymatplotlib and how we can use it to create graphs.
- We'll then explore how to make graphs that present data clearly and intuitively.
- Finally, we'll use graphs to explore Newton's Law of Universal Gravitation and projectile motion.


## 02-01 Understanding the Cartesian Coordinate Plane
 (see:05-01 What's a Set?)
## 02-02 Working with Lists and Tuples

### List vs Tuple

#### List

##### After you create a list, it's possible to add values to it and to change the order of the values

##### A list is the best choice for storing data if you don't know beforehand how many numbers or strings you may need to store

#### Tuple

##### The values in a tuple are immediately fixed and can't be changed

### 02-02-01 Iterating over a List or Tuple

#### for index, item in enumerate(l):

## 02-03 Creating Graphs with Matplotlib

### 02-03-01 Marking Points on Your Graph

#### 02-03_01.py

### 02-03-02 Graphing the Average Annual Temperature

#### 02-03_01.py

### 02-03-03 Comparing the Monthly Temperature Trends

#### 02-03_01.py

### 02-03-04 Customizing Graphs

#### Adding a Title and Labels

##### 02-03_02.py

#### Customizing the Axes

##### 02-03_02.py

#### Plotting Using pyplot

##### 02-03_03.py

##### 02-03_04.py

### 02-03-05 Saving the Plots

#### 02-03_05.py

## 02-04 Plotting with Formulas

### 02-04-01 Newton's Law of Universal Gravitation

#### 02-04_01-univeral-gravitation.py

#### 02-04_01-univeral-gravitation-adjustable.py

### 02-04-02 Projectile Motion

#### Generating Equally Spaced Floating Point Numbers

##### 02-04_02-1-Drawing-Trajectory.py

#### Drawing the Trajectory

##### 02-04_02-1-Drawing-Trajectory.py

#### Comparing the Trajectory at Different Initial Velocities

##### 02-04_02-2-Comparing-Trajectory.py

## 02-05 Programming Challenges

### 1. How Does the Temperature Vary

#### 02-05_1_Temperature-of-a-Day.py

### 2. Explorting a Quadratic Function Visually

#### 02-05_2_visaulize-quadratic-function.py

### 3. Enhanced Projectile Trajectory Comparison

#### 02-05_3_Comparing-Trajectory_Enhanced

### 4. Visualizing Your Expenses

#### 02-05_4-1_daily-steps.py

#### 02-05_4-2_personal-expense.py

### 5. Exploring the Relationship Between the Fibonacci Sequence and the Golden Ratio

#### 02-05_5-1_Fibonacci-and-Golden-Ratio.py

#### 02-05_5-2_Fibonacci-and-Golden-Ratio.py

# 03 Describing Data with Statistics

In this chapter:

- We'll use Python to explore statistics so we can study, describe, and better understand sets of data.
- After looking at some basic statistical measures -- the mean, median, mode, and range -- we'll move on to some more advanced measures, such as variance and standard deviation
- We'll see how to calculate the correlation coefficient, which allows you to quantify the relationship between two sets of data
- We'll end the chapter by learning about scatter plots.
- We'll learn more about the Python language and standard library modules.


## 03-01 Finding the Mean

### The "average" number; found by adding all data points and dividing by the number of data points
 
It's best to use themean  to describe the center of a dataset when the distribution is mostly symmetrical and there are no outliers


### 03-01_finding-mean.py

## 03-02 Finding the Median

### The middle number; found by ordering all data points and picking out the one in the middle (or if there are two middle numbers, taking the mean of those two numbers)

### It's best to use the median when the distribution is either skewed or there are outliers present

### 03-02_finding-median.py

## 03-03 Finding the Mode and Creating a Frequency Table

### 03-03-01 Finding the Most Common Elements

#### Count how many times each unique number occurs and find the one that occurs the most.

#### from collections import Counter
Counter(list).most_common()
mode = Counter(list).most_common(1)

#### 03-03_1_fining-most-common-elements.py

### 03-03-02 Finding the Mode

#### 03-03_2_fining-mode.py

#### 03-03_3_fining-multiple-modes.py

### 03-03-03 Creating a Frequency Table

#### 03-03_4_frequency-table.py

#### 03-03_5_frequency-table-sorted.py

## 03-04 Measuring the Dispersion (分散)

Thedispersion tells us how far away the numbers int he set of data are from the mean of the data set.


### 03-04-01 Finding the Range of a Set of Numbers
 
For a list of numbers, therange  is the difference between the highest number and the lowest number


#### You could have two groups of numbers with the exact same mean but with vastly different ranges, so knowing the range fills in more information about a set of numbers
 (see:03-01 Finding the Mean)
#### 03-04_1_finding-range.py

### 03-04-20 Finding the Variance and Standard Deviation
 
Thevariance is the average of the squares of those differences of each of the numbers from themean.

 (see:Standard Deviation is the square root of the variance)
##### A high variance means that values are far from the mean.

##### A low variance means that the values are clustered close to the mean.

#### Standard Deviation is the square root of the variance

##### Values that are within ONE standard deviation of the mean can be thought of as fairly typical.
 
Values that are THREE or MORE standard deviations away from the mean can be considered much more atypical -- we call such valuesoutliers

 (see:It's best to use the median when the distribution is either skewed or there are outliers present)
#### 03-04_2_finding-variance-sd.py

## 03-05 Calculating the Correlation Between Two Data Sets

In this section, we'll learn how to calculate a statistical measure that tells usthe nature and strength of the relationship between two sets of numbers: thePearson Correlation Coefficient.

This coefficient measures the strength of thelinear relationship.

The coefficient can be either positive or negative, and its magnitude can range between -1 and 1 (inclusive).



"Correlation 相关性 doesn't imply causation 因果关系."

 (see:1. Better Correlation Coefficient)
### 03-05-01 Calculating the Correlation Coefficient

#### 03-05_1_finding-correlation.py

### 03-05-02 High School Grades and Performance on College Admission Tests
 (see:03-06 Scatter Plots)
#### 03-05_2_correlation_analysis.py

## 03-06 Scatter Plots

### 03-06_scatter-plot.py

## 03-07 Reading Data from Files

### 03-07-01 Reading Data from a Text File
 (see:2. Statistics Calculator)
#### 03-07_1_read-text-file-and-sum.py

#### 03-07_2_read-text-file-and-calc-in-list.py

#### 03-07_3_read-text-file-by-inputname.py

### 03-07-02 Reading Data from a CSV File
 (see:3. Experiment with other CSV Data)
#### 03-07_4_read-csv-and-plot.py

#### 03-07_5_read-trend-csv-and-plot.py

## 03-08 Programming Clallenges

### 1. Better Correlation Coefficient

#### 03-08_1_better_finding-correlation.py

### 2. Statistics Calculator

#### 03-08_2_statistics-calculator.py

### 3. Experiment with other CSV Data

#### US Population Data

#### 03-08_3_US-population-trends.py

### 4. Finding the Percentile (百分位数)

#### 03-08_4_1-find-percentile-score.py

#### 03-08_4_2-find-percentile-score.py

### 5. Creating a Grouped Frequency Table

#### 03-08_5_grouped-frequency-table.py

# 04 Algebra and Symbolic Math with Sympy

We learn how to write programs that can solve symbolic math problems.

We will use SymPy - a Python library that lets you write expressions containing symbols and perform operations on them.


## 04-00 Installing SymPy

### Prerequisite: pip3 install mpmath

### pip3 install sympy

#### Verify of Installation: from sympy import *

### Usage

#### import sys
import mpmath
from sympy import *

### Testing

#### After import sympy, execute below:
>>> x = Symbol('x')
>>> limit(sin(x)/x, x, 0)
1
>>> integrate(1/x, x)
log(x)

### SymPy Introductory Tutorial

## 04-01 Defining Symbols and Symbolic Operations

### Symbols form the building blocks of symbolic math (符号数学).

### Define single symbol

#### from sympy import Symbol
x = Symbol('x')

### Define multiple symbols

#### from sympy import symbols
x,y,z = symbols('x,y,z')
 
SymPy automatically simplifies only themost basic of expressions and leaves it to the programmer to explicitly require simplification in cases such as the one e.g. (x+2)*(x-3)

 
If you want to multiply out the expression to get the expanded version, you'll have to use theexpand()  function


## 04-02 Working with Expressions

### 04-02-01 Fractorizing and Expanding Expressions

#### factorize: 因式分解

##### from sympy import factor
expr = x**2 - y**2
factor(expr)  # (x-y)*(x+y)

#### expand: 多项式展开

##### from sympy import expand
factors = factor(expr)
expand(factors)

### 04-02-02 Pretty Printing

#### from sympy import pprint
pprint(expr)

#### 04-02-02-01 Printing a Series
 (see:3. Summing a Series)
##### 04-02_1_printing-series.py

### 04-02-03 Substituting (替代) in Values

#### expr = x*x + 2*x*y + y*y
res = expr.subs({x:1, y:2})

#### from sympy import simplify
expr_subs = expr.subs({x:1-y})
simplify(expr_subs)

#### 04-02-03-01 Calculating the Value of a Series

##### 04-02_2_culculate-value-of-series.py

### 04-02-04 Converting Strings to Mathematical Expressions

#### sympify(): converts that string into a SymPy object that makes it possible to apply SymPy's functions to the input

#### from sympy import sympify

#### from sympy.core.sympify import SympifyError
try:
except SimpifyError:

##### 04-02_3_simpify-error-handling.py

#### 04-02-04-01 Expression Multiplier

##### 04-02_4_expression-multiplier.py

## 04-03 Solving Equations

### from sympy import Symbol, solve
x = Symbol('x')
expr = x - 5 - 7
solve(expr) # assuming the expr is equal to zero

### 04-03-01 Solving Quadratic Equations (二次方程)

### 04-03-02 Solving for One Variable in Terms of Others

### 04-03-03 Solving a System of Linear Equations

## 04-04 Plotting Using SymPy

### from sympy.plotting import plot

### 04-04-01 Plotting Expressions Input by the User

#### 04-04_1_plotting-exression.py

### 04-04-02 Plotting Multiple Functions

#### 04-04_2_two-line-plotting.py

## 04-05 Programming Challenges

### 1. Factor Finder

#### 04-05_1_factor-finder.py

### 2. Graphical Equation Solver

#### 04-05_2_graphical-equation-solver.py

### 3. Summing a Series

#### from sympy import summation
s = summation(x**n/n, (n,1,5))

#### 04-05_3_summing-a-series.py

### 4. Solving Single-Variable Inequalities

#### inequality-solving function
(from sympy import Poly)

##### polynomial function
 
Apolynomial (多项式) is an algebraic expression consisting of a variable and coefficients and involving only the operations of addition, subtraction, and multiplication, and only positive powers of the variable. e.g. x**2 + 4 < 0


###### from sympy import solve_poly_inequality

##### retional function
 
Arational expression is an algebraic expression in which the numerator and denominator are both polynomials. e.g. ((x-1)/(x+2)) > 0


###### from sympy import solve_rational_inequalities

##### all other inequalities

###### e.g. sinx - 0.6 > 0

###### from sympy import solve_univariate_inequality, sin

# 05 Playing with Sets and Probability

- We will start by learning how we can make our programs understand and manipulate sets of numbers.
- We'll see how sets can help us understand basic concepts in probability.
- We'll learn about generating random numbers to simulate random events.


## 05-01 What's a Set?
 
A set is a collection ofdistinct objects, often calledelementsormembers.


#### The set is "well defined", meaning the question "Is a particular object in this collections?" always has a clear Yes or No answer, usually based on a rule or some given criteria.

#### No two members of a set are the same!

### 05-01-01 Set Construction

#### from sympy import FiniteSet

#### 05-01-01-01 Checking Whether a Number Is in a Set

#### 05-01-01-02 Creating an Empty Set

#### 05-01-01-03 Creating Sets from Lists or Tuples

#### 05-01-01-04 Set Repetition and Order

##### FiniteSet(*members)

### 05-01-02 Subsets, Supersets, and PowerSets
 
A set,s, is asubset  of another set,t, if all the members ofsare also members oft. --> is_subset()

 
A set,t, is said to be asuperset  of another set,s, ift  contains all of the members contained ins. --> is_superset()

 
Thepowerset of a set,s, is the set of all possible subsets ofs. --> powerset()


#### Using len() to find set's cardinality.

#### is_proper_subset(), is_proper_superset()

### 05-01-03 Set Operations

#### Union and Intersection

##### set1.union(set2)

##### set1.intersect(set2)

#### Cartesian Product (笛卡尔积)

##### product=set1 * set2

#### Applying a Formula to Multiple Sets of Variables

##### 05-01_1_pendulum-single-set.py

#### Different Gravity, Different Results

##### 05-01_2_pendulum-multi-set.py

### Sets allows us to reason about the basic concepts of probability

## 05-02 Probability

### Some Probability Definitions

#### Experiment: is simply the test we want to perform. We perform the test because we are interested in the probability of each possible outcome.

#### Sample Space: all possible outcomes of an experiment form a set known as the sample space, whcih we'll usually call S in our formulas.

#### Event: a set of outcomes that we want to calculate the probability of and that from a subset of the sample space.

#### Uniform Distribution: each outcomes in the sample space is equally likely to occur, formula is P(E) = n(E) / n(S), P(E) is the probability of an event, n(E) is the cardinality of the sets E (event), n(S) is the cardinality of the sets S (sample space)

##### def probability(space, event):
    return len(event)/len(space)

#### 05-02_1_prime-in-20-side-die.py

#### 05-02_2_prime-in-n-sided-die.py

### 05-02-01 Probability of Event A or Event B

#### len(a union b) / len(s)

### 05-02-02 Probability of Event A and Event B

#### len (a intersect b) / len(s)

### 05-02-03 Generating Random Numbers

#### 05-02-03-01 Simulating a Die Roll

##### import random
random.randint(1,6)

#### 05-02-03-02 Can You Roll That Score?

##### 05-02_3_roll-die-till-a-score.py

#### 05-02-03-03 Is the Target Score Possible?

##### 05-02_4_roll-till-target-score.py

### 05-02-04 Nonuniform Random Numbers

#### 05-02_5_unequal-coin-rolling.py

#### 05-02_6_fictional-ATM.py

## 05-03 Programming Challenges

### 1. Using Venn Diagrams to Visualize Relations

#### Venn Diagram (wikipedia), also called set diagram or logic diagram, shows all possible logical relations between a finite collection of different sets.

#### 05-03_1_1_basic-venn-diagram.py

#### 05-03_1_2_student-sports.py

### 2. Law of Large Numbers

#### 05-03_2_1_law-of-large-number.py

#### 05-03_2_2_law-of-large-number-plotting.py

### 3. How Many Tosses Before you Run Out

#### 05-03_3_coin-toss-game.py

### 4. Shuffling (洗牌) a Deck of Cards

#### random.shuffle(list): The shuffle() is an inbuilt method of the random module. It is used to shuffle a sequence (list). Shuffling a list of objects means changing the position of the elements of the sequence using Python.

#### 05-03_4_1_shuffle-numbers.py

#### 05-03_4_2_shuffle-deck-of-cards.py

#### 05-03_4_3_shuffle-deck-of-cards-using-set.py

### 5. Estimating the Area of a Circle

#### 05-03_5_1_estimate-area-of-circle.py

#### 05-03_5_2_estimate-area-of-circle-plot.py

#### 5.1 Estimating the Value of Pi

##### 05-03_5_3_estimate-pi.py

# 06 Drawing Geometric Shapes and Fractals

- We'll learn about patches in matplotlib that allow us to draw geometric shapes, e.g. circles, triangles, and polygons.
- We'll learn about matplotlib's animation support and write a program to animate a projectile's trajectory
- We'll learn how to drawfractals -- complex geometric shapes created by the repeated applications of simple geometric transformations.


## 06-01 Drawing Geometric Shapes with Matplotlib's Patches

### 06-01-01 Drawing a Circle

#### 06-01_1_draw-circle.py

### 06-01-02 Creating Animated Figures

#### matplotlib.animation.FuncAnimation

#### Animations & Object Persistence #1656

#### 06-01_2_create-animated-figure.py

### 06-10-03 Animating a Projectile's Trajectory

#### 06-01_3_animating-projectile-trajectory.py

## 06-02 Drawing Fractals (分形)

### 06-02-01 Transformations of Points in a Plane

#### 06-02_1_zigzag-path.py

#### 06-02_2_zigzag-path-enhanced.py

### 06-02-02 Drawing the Barnsley Fern (巴恩斯利蕨)
 (see:2. Drawing the Sierpinski Triangle (谢尔宾斯基三角))
#### 06-02_3_Barnsley-Fern.py

## 06-03 Programming Challenges

### 1. Packing Circles into a Square

#### 06-03_1_1_draw-square.py

#### 06-03_1_2_packing-circles-in-a-square.py

### 2. Drawing the Sierpinski Triangle (谢尔宾斯基三角)

#### 06-03_2_Sierpinski-Triangle.py

### 3. Exploring Henon's Function (海农函数)

### 4. Drawing the Mandelbrot Set (曼德尔布罗特集)

#### 4.1 The imshow() Function

##### Display data as an image, i.e., on a 2D regular raster (常规光栅).

##### imshow documentation in matplotlib.org

##### matplotlib.pyplot.imshow(X, cmap=None, norm=None, *, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, interpolation_stage=None, filternorm=True, filterrad=4.0, resample=None, url=None, data=None, **kwargs)

#### 4.2 Creating a List of Lists

##### 06-03_4_1_gray-level-headmap.py

#### 4.3 Drawing the Mandelbrot Set

##### 06-03_4_2_mandelbrot-set.py

# 07 Solving Calculus Problems

- We'll learn to solve calculus problems.
- We'll first learn about mathematical functions, followed by a quick overview of the common mathematical functions available in Python's standard library and SymPy.
- We'll then learn how we can find the limits of functions and calculate derivatives and integrals.


## 07-01 What is a Function?
 
A function is amapping between an input set and an output set.


### 07-01-01 Domain and Range of a Function
 
Thedomain of a function is the set of input values that the independent vairable can validly assume.

 
The output set of a function is called therange.


### 07-01-02 An Overview of Common Mathematical Functions

## 07-02 Assumptions in SymPy

## 07-03 Finding the Limit of Functions
 (see:1. Verify the Continuity of the Function)
### 07-03-01 Continuous Compound Interest

### 07-03-02 Instantaneous Rate of Change

## 07-04 Finding the Derivative (导数) of Functions
 
By default, creating the derivative object usingDerivative  class finds the first-order derivative

 (see:To find higher-order derivatives, specify the order of the derivative to calculate as the 3rd argument)
#### Derivative(f,x)

### 07-04-01 A Derivative Calculator

#### 07-04_derivative-calculator.py

### 07-04-02 Calculating Partial Derivatives

## 07-05 Higher-Order Derivatives and Finding the Maxima

### To find higher-order derivatives, specify the order of the derivative to calculate as the 3rd argument

#### # order = n (n>=2)
Derivative(f,x,n)

### 07-05_find-maxima-minima.py

## 07-06 Finding the Global Maximum Using Gradient Ascent (梯度上升法)
 (see:2. Implement the Gradient Descent)
### 07-06-00 Basic grad_ascent() function

#### 07-06_1_basic-gradient-ascent-function.py

### 07-06-01 A Generic Program for Gradient Ascent

#### 07-06_2_generic-gradient-ascent-function.py

### 07-06-02 A Word of Warning About the Initial Value

### 07-06-03 The Role of the Step Size and Epsilon

#### 07-06_3_enhanced-gradient-ascent-function.py

## 07-07 Finding the Integrals of Functions

## 07-08 Probability Density Functions

## 07-09 Programming Challenges

### 1. Verify the Continuity of the Function

#### Learning: Continuity at a Point

#### 07-09_1_vefiry-continuity.py

### 2. Implement the Gradient Descent

### 3. Area Between Two Curves

### 4. Finding the Length of a Curve

# Appendix A: Software Installation

## Anaconda

## SymPy
 (see:04-00 Installing SymPy)
### conda install sympy=0.7.6

## Installing matplotlib-venn
 (see:1. Using Venn Diagrams to Visualize Relations)
### $ pip install matplotlib-venn

## Starting the Python Shell

# Appendix B: Overview of Python Topics

## B-01 if __name__ == '__main__'

## B-02 List Comprehensions

## B-03 Dictionary Data Structure

## B-04 Multiple Return Values

## B-05 Exception Handling

### B-05-01 Specifying Multiple Exception Types

### B-05-02 The ELSE Block

## B-06 Reading Files in Python
 (see:03-07 Reading Data from Files)
### B-06-01 Reading All the Lines at Once

### B-06-02 Specifying the Filename as Input

### B-06-03 Handling Errors When Reading Files

## Reusing Code
