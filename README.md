
# AI in Software Engineering — Week 4


**Project:** Bug Severity Prediction from GitHub Issues


**Author:** [Your Name]


## Overview
This project demonstrates an AI pipeline that:
- Loads GitHub Issues data
- Preprocesses text
- Trains a classifier to predict bug severity (low / medium / high)
- Provides a script to infer severities for new issues
- Includes an optional Selenium scraper to fetch issue titles from a repository


## Repo structure
See the file tree.


## How to run
1. Clone this repo.
2. Create a virtual environment and install dependencies:


```bash
python -m venv venv
source venv/bin/activate # on Windows: venv\Scripts\activate
pip install -r requirements.txt
