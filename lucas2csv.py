#!/usr/bin/env python
# coding: utf-8

import os
import numpy as np
import pandas as pd
import rpy2.robjects as robjects


def lucas2csv(path_to_rdata_file, output_path="", verbose=0):
    """Convert LUCAS database to csv files.

    Description
    -----------
    Convert the following columns to single csv files:
        - sample.ID: ID of the soil sample
        - date: date and time
        - spc: hyperspectral data
        - clay: clay content in percentage
        - silt: silt content in percentage
        - sand: sand content in percentage
        - GPS_LAT: GPS latitude
        - GPS_LONG: GPS longitude

    Parameters
    ----------
    path_to_rdata_file : str
        Path to LUCAS.soil_ file
    output_path : str
        Path to the output folder
    verbose : int
        Degree of verbose

    """
    if verbose:
        print("Converting Rdata file ...")
    path_to_rdata_file = os.path.join(path_to_rdata_file, '')
    output_path = os.path.join(output_path, '')
    lucas_file_name = "LUCAS.SOIL_corr.Rdata"

    if verbose:
        print("- Loading Rdata file ...")

    robjects.r["load"](path_to_rdata_file+lucas_file_name)

    if verbose:
        print(tuple(robjects.globalenv.keys()))

    if verbose:
        print("- Loading environment ...")
    df_1 = robjects.globalenv["LUCAS.SOIL"]

    if verbose:
        print("- Saving columns to np.array ...")
    col_to_name = {
        0: "sample.ID",
        2: "date",
        3: "spc",
        5: "clay",
        6: "silt",
        7: "sand",
        25: "GPS_LAT",
        27: "GPS_LONG",
    }
    dict_of_nparrays = {}
    for col in col_to_name:
        if verbose:
            print("   ->", col_to_name[col], "...")
        if col == 2:
            dict_of_nparrays[col_to_name[col]] = np.array(df_1[col], dtype=str)
        else:
            # dict_of_nparrays[col_to_name[col]] = robjects.conversion.ri2py(
            #     df_1[col])
            dict_of_nparrays[col_to_name[col]] = np.array(df_1[col])

    if verbose:
        print("- Saving np.arrays to csv ...")
    for col in col_to_name:
        nparray = np.array(dict_of_nparrays[col_to_name[col]])
        if col_to_name[col] == "spc":
            nparray = nparray.T
        df = pd.DataFrame(data=nparray)
        df.to_csv(output_path+col_to_name[col]+".csv")
        if verbose:
            print("   ->", col_to_name[col], ".csv saved with shape ",
                  df.shape)


if __name__ == '__main__':

    # --- Change BELOW vvv
    path_to_lucas_database = "path/to/lucas/"
    output_path = "tmp/"
    verbose = 1
    # --- Change ABOVE ^^^

    lucas2csv(path_to_rdata_file=path_to_lucas_database,
              output_path=output_path,
              verbose=verbose)
