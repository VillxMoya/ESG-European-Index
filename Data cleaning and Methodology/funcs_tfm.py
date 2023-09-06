import pandas as pd

def coef_flotante(float_pct): # Coeficiente de ajuste a la flotación de las acciones
    if pd.isna(float_pct) or float_pct == '<NA>':
        return 'Unknown'
    elif float_pct < 10:
        return float(10)
    elif 10 < float_pct < 20:
        return float(20)
    elif 20 < float_pct < 30:
        return float(40)
    elif 30 < float_pct < 40:
        return float(60)
    elif 40 < float_pct <50:
        return float(80)
    elif float_pct > 50:
        return float(100)

def adj_sobrepon(weight): # Ajuste de sobreponderación
    if pd.isna(weight) or weight == '<NA>':
        return 'Unknown'
    elif weight < 0.1:
        return float(0)
    elif  0.1 < weight < 0.15:
        return float(0.1)
    elif 0.15 < weight < 0.2:
        return float(0.3)
    elif weight > 0.2:
        return float(0.6)