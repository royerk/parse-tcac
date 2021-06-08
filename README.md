# Parse tcac

## Install

* Install `poetry`
* Run `poetry install`

## Collect data

* Edit `collector.py` with new URL and last 2 digits of year to download
* Eventually add more fields to extract from applications, also in `collector.py`
* Run `poetry run parse_tcac/collector.py` (it's kind of slow, but given the limited use case, didn't bother with multithreading but it would make a fun addition: downloading or I/O are all independent)
