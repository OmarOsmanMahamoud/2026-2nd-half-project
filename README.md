# Solar System Gravitational Simulation

## Overview

This project explores the numerical simulation of gravitational interactions in the Solar System. Development began on July 9, 2026, with the aim of progressively extending the physical model and improving the numerical methods and computational algorithms used.

The initial implementation is written in Python. A C++ implementation is currently under development, with a focus on algorithmic efficiency and data structures for large-scale gravitational simulations.

## Current implementation

The Python version models the gravitational interactions between the Sun and the eight planets using a direct pairwise calculation.

* **Algorithm:** direct gravitational interaction calculation using nested loops
* **Computational complexity:** \(O(N^2)\) per force evaluation
* **Visualization:** static trajectory plots using Matplotlib
* **Implementation status:** initial working version

This implementation provides a baseline for testing numerical methods and evaluating alternative approaches to gravitational force computation.

## Numerical methods

The current Python implementation uses **symplectic Euler** for numerical integration.

An important aspect of the project is understanding how the choice of integrator affects accuracy, stability and the long-term behaviour of gravitational simulations.


## Planned developments

The main development goals are:

* Implement a Barnes–Hut tree algorithm to reduce the computational cost of gravitational force evaluation.
* Develop the data structures required for tree-based spatial decomposition, including quadtrees.
* Reimplement the simulation in C++.
* Compare the direct and tree-based approaches in terms of computational performance and numerical behaviour.
* Improve trajectory visualization through animation.

These developments will be implemented progressively as the project evolves.

## Project scope

This is an ongoing personal project at the intersection of computational physics, numerical analysis and scientific programming. The repository documents the implementation and development of the simulation, including the numerical methods and algorithms explored along the way.
