# Map Visualizations

CSV to PDF Speed Map Generator

This project reads GPS data stored in CSV files, applies **natural breaks classification** to the `SPEED` column, and generates a **map with colored points** saved as a PDF file.

Each CSV file inside `assets/inputs/` will automatically be processed, and the output PDFs will be saved into `assets/outputs/`.

The PDF will contain a speed map with points colored by speed:

- Dark Blue → slowest speeds
- Cyan Blue
- Grey/White
- Orange
- Red → fastest speeds
---

## 🚀 Getting Started

### 1. Install Python
Make sure you have **Python 3.13+** installed.
On Windows, you can download it from [python.org](https://www.python.org/downloads/).

### 2. Install dependencies
First, clone or download this project, then install the required dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Note: Note: Installing geopandas on Windows may also require installing shapely, fiona, and other GIS dependencies. If you have issues, check the official [GeoPandas installation guide](https://geopandas.org/en/stable/getting_started/install.html).

### 3. Project Structure

```
assets/
│── inputs/   <- place your CSV files here
│── outputs/  <- generated PDF maps will appear here
main.py       <- the main script
requirements.txt
```
### 4. Run the script

```bash
python main.py
```

#### Notes:
- ✅ The code has been tested on Linux only. It should work on Windows and Mac, but some dependencies (like GeoPandas) may need extra setup.
- ⏳ Big CSV files will take longer to process due to map rendering and classification.

#### TODOs

- Add unit tests to validate outputs.
- Improve performance for large CSV files.
- Add a Compass Rose for Cardinal Points.

#### License
MIT License