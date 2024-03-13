import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def draw_bezier_recursive(points, iterations):
    if len(points) == 2 or iterations == 0:
        xs, ys = zip(*points) # unpack points jadi x and y coordinates
        plt.plot(xs, ys, 'b-')
    else:
        new_points = []
        for i in range(len(points)-1):
            new_points.append(midpoint(points[i], points[i+1]))
        new_points = [points[0]] + new_points + [points[-1]]
        draw_bezier_recursive(new_points, iterations - 1)

# contoh titik
points = [(2, 2), (3, 3), (6, 2)]

# buat kurva animasi
def animate(iteration):
    ax.clear()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title(f'Bezier Curve Iteration {iteration}')
    ax.grid()
    ax.axis('equal')

    # Tampilkan titik
    for i, point in enumerate(points):
        plt.plot(*point, 'ro')
        plt.text(point[0], point[1], f'P{i}')

    # Gambar kurva
    draw_bezier_recursive(points, iteration)

# inisialisasi plot
fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Bezier Curve')
ax.grid()
ax.axis('equal')

# buat animasi
iterations = int(input("Masukkan jumlah iterasi: "))
ani = FuncAnimation(fig, animate, frames=iterations+1, interval=350, repeat=True)

# tampilkan animasi
plt.draw()
plt.show()