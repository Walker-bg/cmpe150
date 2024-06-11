# CMPE150 - Introduction to Programming

Welcome to the repository for CMPE150 - Introduction to Programming. This course is the first coding class taken by freshman students at Boğaziçi University, and it introduces fundamental programming concepts using Python.

## Course Information

- **Instructor**: Emre Uğur
- **Semester**: Fall 20

This repository contains the following materials:
- **3 Projects**: Project4, Project5, and Project6
- **Final Exam Questions**
- **Practice Questions**

## Repository Structure

The repository is organized into five main folders: `final`, `practice`, `Project4`, `Project5`, and `Project6`.

```
.
├── Project4
│   ├── description.pdf
│   ├── src
│   │   ├── hw4.py
│   │   └── template.py
│   └── testing
│       ├── cases1  [49 entries]
│       ├── cases2  [50 entries]
│       └── cases3  [600 entries]
├── Project5
│   ├── description.pdf
│   ├── flow-chart.pdf
│   ├── src
│   │   └── hw5.py
│   └── testing
│       ├── bad  [55 entries]
│       ├── handmade  [82 entries]
│       ├── long  [704 entries]
│       └── short  [705 entries]
├── Project6
│   ├── description.pdf
│   ├── src
│   │   └── hw6.py
│   └── testing
│       ├── crime_scene.txt
│       ├── hw6.py
│       ├── solution_part1.txt
│       ├── solution_part2.txt
│       ├── solution_part3.txt
│       ├── test.py
│       └── tests  [1200 entries]
├── README.md
├── final
│   ├── q1
│   │   ├── Q1.py
│   │   ├── Q1_blank.py
│   │   └── q1.html
│   ├── q2
│   │   ├── Q2_blank.py
│   │   ├── Q2.py
│   │   └── q2.html
│   └── q3
│       ├── Q3.py
│       ├── Q3_blank.py
│       └── q3.html
└── practice
    ├── ClassExercise [3 entries]
    ├── RecursionPractice  [14 entries]
    ├── Stuff  [22 entries]
    ├── WeeklyPracticeQuestions  [13 entries]
    └── WeeklyPracticeQuestions2  [14 entries]
```

## Project Details

### Project 4: ASCII Atari-like Game

**Description**:
This project involves creating an interactive Atari-like game in the terminal using Python. The game includes elements like asteroids, firing, time simulation, and an ending that can result in either success or failure.

Check out the [description](Project4/description.pdf) for more details.

- **Inputs**: `x` (length of the asteroid cluster), `y` (width of the asteroid cluster), `g` (distance to the asteroid cluster)
- **Actions**: `left`, `right`, `fire`, `exit`
- **Rules**:
  - `x >= 0`, `y > 0`, `g >= 0`
  - Inputs are always integers.
  - Actions are case insensitive.
  - No functions or imports allowed.

**Files**:
- `description.pdf`: Detailed project description
- `src/`: Contains the source code `hw4.py` and a `template.py`
- `testing/`: Contains test cases

### Project 5: SiNiR Compiler

**Description**:
The project involves implementing a syntax checker for a hypothetical programming language called SiNiR.

Check out the [description](Project5/description.pdf) and [flowchart](Project5/flow-chart.pdf) for more details.

- **Input File**: `calc.in`
- **Output File**: `calc.out`
  - If there is a syntax error, print "Dont Let Me Down".
  - If no syntax errors, print "Here Comes the Sun".

**Files**:
- `description.pdf`: Detailed project description
- `flow-chart.pdf`: Syntax flowchart
- `src/`: Contains the source code `hw5.py`
- `testing/`: Contains various test cases

### Project 6: Knapsack Problem

**Description**:
This project involves solving a knapsack problem with additional dimensions and constraints, helping a detective collect evidence within limited time and weight constraints.

Check out the [description](Project6/description.pdf) for more details.

**Files**:
- `description.pdf`: Detailed project description
- `src/`: Contains the source code `hw6.py`
- `testing/`: Contains test files and additional resources

## Final Exam Questions

The `final` folder contains three questions from the final exam, each with:
- A blank template Python file
- A solution Python file
- An HTML file with the question description

## Practice Questions

The `practice` folder contains various Python files used for practice, organized into subfolders such as `ClassExercise`, `RecursionPractice`, `Stuff`, `WeeklyPracticeQuestions`, and `WeeklyPracticeQuestions2`.

## How to Use This Repository

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the desired project or folder**:
   ```bash
   cd ProjectX
   ```
3. **Read the description files**: Each project contains a `description.pdf` file with detailed instructions.
4. **Run the source code**: Source files are located in the `src/` directory of each project.
5. **Test your solutions**: Use the provided test cases in the `testing/` directory to validate your solutions.

## License

This repository is licensed under the MIT License. See the `LICENSE` file for more details.
