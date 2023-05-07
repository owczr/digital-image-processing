import matplotlib.pyplot as plt


def image_and_heatmap(image, geodetic_map, point):
    _, axs = plt.subplots(2, 1, figsize=(5, 10))
    axs[0].imshow(image, cmap="gray")
    axs[0].set_title("Input image")
    axs[1].imshow(geodetic_map, cmap='inferno')
    axs[1].scatter(point[1], point[0], marker="x", s=100)
    axs[1].set_title("Geodetic map of distances")
    plt.show()
