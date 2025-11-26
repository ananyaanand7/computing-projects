Filename: `analyze_steps.py`

Functions:

- `total_steps` takes a list of step data and returns the sum

- `active_hours` takes step data and a threshold number steps. It returns the number of hours in which more than [threshold] steps were taken.

- `best_hour` takes step data and return the hour of the day with the most steps. Assumes data index corresponds to time in 24-hour time.

## Provided

Main function and sample data for 3 days. Provided `analyze_one_day` calls functions for each day of data.

# Step Analysis Project

## Description
This Python miniproject analyzes daily step count data to provide insights into physical activity patterns. The program computes total steps per day, identifies active hours, and finds the hour with the highest activity. It demonstrates modular code design, functions, loops, and basic data analysis.

## Features
- **Total Steps:** Calculates the sum of steps for a given day.  
- **Active Hours:** Counts the number of hours exceeding a step threshold (default 500).  
- **Best Hour:** Identifies the hour with the maximum number of steps.  
- **Daily Analysis:** Iterates through multiple days of data to provide a summary for each day.  

## Sample Output
Example output for a single day:
Analyze day 1:
Total: 22500
Active hours: 8
Best hour: 15

- **Total:** Sum of all steps during the day  
- **Active hours:** Hours exceeding the activity threshold  
- **Best hour:** Hour with the most steps  

## Technologies Used
- Python 3.x  
- Core Python libraries (no external dependencies)

## Usage
1. Clone the repository:
```bash
git clone git@github.com:ananyaanand7/lists_analyzesteps.git

2. Run the program:

python analyze_steps.py

3. Observe daily activity summaries in the console.

Code Structure
lists_analyzesteps/
│── step_analysis.py        # Main Python script
│── README.md               # Project description

Learning Outcomes
- Writing modular Python functions with clear docstrings
- Applying loops, conditionals, and indexing to process time-series data
- Summarizing and analyzing structured datasets
- Presenting data in a concise and interpretable format
