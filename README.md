# EAI320_Practical-3

# Implemented By: Mohamed Ameen Omar
# EAI 320 - Intelligent Systems, University of Pretoria

## Practical Assignment 3

### Compiled by Dr J. Dabrowski

### Compiled, edited, and reviewed by Johan Langenhoven

### 16 February 2018


## 1 Scenario

A new hospital is to be built within the city where you reside. The city council has
asked you to help determine the optimal location of the new hospital. The objective is
to place the hospital at a location such that the response time to any medical emergency
is minimised. A medical emergency could occur anywhere in the city. The city is divided
up into a 16×16 grid as illustrated below.

There is a river that flows through the city as indicated by the blue line. There are two
bridges over the river at locations [3,8] and [10,8]. These are illustrated by the green
markers.

You have been provided with the results of a survey. The results include number of
medical emergencies in each block over a period of a year. This data is provided in the
following Numpy array:


```
w = np.array(
[[2, 1, 7, 9, 1, 9, 3, 12, 12, 2, 13, 12, 11, 10, 8, 12;
1, 1, 2, 4, 8, 6, 2, 12, 5, 4, 17, 16, 8, 6, 10, 8;
4, 1, 7, 12, 6, 10, 1, 2, 2, 2, 7, 4, 15, 1, 5, 10;
7, 12, 7, 2, 6, 6, 13, 9, 12, 4, 23, 14, 15, 12, 1, 8;
10, 11, 8, 7, 8, 7, 8, 7, 16, 15, 2, 15, 3, 14, 6, 10;
8, 1, 4, 1, 7, 6, 2, 9, 3, 13, 10, 15, 6, 3, 8, 7;
5, 8, 5, 5, 10, 6, 8, 10, 2, 8, 12, 10, 1, 8, 8, 10;
6, 12, 5, 5, 12, 2, 7, 2, 2, 11, 3, 5, 6, 10, 10, 7;
11, 4, 8, 12, 10, 4, 5, 12, 1, 4, 6, 1, 6, 2, 9, 12;
8, 1, 7, 4, 6, 11, 8, 7, 10, 6, 5, 2, 5, 1, 12, 2;
4, 5, 8, 6, 1, 11, 5, 12, 6, 5, 7, 4, 12, 6, 8, 11;
7, 10, 2, 6, 12, 6, 4, 8, 7, 8, 11, 11, 6, 2, 11, 2;
11, 8, 8, 11, 5, 8, 4, 2, 8, 12, 5, 12, 10, 12, 2, 10;
2, 6, 10, 1, 10, 10, 5, 1, 11, 4, 8, 6, 8, 12, 11, 6;
11, 12, 5, 10, 11, 2, 1, 1, 2, 10, 12, 12, 11, 12, 12, 8;
2, 1, 5, 7, 11, 7, 5, 2, 4, 7, 11, 1, 4, 12, 4, 5]])
```
Furthermore, it is found that the average response time in minutes is 2.4 + 4. 5 d, where
dis the Euclidean distance from the hospital to the location of the emergency. With
this information, a suitable cost function for a proposed location is given by

```
Cloc=
```
#### ∑^16

```
i
```
#### ∑^16

```
j
```
```
wi,j·TR (1.1)
```
wherewi,j is the number of medical emergencies in blocki, j, and TR is the average
response time.

The cost function represents thetotalcost associated with a specific location for the
hospital. Each possible hospital location will have a different cost.

## Question 1

Create a function in Python to compute the distance between a block in the city and the
hospital, taking into account the river and bridges. To cross a bridge, you will calculate
the Euclidean distance from a block to the bridge, and then from the bridge to the
hospital.

Create a function in Python that implements the cost function presented in equation
1.1. Plot the three dimensional cost surface for equation 1.1 over the grid space. Note
where the global minimum is. To do this, you will iterate through the entire search
space, placing the hospital in each possible location, and then evaluating the cost.

## Question 2

Implement a genetic algorithm (GA) to search for the solution of the optimal hospital
location. Your population will exist out of a set of different possible locations for the


hospital. It is up to you to decide the population size, and the mutation rate of the
algorithm, as well as how to repopulate the population after elimination of the weak
genes, and crossover has been done.

Please ensure that you indicate the following in your report:

1. How the chromosomes are represented.
2. The size of the population used.
3. How the selection step in the GA is performed.
4. How the crossover step in the GA is performed.
5. How the mutation step in the GA is performed.
6. The number of algorithm iterations required to find a solution.
7. The optimal location for the hospital.

Include any possible changes you would have/could have made if you chose to approach
the problem differently.

## Report

You have to write a short technical report for this assignment. Your report must be
written in LATEX. In the report you will give your results as well as provide a discussion
on the results. Make sure to follow the guidelines as set out in the separate questions
to form a complete report.

Reports will only be handed in as digital copies, but a hard copy plagiarism statement
needs to be handed in at the following week’s practical session (on the final day of the
practical submission).

## Deliverables

- Write a technical report on your finding for this assignment.
- Include your code in the digital submission as an appendix.

## Instructions

- All reports must be in PDF format and be named report.pdf.
- Place the software in a folder called SOFTWARE and the report in a folder called
    REPORT.
- Add the folders to a zip-archive and name itEAI320_prac3_studnr.zip.


- All reports and simulation software must be e-mailed toup.eai320@gmail.com
    no later than 16:00 on 01 March 2018. No late submissions will be accepted.
- Use the following format for the subject header for the email: EAI 320 Prac 3 -
    studnr.
- Upload your reportwithoutthe plagiarism statement to TurnItIn before 16:00, 01
    March 2018.
- Bring your plagiarism statement to the practical session on Thursday, 01 March
    2018, where they will be collected.
- No hard-copy of the report is required.

## Additional Instructions

- Do not copy! The copier and the copyee (of software and/or documentation) will
    receive zero for both the software and the documentation.
- For any questions or appointments email me atup.eai320@gmail.com.
- Make sure that you discuss the results that are obtained. This is a large part of
    writing a technical report.

## Marking

Your report will be marked as follow:

- 60% will be awarded for the full implementation of the practical and the subsequent
    results in the report. For partially completed practicals, marks will be awarded as
    seen fit by the marker.Commented code allows for easier marking!
- 40% will be awarded for the overall report. This includes everything from the
    report structure, grammar and discussion of results. The discussion will be the
    bulk of the marks awarded.


