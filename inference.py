
PRODUCT_MAP = {

    "Bitumen": ["bitumen", "road", "highway"],

    "Furnace Oil": ["boiler", "power plant"],

    "Marine Fuel": ["marine", "vessel"],

    "HSD Diesel": ["diesel", "fleet", "logistics"],

    "Hexane": ["solvent", "chemical"]

}

def predict(signal):

    signal = signal.lower()

    for product, keywords in PRODUCT_MAP.items():

        for keyword in keywords:

            if keyword in signal:

                return product, 0.9

    return "General Fuel", 0.5
