import matplotlib.pyplot as plt


def plot_before_and_after(image_array, filtration):
    fig, axs = plt.subplots(2, 1, figsize=(7, 14))

    axs[0].imshow(image_array, cmap="gray")
    axs[0].set_title("Before filtration")
    axs[1].imshow(filtration, cmap="gray")
    axs[1].set_title("After filtration")
    plt.show()
