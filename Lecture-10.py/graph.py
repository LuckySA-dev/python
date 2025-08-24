# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]

# plt.plot(x, y, marker='o', linestyle='-', color='b')

# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Line Plot')

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import matplotlib.animation as animation

# fig, ax = plt.subplots()

# x = np.linspace(0, 2 * np.pi, 100)
# y = np.sin(x)

# line, = ax.plot(x, y)

# def update(frame):
#     line.set_ydata(np.sin(x + frame / 10.0))
#     return line,

# ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# plt.show()

