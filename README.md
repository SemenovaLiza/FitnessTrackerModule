# Fitness Tracker Module
![Pytest](https://img.shields.io/badge/tests-passing-brightgreen?style=flat-square&logo=pytest) ![Python](https://img.shields.io/badge/python-3.11-blue?style=flat-square&logo=python) ![License](https://img.shields.io/badge/license-MIT-purple.svg?style=flat-square) ![Status](https://img.shields.io/badge/status-needs%20refactoring-orange?style=flat-square)

A software module for a fitness tracker that processes and displays results for three types of workouts: running, sport walking, and swimming. My first project :)
 статус разработки (в разработке, на поддержке и т.д.), статус билда, процент покрытия тестами и тд.

## Technologies
- [python 3.11.5](https://www.python.org/downloads/release/python-3115/)
- [pytest 6.2.5](https://docs.pytest.org/en/stable/announce/release-6.2.5.html)
- [flake8 4.0.1](https://flake8.pycqa.org/en/4.0.1/)

## Deployement

### System requirements
- Python3.7 and further versions
### How to run project

- Clone the project to your computer 
    ```
    git clone git@github.com:SemenovaLiza/yacut.git
    ```
- Create a virtual environment
    ```
    python3 -m venv venv
    ```

- Activate a virtual environment
    - For Linux/macOS

        ```
        source venv/bin/activate
        ```

    - For Windows OS

        ```
        source venv/scripts/activate
        ```
* Install dependencies from requirements.txt 
    ```
    pip install --upgrade
    pip install -r requirements.txt
    ```
* Run tests
    ```
    pytest
    ```
* Run app
    ```
    python homework.py
    ```

### Output
    ```
    Training type: Swimming; Duration: 1.000 h.; Distance: 0.   994 km; Speed: 1.000 km/h; Calories: 336.000.
    Training type: Running; Duration: 1.000 h.; Distance: 9.750 km; Speed: 9.750 km/h; Calories: 699.750.
    Training type: SportsWalking; Duration: 1.000 h.; Distance: 5.850 km; Speed: 5.850 km/h; Calories: 157.500.
    ```

### Testing
This project contains few unit test with pytest. To run these test run the `pytest` command.

## Author
### Elizaveta Semenova
