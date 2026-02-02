"""Splits the data into two CSV files, one for names and one for places.
"""

import csv
from collections import Counter


def write_counter(counter: Counter, file: str, counted_entity: str) -> None:
    """
    Writes the contents of a Counter object to a CSV file.

    Args:
        counter (Counter): The Counter object containing the items and their counts.
        file (str): The path to the CSV file where the data will be written.
        counted_entity (str): The name of the entity being counted, used as a column header in the CSV.

    The CSV will have two columns: the counted_entity and its corresponding count.
    """

    with open(file, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([counted_entity, "count"])
        writer.writerows(counter.most_common())


if __name__ == "__main__":
    with open("data/names_and_places.csv") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        name_counter = Counter([row["Name"] for row in data])
        place_counter = Counter([row["Ort"] for row in data])

    write_counter(name_counter, "data/names.csv", "Name")
    write_counter(place_counter, "data/places.csv", "Ort")
