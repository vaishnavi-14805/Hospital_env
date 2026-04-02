# Hospital Resource Allocation Environment

## Problem
This project simulates a hospital where patients must be assigned to beds (ICU or normal) based on severity.

## Goal
Maximize reward by assigning:
- High severity → ICU
- Low severity → Normal

## Environment
- 3 difficulty levels: easy, medium, hard
- Patients generated randomly
- Limited beds available

## Files
- environment.py → main environment
- test_env.py → testing file
- inference.py → final solution

## How to Run

Run test:
python test_env.py

Run final:
python inference.py

## Output
The program prints scores for:
- EASY
- MEDIUM
- HARD

## Author
Your Team - Hackathon Project