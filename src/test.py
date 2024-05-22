import pandas as pd

data = {
    "Nombre": ["Juan", "María", "Pedro", "Laura", "Ana"],
    "Edad": [25, 30, 35, 40, 45],
    "Género": ["M", "F", "M", "F", "F"],
    "Puntuación": [80, 90, 85, 95, 88]
}

df = pd.DataFrame(data)

def mult_age_and_score(item):
    print("item", item)
    age = item["Edad"]
    score = item["Score"]
    return age * score

df["Producto"] = df.apply(lambda item: item["Edad"] * item["Puntuación"], axis=1)

print(df)
