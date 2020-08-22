# internet-speed

This is a program that uses speedtest-cli python api to calculate internet speed, logs the result in a file and presents visual representation

## Requirements
- git
- python 3.0 or higher
- python package installer **pip** 
    - *please refer to https://pypi.org/project/pip/ for more information*
- required packages in `requierments.txt` (please refer to How-To)

## How-To

- Start by cloning the repository using the following command `git clone https://github.com/Husseinelghoul/internet-speed`
- Navigate to the code's directory  `cd internet-speed`
- Install the requierments using the following command `pip install -r requierments.txt`
- Run the program using the following command `py app.py`
- You will be prompted to enter the **number of rounds** *(Number of tests to perform before exiting the program)*

## Interpreting Results

The resuls will appear on the **command prompt** and in **log.txt** file <br />
When the program is done the visual representation will appear on the screen and two files will be generated **plot.png** and **plot.pdf** to save the plot <br />
The **log.txt** file contains the following for each round:
- internet speed in and Time
- Date and Time the "get internet speed" request was made 
- Thee time it's taking to get your internet speed
-The round number

### Sample Output
###### Internet speed/ Round Graph
![Sample Graph](https://github.com/Husseinelghoul/internet-speed/blob/master/plot-sample.png)
