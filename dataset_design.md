# Dataset Design

## Disease
COVID-19

## Genome Dataset
Source: NCBI Virus

Features:
- Sequence Length
- GC Content
- Mutation Count
- Collection Date
- Country
- Variant

## Environmental Dataset
Source: NASA POWER

Features:
- Temperature
- Relative Humidity
- Solar Radiation
- Rainfall

## Epidemiological Dataset
Source: Our World in Data

Features:
- Daily Cases
- New Cases
- Total Cases

## Merge Strategy

Datasets will be merged using:

- Collection Date
- Country

## Expected Output

Integrated dataset for disease risk prediction.