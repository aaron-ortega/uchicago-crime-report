#!/bin/sh

eval "$(pyenv init -)"
pyenv activate env3.6

# Run spider
cd /Users/aaron/Documents/github/uchicago-crime-report/uchicagoCrime/uchicagoCrime/spiders
scrapy crawl crimeLog -o ../../../data/raw_crimeLogData_$(date +%Y-%m-%d).json

# Clean data
cd ../../../scripts
python clean_data.py
