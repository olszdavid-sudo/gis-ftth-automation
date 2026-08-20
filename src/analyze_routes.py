from pathlib import Path

import geopandas as gpd
import pandas as pd


# ---------------------------------------------------------
# Project paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "sample_routes.geojson"
OUTPUT_DIR = BASE_DIR / "output"

SUMMARY_FILE = OUTPUT_DIR / "route_summary.csv"
VALIDATED_FILE = OUTPUT_DIR / "validated_routes.geojson"


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

REQUIRED_COLUMNS = [
    "route_id",
    "segment_type",
    "status",
    "cable_type",
]

# EPSG:2180 - Polish national projected coordinate system
# suitable for measurements in metres.
METRIC_CRS = "EPSG:2180"


def load_routes():
    """Load FTTH routes from the sample GeoJSON file."""

    print(f"Loading data from: {INPUT_FILE}")

    routes = gpd.read_file(INPUT_FILE)

    if routes.empty:
        raise ValueError("Input dataset does not contain any FTTH routes.")

    print(f"Loaded {len(routes)} route segments.")

    return routes


def validate_attributes(routes):
    """Check required attributes and missing values."""

    print("\nValidating attributes...")

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in routes.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    routes["missing_attributes"] = routes[
        REQUIRED_COLUMNS
    ].isna().sum(axis=1)

    routes["attributes_valid"] = (
        routes["missing_attributes"] == 0
    )

    return routes


def validate_geometry(routes):
    """Validate FTTH route geometries."""

    print("Validating geometries...")

    routes["geometry_empty"] = routes.geometry.is_empty

    routes["geometry_valid"] = (
        routes.geometry.notna()
        & ~routes.geometry.is_empty
        & routes.geometry.is_valid
    )

    routes["geometry_type_valid"] = (
        routes.geometry.geom_type == "LineString"
    )

    return routes


def calculate_lengths(routes):
    """Calculate FTTH route lengths in metres."""

    print("Calculating route lengths...")

    # Input data is stored as geographic coordinates.
    # Reproject to EPSG:2180 before measuring length.
    routes_metric = routes.to_crs(METRIC_CRS)

    routes["length_m"] = routes_metric.geometry.length.round(2)

    routes["length_valid"] = routes["length_m"] > 0

    return routes


def add_validation_status(routes):
    """Create final validation status for every route."""

    routes["validation_status"] = "OK"

    invalid_mask = (
        ~routes["attributes_valid"]
        | ~routes["geometry_valid"]
        | ~routes["geometry_type_valid"]
        | ~routes["length_valid"]
    )

    routes.loc[
        invalid_mask,
        "validation_status"
    ] = "CHECK"

    return routes


def generate_summary(routes):
    """Generate overall FTTH route statistics."""

    summary = {
        "segments_analysed": len(routes),
        "total_route_length_m": round(
            routes["length_m"].sum(), 2
        ),
        "average_segment_length_m": round(
            routes["length_m"].mean(), 2
        ),
        "invalid_geometries": int(
            (~routes["geometry_valid"]).sum()
        ),
        "missing_attribute_records": int(
            (~routes["attributes_valid"]).sum()
        ),
        "segments_requiring_check": int(
            (routes["validation_status"] == "CHECK").sum()
        ),
    }

    return summary


def print_summary(summary):
    """Print analysis results in a readable format."""

    print("\nFTTH Route Analysis")
    print("-" * 35)

    print(
        f"Segments analysed: "
        f"{summary['segments_analysed']}"
    )

    print(
        f"Total route length: "
        f"{summary['total_route_length_m']} m"
    )

    print(
        f"Average segment length: "
        f"{summary['average_segment_length_m']} m"
    )

    print(
        f"Invalid geometries: "
        f"{summary['invalid_geometries']}"
    )

    print(
        f"Records with missing attributes: "
        f"{summary['missing_attribute_records']}"
    )

    print(
        f"Segments requiring check: "
        f"{summary['segments_requiring_check']}"
    )


def export_results(routes, summary):
    """Export validated routes and summary."""

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\nExporting results...")

    # Export route validation results
    routes.to_file(
        VALIDATED_FILE,
        driver="GeoJSON"
    )

    # Export overall statistics
    summary_df = pd.DataFrame(
        [summary]
    )

    summary_df.to_csv(
        SUMMARY_FILE,
        index=False
    )

    print(f"Validated routes: {VALIDATED_FILE}")
    print(f"Summary: {SUMMARY_FILE}")


def main():
    """Run the complete FTTH GIS analysis."""

    print("=" * 50)
    print("GIS / FTTH AUTOMATION")
    print("=" * 50)

    routes = load_routes()

    routes = validate_attributes(routes)
    routes = validate_geometry(routes)
    routes = calculate_lengths(routes)
    routes = add_validation_status(routes)

    summary = generate_summary(routes)

    print_summary(summary)

    export_results(
        routes,
        summary
    )

    print("\nAnalysis completed successfully.")


if __name__ == "__main__":
    main()
