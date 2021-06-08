# Parse tcac

## Install

* Install `poetry`
* Run `poetry install`

## Collect data

* Edit `collector.py` with new URL and last 2 digits of year to download
* Eventually add more fields to extract from applications, also in `collector.py`
* Run `poetry run parse_tcac/collector.py`, sometimes `os` crashes over permission issues if so then run `poetry shell` then `python parse_tcac/collector.py`
