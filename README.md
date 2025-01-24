
# Cricket Stats Analysis

This project provides an analysis of cricket player statistics, including their ball-by-ball performance, cumulative runs, and graphical visualizations of their career.

## Features

- **Ball-by-Ball Data**: Extracts ball-by-ball data for selected players using Cricinfo's wagon wheel JSON dumps.
- **Cumulative Runs**: Calculates cumulative runs for each player across multiple matches.
- **Data Visualization**: Uses Plotly to generate graphical representations of player performance over time.

## Files

- `balling.py`: Extracts ball-by-ball data from Cricinfo and processes it into a DataFrame.
- `graph.py`: Reads the processed data and generates cumulative runs graphs for players.
- `webscrap.py`: Scrapes Cricinfo for match data for individual players.
- `playerdata/`: Directory containing CSV files with player statistics.
- `requirement.txt`: Lists the required Python libraries for the project.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-repo/Cricket-Stats-Analysis.git
cd Cricket-Stats-Analysis
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:

```bash
pip install -r requirement.txt
```

4. Run the scripts:

- `balling.py`: Scrapes and processes ball-by-ball data.
- `graph.py`: Generates visual graphs based on the processed data.

## Dependencies

- `pandas`: For data manipulation.
- `requests`: To make HTTP requests to Cricinfo.
- `beautifulsoup4`: For web scraping.
- `plotly`: For generating graphs (optional, for visualization).
