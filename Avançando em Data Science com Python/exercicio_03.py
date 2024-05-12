import pandas as pd
import matplotlib.pyplot as plt 

data = {
    "Cidades": ["Nova York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
    "População": [8622698, 3990456, 2716000, 2320268, 1680992],
    "Área (km²)": [783.8, 1302, 606.1, 1650.4, 1340.6],
    "Densidade Populacional (por km²)": [11016, 3057, 4483, 1405, 1254],
    "IDH": [0.95, 0.92, 0.88, 0.84, 0.81]
}

df=pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(14,8))

ax.bar(data["Cidades"], data["População"], color='green')
ax.set_xlabel('Cidades')
ax.set_ylabel('População')
ax.set_title('População das Cidades')
plt.show()