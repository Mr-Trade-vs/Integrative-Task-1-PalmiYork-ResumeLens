# ResumeLens

**ResumeLens** is a Python application that analyzes resumes and classifies candidates according to professional profiles using formal language techniques.

## Objectives

- Extract information from resumes using regular expressions.
- Normalize equivalent qualifications using finite-state transducers.
- Classify candidates using finite automata.
- Define and validate candidate profiles using a context-free grammar (CFG).
- Visualize candidate analysis results.

## Technologies

- Python
- Regular Expressions (`re`)
- Pyformlang
- textX
- Streamlit
- Pytest

## Supported Profiles

- Full Stack Developer
- Machine Learning Engineer
- Backend Developer
- Data Scientist

## Project Structure

```text
ResumeLens/
├── app.py
├── requirements.txt
├── config/
├── data/
├── docs/
└── src/
    ├──resumelens/
    └──tests/
```

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Mr-Trade-vs/Integrative-Task-1-PalmiYork-ResumeLens.git
cd Integrative-Task-1-PalmiYork-ResumeLens
```

Create a virtual environment and install the dependencies:

```bash
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install -r requirements.txt
```

## Run the Application

```bash
py -m streamlit run app.py
```

## Run Tests

```bash
cd src
py -m pytest -v
```