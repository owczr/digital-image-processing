import matplotlib.pyplot as plt


def plot_input_and_closed(image, image_closed):
    fig, axs = plt.subplots(2, 1, figsize=(5, 10))
    axs[0].imshow(image, cmap="gray")
    axs[0].set_title("Input image before closing")
    axs[1].imshow(image_closed, cmap="gray")
    axs[1].set_title("Input image after closing")
    plt.show()
