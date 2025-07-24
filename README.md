# Data Pipeline

A data processing pipeline for medical datasets.

## Project Structure

```
data-pipeline/
├── app/
│   └── pipeline.py       # Main pipeline code
├── data/
│   └── Medicaldataset.csv # Input data (not tracked in git)
├── docker-compose.yml    # Docker Compose configuration
├── Dockerfile            # Docker configuration
└── requirements.txt      # Python dependencies
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```
   python app/pipeline.py
   ```

## Docker Usage

Build and run using Docker Compose:

```
docker-compose up
```

## License
