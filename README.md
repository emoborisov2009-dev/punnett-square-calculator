Punnett Square Calculator

A Python-based Mendelian genetics calculator that generates Punnett squares and calculates genotype and phenotype ratios.

About the Project

The idea for this project came from a biology lesson about Mendelian genetics and Punnett squares. After learning how allele combinations determine the possible genotypes and phenotypes of offspring, I became interested in whether I could recreate the process using Python.

I decided to turn what I had learned in biology into a programming project, combining two subjects I enjoy.

The program allows users to enter the genotypes of two individuals and automatically generates a Punnett square, calculates possible offspring combinations, and determines genotype and phenotype distributions.

Features
Input validation for parental genotypes
Automatic Punnett square generation
Genotype distribution calculations
Phenotype distribution calculations
Genotype and phenotype ratios
Interactive command-line interface
Option to exit the program
Example

Input:

text
Individual 1: Aa
Individual 2: Aa


Punnett Square:

	A	a
A	AA	Aa
a	Aa	aa

Results:

Genotype distribution: 1 AA, 2 Aa, 1 aa
Genotype ratio: 1:2:1
Phenotype distribution: 3 dominant, 1 recessive
Phenotype ratio: 3:1
Technologies and Concepts
Python 3
Conditional statements
Nested loops
String methods
Variables and counters
Input validation
How to Run
Install Python 3.
Clone or download this repository.
Open a terminal in the project directory.
Run the following command:
bash
python punnett_calculator.py

Scientific Scope

The current version focuses on monohybrid crosses involving one gene with two alleles and complete dominance.

The calculated ratios represent theoretical Mendelian probabilities.

Future Improvements
Support for dihybrid crosses
Additional inheritance patterns
Improved result visualization
Expanded input validation
Author

Developed as an independent programming project inspired by a biology lesson.
