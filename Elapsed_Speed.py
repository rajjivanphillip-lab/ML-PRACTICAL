import matplotlib.pyplot as plt

# Data
elapsed_time = [0, 1, 2, 3, 4, 5, 6]
speed = [0, 3, 7, 12, 20, 30, 45.6]

plt.figure()
plt.plot(elapsed_time, speed, marker='o')

plt.title("Elapsed Time vs Speed")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Speed (m/s)")
plt.grid(True)

plt.show()
plt.figure()
plt.bar(elapsed_time, speed)

plt.title("Elapsed Time vs Speed")
plt.xlabel("Elapsed Time (s)")
plt.ylabel("Speed (m/s)")

plt.show()