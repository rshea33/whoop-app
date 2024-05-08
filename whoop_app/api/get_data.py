import json
import logging
import os
import shutil
from typing import Literal

import polars as pl
import requests

PATH = "whoop_app/csv_data"


class WhoopApp:
    """A class to get data from the Whoop API or a CSV file."""

    def __init__(self, mode: Literal["api", "csv"]):
        self.mode = mode
        self.get_data()

    def get_data(self) -> None:
        if self.mode == "api":
            # Get data from the Whoop API, to be implemented
            raise NotImplementedError

        elif self.mode == "csv":
            self._get_data_from_csv()

        else:
            raise ValueError("Invalid mode. Please choose 'api' or 'csv'.")

    def _get_data_from_csv(self) -> None:
        directories = os.listdir(PATH)
        directories = [d for d in directories if "my_whoop_data_" in d]
        directories.sort(reverse=True)
        self._directory = f"{PATH}/{directories[0]}"

        self._journal_entries = pl.read_csv(f"{self._directory}/journal_entries.csv")
        self._physiological_cycles = pl.read_csv(
            f"{self._directory}/physiological_cycles.csv"
        )
        self._sleeps = pl.read_csv(f"{self._directory}/sleeps.csv")
        self._workouts = pl.read_csv(f"{self._directory}/workouts.csv")


if __name__ == "__main__":
    app = WhoopApp("csv")
    print()
