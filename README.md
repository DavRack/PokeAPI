# Poke berries api

the env variable are set in .env file
by default the host is localhost and the port is 4000

The endpoint ["/allBerryStats"](https://pokeapi-edhe.onrender.com/allBerryStats) returns the following structure:
```{json}
    Response: {
        "berries_names": [...],
        "min_growth_time": "" // time, int
        "median_growth_time": "", // time, float
        "max_growth_time": "" // time, int
        "variance_growth_time": "" // time, float
        "mean_growth_time": "", // time, float
        "frequency_growth_time": "", // time, {growth_time:    frequency, ...}
    }
```
The endpoint ["/allBerryFrequency"](https://pokeapi-edhe.onrender.com/allBerryFrequency) will return an html page with a histogram of the frequency_growth_time 

## Execution instructions

## Dependencies

- a unix like system (tested on Arch linux, kernel 6.4.4-arch1-1)
- python 3.11
- virtualenv

### Create a python env
```
 python -m venv env
```
### Initialize python env
```
source env/bin/activate
```
### Install dependencies
```
pip install -r requirements.txt
```
### Install dependencies
```
pip install -r requirements.txt
```
### Run app
```
python main.py
```
