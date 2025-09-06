# Standard library imports (none in your list)
import os

# Third-party imports
#import folium
import geopandas
import mapclassify
import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import colormaps
import numpy as np
import pandas as pd
import contextily as cx
#from google.colab import drive


CSV_FILES_PATH = 'assets/inputs/'
OUTPUT_DIRECTORY = 'assets/outputs/'

# Ensure output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

filename = "my_filename"

def create_pdf_file(filename):
    df = pd.read_csv(CSV_FILES_PATH + filename)

    #print("Combining and converting date/time columns...")
    df['datetime'] = pd.to_datetime(df['UTC DATE'] + ' ' + df['UTC TIME'])

    # Creating GeoPandas Dataframe

    geometry = geopandas.points_from_xy(df.LONGITUDE, df.LATITUDE)

    print(f"Processing the GeoDataFrame for {filename}")
    gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    gdf = gdf.to_crs(gdf.estimate_utm_crs())

    # Plotting the map

    custom_cmap = mcolors.ListedColormap([
        "#00008B",  # Dark Blue
        "#00BFFF",  # Cyan Blue
        "#D3D3D3",  # Light Grey (could use "white" too)
        "#FFA500",  # Orange
        "#FF0000"   # Red
    ])



    print(f"Plotting {filename}")

    # Create PDF file
    pdf_name = os.path.splitext(filename)[0] + ".pdf"
    output_pdf = os.path.join(OUTPUT_DIRECTORY, pdf_name)

    with PdfPages(output_pdf) as pdf:
        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(17,17))
        gdf.plot(
            ax=ax,
            column='SPEED',
            scheme="natural_breaks",
            k=5,
            markersize=5,
            marker="o",
            legend=True,
            cmap=custom_cmap,
            legend_kwds={
                "title": "Mean Speed (m/s)",  # legend title
                "fontsize": 10
            }
        )
        cx.add_basemap(ax, source=cx.providers.Esri.WorldImagery, crs=gdf.crs)
        ax.set_title(f"{filename}" )

        # Save current figure into the PDF
        pdf.savefig(fig, bbox_inches="tight")
        plt.close(fig)

    print(f"Map saved inside {output_pdf}", end="\n\n" )

if __name__ == '__main__':
    # Loop through every CSV file inside the CSV_FILES_PATH
    for file in os.listdir(CSV_FILES_PATH):
        if file.lower().endswith(".csv"):
            create_pdf_file(file)