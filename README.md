# GIS / FTTH Automation

Python project for automating selected GIS data-processing tasks related to FTTH infrastructure.

The project demonstrates how Python can be used together with GIS tools to analyse spatial data, validate network geometries and generate technical summaries.

## 🎯 Project goals

The project is being developed to demonstrate automation of common GIS / FTTH workflows, including:

- processing spatial data,
- analysing fiber-optic routes,
- calculating route lengths,
- validating geometries,
- generating summaries,
- exporting processed data.

## 🛠️ Technologies

- Python
- GeoPandas
- Shapely
- pandas
- QGIS
- GeoJSON

## 📌 Planned functionality

- FTTH route length calculation
- geometry validation
- attribute validation
- summary generation
- CSV / Excel export
- GeoJSON export

## 📂 Planned project structure

```text
gis-ftth-automation/
├── data/
│   └── sample_routes.geojson
├── src/
│   └── analyze_routes.py
├── output/
├── requirements.txt
└── README.md# GIS / FTTH Automation

Python project focused on automating selected **GIS data-processing tasks related to FTTH infrastructure**.

The project demonstrates how Python can be combined with GIS tools to analyse spatial data, validate network geometries, calculate route parameters and generate technical summaries.

## 🎯 Project goals

The main goal of this project is to demonstrate automation of common GIS / FTTH workflows, including:

* processing spatial data,
* analysing fiber-optic routes,
* calculating route lengths,
* validating geometries,
* validating attribute data,
* generating technical summaries,
* exporting processed results.

The project combines practical experience in **GIS and FTTH infrastructure** with Python-based workflow automation.

## 🛠️ Technologies

Planned technologies used in the project:

* **Python**
* **GeoPandas**
* **Shapely**
* **pandas**
* **QGIS**
* **GeoJSON**
* **CSV / Excel**

## 📌 Planned functionality

The project is planned to include:

* FTTH route length calculation,
* geometry validation,
* attribute validation,
* detection of missing or incorrect data,
* route statistics and summaries,
* CSV export,
* Excel export,
* GeoJSON export.

## 🗺️ Example workflow

The planned workflow will follow the steps below:

1. Load spatial data containing sample FTTH routes.
2. Validate input geometries.
3. Check selected route attributes.
4. Calculate route lengths.
5. Generate route statistics.
6. Export processed results to CSV / Excel.
7. Export validated geometries to GeoJSON.

## 📂 Planned project structure

```text
gis-ftth-automation/
├── data/
│   └── sample_routes.geojson
│
├── src/
│   └── analyze_routes.py
│
├── output/
│   ├── route_summary.csv
│   └── validated_routes.geojson
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Example data

The repository will use **sample and synthetic spatial data only**.

No production, customer or confidential infrastructure data will be included.

The example dataset will represent simplified FTTH route segments with attributes such as:

* route ID,
* segment type,
* route status,
* cable type,
* geometry,
* calculated length.

## 🔎 Planned validation

The project will include basic validation of spatial and attribute data.

Examples:

* invalid or empty geometry,
* missing route identifiers,
* missing required attributes,
* duplicated identifiers,
* incorrect geometry types,
* zero-length route segments.

## 📈 Planned output

The analysis will generate a summary containing information such as:

* number of analysed FTTH segments,
* total route length,
* average segment length,
* number of invalid geometries,
* number of missing attributes,
* validation status.

Example output:

```text
FTTH Route Analysis
-------------------

Segments analysed: 25
Total route length: 4,820 m
Average segment length: 192.8 m
Invalid geometries: 0
Missing attributes: 2
```

## 🚧 Project status

**Work in progress**

Current development roadmap:

* [ ] Create synthetic FTTH spatial dataset
* [ ] Add GeoJSON input data
* [ ] Implement route length calculation
* [ ] Implement geometry validation
* [ ] Implement attribute validation
* [ ] Generate route statistics
* [ ] Add CSV export
* [ ] Add Excel export
* [ ] Add GeoJSON export
* [ ] Add example results
* [ ] Add screenshots from QGIS

## 💡 Project motivation

In GIS and infrastructure projects, many repetitive tasks involve checking spatial data, calculating route parameters and preparing technical summaries.

This project explores how Python can support these workflows by automating repetitive operations and improving data consistency.

It also demonstrates the combination of:

**GIS • FTTH • Spatial Data • Python Automation**

## 🎓 Skills demonstrated

This project is intended to demonstrate practical knowledge of:

* GIS data processing,
* spatial data analysis,
* vector data handling,
* geometry validation,
* FTTH infrastructure,
* Python automation,
* data quality control,
* technical data reporting.

## 🔐 Data privacy

All data used in this repository will be **synthetic or publicly available demonstration data**.

The repository does not contain production data, customer information, confidential network documentation or internal company files.

## 👤 Author

**Dawid Olszewski**

CAD/GIS • FTTH • Spatial Data • Python Automation
