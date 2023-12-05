# simple-synchronization-simulator

## Overview

This repository contains experiments comparing synchronized operations with concurrent operations in threading. The goal is to explore the impact of synchronization mechanisms on shared data consistency in a multi-threaded environment.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Experimental Setup](#experimental-setup)
- [Results](#results)
- [Usage](#usage)

## Introduction

Concurrency in programming introduces challenges related to shared resource access. This repository hosts a simulation project that explores the impact of synchronization on concurrent processes modifying a shared variable. The experiments aim to provide insights into the reliability and predictability of results in both synchronized and unsynchronized scenarios.

## Prerequisites

Before running the simulations, ensure that you have the following prerequisites installed:

- Python 3.x
- Multicore Environment 

## Experimental Setup

### Shared Variables and Processes

- Shared Variable: `X = 1000`
- Processes/Threads: Random number of adders and subtractors
- Local Variables: Random number of iterations between 100-1000 for each process

### Results

#### Without Synchronization

The simulation without synchronization results in a final value of `X` influenced by race conditions and uncontrolled access to the critical section.
Without Synchronization - Final value of X: ...

## Usage

To run the simulations and explore the results:

1. Clone the repository: `git clone https://github.com/Halasalhab/simple-synchronization-simulator`
2. Navigate to the project directory: `cd simple-synchronization-simulator`
3. Execute the simulation script: `python simulation.py`

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -m "Add new feature"`
4. Push to the branch: `git push origin feature/new-feature`
5. Open a pull request.

