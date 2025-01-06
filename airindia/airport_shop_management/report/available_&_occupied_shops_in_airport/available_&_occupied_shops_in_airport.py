import frappe

from frappe import _

def execute(filters: dict | None = None):
    columns = get_columns()
    data = get_data()
    chart = get_chart_data(data)  
    
    return columns, data, None, chart  

def get_columns() -> list[dict]:
    return [
        {
            "label": _("Airport"),
            "fieldname": "airport",
            "fieldtype": "Data",
        },
        {
            "label": _("Total Shops"),
            "fieldname": "total_shops",
            "fieldtype": "Int",
        },
        {
            "label": _("Available Shops"),
            "fieldname": "available_shops",
            "fieldtype": "Int",
        },
        {
            "label": _("Occupied Shops"),
            "fieldname": "occupied_shops",
            "fieldtype": "Int",
        },
    ]

def get_data() -> list[dict]:
    
    data = frappe.db.sql("""
        SELECT 
            airport,
            COUNT(*) AS total_shops,
            SUM(CASE WHEN select_qhzc = 'Available' THEN 1 ELSE 0 END) AS available_shops,
            SUM(CASE WHEN select_qhzc = 'Occupied' THEN 1 ELSE 0 END) AS occupied_shops
        FROM `tabAirport Shop`
        GROUP BY airport
    """, as_dict=True)
    
    return data

def get_chart_data(data: list[dict]) -> dict:
    
    labels = [row['airport'] for row in data]
    available_shops = [row['available_shops'] for row in data]
    occupied_shops = [row['occupied_shops'] for row in data]

    chart = {
        "data": {
            "labels": labels,
            "datasets": [
                {
                    "name": _("Available Shops"),
                    "values": available_shops,
                },
                {
                    "name": _("Occupied Shops"),
                    "values": occupied_shops,
                },
            ]
        },
        "type": "bar",  
        "colors": ["#6aff00", "#ff4f4f"], 
    }
    
    return chart
