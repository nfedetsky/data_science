import matplotlib.pyplot as plt
plt.rcdefaults()

d = {
    'Moscow': 12,
    'Vladivostok': 23,
    'Warsow': 79,
    'Prague': 68,
    'Budapest': 56
}

towns = d.keys()
years = d.values()
plt.bar(towns, years)
plt.show()