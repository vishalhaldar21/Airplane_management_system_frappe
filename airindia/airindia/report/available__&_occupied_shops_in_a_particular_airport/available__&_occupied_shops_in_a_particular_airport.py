# Copyright (c) 2024, vishal haldar and contributors
# For license information, please see license.txt

# Import frappe library
# Available & Occupied Shops in a Particular Airport

import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)

    chart = {
        "type": "bar",  # or 'pie', 'line', etc.
        "data": {
            "labels": [row["airport"] for row in data],
            "datasets": [
                {
                    "name": _("Available Shops"),
                    "values": [row["available_shops"] for row in data],
                    "color": "#36a2eb"  # Blue color for Available shops
                },
                {
                    "name": _("Occupied Shops"),
                    "values": [row["occupied_shops"] for row in data],
                    "color": "#ff6384"  # Red color for Occupied shops
                }
            ]
        },
        "colors": ["#36a2eb", "#ff6384"],
        "title": _("Available & Occupied Shops in Airports"),
        "showLegend": 1
    }

    return columns, data, None, chart

def get_columns():
    return [
        {"fieldname": "airport", "label": _("Airport"), "fieldtype": "Data", "width": 200},
        {"fieldname": "total_shops", "label": _("Total Shops"), "fieldtype": "Int", "width": 120},
        {"fieldname": "available_shops", "label": _("Available Shops"), "fieldtype": "Int", "width": 120},
        {"fieldname": "occupied_shops", "label": _("Occupied Shops"), "fieldtype": "Int", "width": 120}
    ]

def get_data(filters):
    # Fetch the data based on the selected filters
    data = frappe.db.sql("""
        SELECT
            airport.name AS airport,
            COUNT(shop.name) AS total_shops,
            SUM(CASE WHEN shop.status = 'Available' THEN 1 ELSE 0 END) AS available_shops,
            SUM(CASE WHEN shop.status = 'Occupied' THEN 1 ELSE 0 END) AS occupied_shops
        FROM
            `tabShop` AS shop
        JOIN
            `tabAirport` AS airport ON shop.airport = airport.name
        GROUP BY
            airport.name
    """, as_dict=True)
    return data
