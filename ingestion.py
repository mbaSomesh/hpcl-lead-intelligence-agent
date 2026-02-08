import pandas as pd
import sqlite3
import random
from database import init
from scoring import calculate_score

DB = "data/leads.db"

init()

df = pd.read_csv("dataset/signals.csv")

conn = sqlite3.connect(DB)

cursor = conn.cursor()


def infer_product(signal):

    signal = signal.lower()

    if "bitumen" in signal or "highway" in signal:
        return "Bitumen"

    elif "diesel" in signal or "fleet" in signal:
        return "HSD Diesel"

    elif "boiler" in signal or "power plant" in signal:
        return "Furnace Oil"

    elif "chemical" in signal or "solvent" in signal:
        return "Hexane"

    elif "marine" in signal or "vessel" in signal:
        return "Marine Fuel"

    else:
        return "Industrial Fuel"


for _, row in df.iterrows():

    company = row["company"]

    industry = row["industry"]

    signal_text = row["signal"]

    product = infer_product(signal_text)

    confidence = round(random.uniform(0.65, 0.95), 2)

    score, urgency = calculate_score(confidence)

    source = random.choice([
        "GeM Tender Portal",
        "Govt eProcurement Portal",
        "Economic Times News",
        "Company Press Release"
    ])

    cursor.execute("""
    INSERT INTO leads
    (company, industry, product, score, urgency, source, signal, confidence)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        company,
        industry,
        product,
        score,
        urgency,
        source,
        signal_text,
        confidence
    ))


conn.commit()

conn.close()

print("SUCCESS: Realistic leads created")
