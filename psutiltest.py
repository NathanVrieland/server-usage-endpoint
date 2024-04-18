import psutil

print("### CPU PERCENT ###")
print(psutil.cpu_percent(interval=1), "%")
print("### CPU PERCENT PER LOGICAL PROCESSOR ###")
print(psutil.cpu_percent(interval=1, percpu=True))
print("### MEMORY ###")
print(psutil.virtual_memory().percent, "%")