#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        new_list = []
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                new_list.append(row)
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(new_list, json_file)

        return True
    except FileNotFoundError:
        return False
