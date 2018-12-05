# LUCAS 2 CSV

Export several columns from the Rdata-File of the LUCAS Topsoil Database 2009 to CSV files.

## Description

The LUCAS 2009 TOPSOIL database is a rich dataset consisting of hyperspectral reflectance data and various soil properties data like clay, silt and sand content. This Python script extracts the several columns from the RData-file. I uploaded this script since there are no working examples for this file available yet.

The following columns are extracted:

- `sample.ID`: ID of the soil sample
- `date`: date and time
- `spc`: hyperspectral data
- `clay`: clay content in percentage
- `silt`: silt content in percentage
- `sand`: sand content in percentage
- `GPS_LAT`: GPS latitude
- `GPS_LONG`: GPS longitude

Link to the LUCAS Topsoil database: [https://esdac.jrc.ec.europa.eu/content/lucas-2009-topsoil-data](https://esdac.jrc.ec.europa.eu/content/lucas-2009-topsoil-data)

## Requirements

For this script, the following Python 3.x packages are needed:

* rpy2
* numpy
* pandas

## Usage

```python
import lucas2csv as l2csv

lucas2csv(
    path_to_rdata_file="path/to/rdata",
    output_path="output/path/",
    verbose=1)
```
