## SmartEdge_Data Engineering Task
This repository contains SmartEdge data engineering task. The aim of this task is to access the candidate on their knowledge of maintaining code data quality and data integrity.

## Tools Used
```py
- python==3.12
- pandas==2.3.0
- pytest==8.4.1
```

## Directory Structure

| Path             | Description                          |
|------------------|--------------------------------------|
| `data/`          | Contains input data files            |
| `src/`           | Source code (core logic)             |
| `test/`          | Unit tests for the project           |
| `utils/`         | Helper/utility functions             |
| `.gitignore`     | Specifies files Git should ignore    |
| `README.md`      | Project overview and documentation   |
| `main.py`        | Entry point for running the script   |
| `requirements.txt` | Python dependencies list           |

<br>

# Code Usage

## Clone the repository
`
  git clone https://github.com/ioaviator/smartedge_de_task.git
`

## Navigate to project directory
`cd smartedge_de_task`

## Activate virtual environment
`python -m venv venv`

Linux: `source venv/bin/activate` \
Windows: `venv\Scripts\activate`

## Install dependencies
`pip install -r requirements.txt`

## Run the code
`python main.py --file ./data/311_service_request.csv`


## Using the logging module

Logs(Code Errors, Code Information) are passed into the `data_quality_logs.log` file.

```python
import logging

# configure logging 
logging.basicConfig(
    filename='data_quality_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
```

## Testing
Naviagte to test folder: \
`cd test`

Run Test: \
`pytest`
