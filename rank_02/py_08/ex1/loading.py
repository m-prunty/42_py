#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    loading.py                                        :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: maprunty <maprunty@student.42heilbronn.d  +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/04/24 08:06:36 by maprunty         #+#    #+#              #
#    Updated: 2026/04/24 14:11:21 by maprunty        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #
"""This program loads the weather forecast data and visualizes it."""

import importlib
import sys

import matplotlib.pyplot as plt  # type: ignore
import numpy as np
import pandas as pd
import requests

RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
LIGHT_BLUE = "\033[1;34m"
BOLD = "\033[1m"
END = "\033[0m"


def check_dependency(mod: tuple[str, str]) -> bool:
    """Check if a module is available and print its version."""
    try:
        module = importlib.import_module(mod[0])
        version = getattr(module, "__version__", "unknown")
        print(f"{GREEN}[OK]{END} {mod[0]} ({version}) - {mod[1]} ready")
        return True
    except ImportError as e:
        print(f"{RED}[FAIL]{END} Missing dependency: {e.name}. Please install")
        return False


def dependencies() -> None:
    """Check all required dependencies and print their status."""
    print("\nChecking dependencies:")
    dependencies = [
        ("pandas", "Data manipulation"),
        ("numpy", "Numerical computations"),
        ("requests", "Newtork access"),
        ("matplotlib", "Visualization"),
    ]
    all_ok = True
    for mod in dependencies:
        if not check_dependency(mod):
            all_ok = False
    if not all_ok:
        raise Exception


def get_data() -> pd.DataFrame:
    """Fetch weather forecast data and return it as a DataFrame."""
    print(f"\n{PURPLE}LOADING STATUS:{END} Fetching data...")
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        + "latitude=49.1427&longitude=9.2109&past_days=41"
        + "&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m,"
        + "precipitation_probability,rain&forecast_days=10"
    )
    try:
        response = requests.get(url, verify=True)
        df = pd.json_normalize(response.json())
        hourly_cols = [c for c in df.columns if c.startswith("hourly.")]
        arrays = {col: np.asarray(df.iloc[0][col]) for col in hourly_cols}
        out = {col: arrays[col] for col in hourly_cols}
        print("Analyzing Matrix data...")
        return pd.DataFrame(out)

    except requests.RequestException as e:
        print(f"{RED}[ERROR]{END} Failed to fetch data: {e}")
        raise


def plot_weather_forecast(df: pd.DataFrame, file: str) -> None:
    """Plot the weather forecast data with a dark theme and multiple axes."""

    def find_col(keyword: str) -> str | None:
        for col in df.columns:
            if col.startswith("hourly.") and keyword in col:
                return col
        return None

    print("Generating visualization...")
    time_col = find_col("time")
    temp_col = find_col("temperature")
    hum_col = find_col("humidity")
    precip_col = find_col("precipitation_probability")
    rain_col = find_col("rain")
    wind_col = find_col("wind_speed")

    if not time_col or not temp_col:
        raise ValueError("Missing required columns: time and temperature")
    df = df.copy()
    df[time_col] = pd.to_datetime(df[time_col])
    df = df.set_index(time_col)

    fig, ax1 = plt.subplots(figsize=(60, int(60 * 0.43)))
    ax1.set_facecolor("xkcd:black")
    fig.set_facecolor("xkcd:grey")

    ax1.plot(df.index, df[temp_col], label="Temperature (°C)", color="tab:red")
    ax1.set_ylabel("Temperature (°C)")
    ax1.plot(
        df.index,
        df[wind_col],
        linestyle="--",
        label="Wind (km/h)",
        color="tab:orange",
    )
    ax2 = ax1.twinx()
    ax2.plot(
        df.index,
        df[hum_col],
        linestyle="--",
        label="Humidity (%)",
        color="tab:blue",
    )
    ax2.plot(
        df.index,
        df[precip_col],
        linestyle=":",
        label="Precip (%)",
        color="tab:cyan",
    )
    ax2.bar(
        df.index,
        df[rain_col] * 4,
        alpha=0.5,
        label="Rain (mm)",
        color="tab:blue",
    )
    ax2.set_ylabel("Humidity / Precip / Rain")

    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2)

    plt.title("Weather Forecast (Hourly)")
    plt.savefig(file)


def main() -> None:
    """Load and run the visualization process."""
    print(f"\n{PURPLE}LOADING STATUS:{END} Loading programs...\n")
    try:
        dependencies()
    except Exception:
        print(
            f"\n{RED}[ERROR]{END}:"
            + "Please install the missing dependencies and try again."
        )
        sys.exit(1)
    try:
        data = get_data()
    except Exception as e:
        print(f"{RED}[ERROR]{END} Could not load data: {e}")
        sys.exit(1)
    print(f"Processing {len(data)} data points...")
    file = "matrix_analysis.png"
    plot_weather_forecast(data, file)
    print(f"Results saved to: {file}")


if __name__ == "__main__":
    main()
