import numpy as np
from collections import Counter
from sklearn.cluster import KMeans


def get_color_percentages(image, num_colors):
    def rgb_to_hex(r, g, b):
        return f"#{r:02x}{g:02x}{b:02x}"

    img_array = np.array(image)
    pixels = img_array.reshape(-1, 3)
    kmeans = KMeans(n_clusters=num_colors, random_state=0).fit(pixels)
    new_pixels = kmeans.cluster_centers_[kmeans.labels_]
    new_img_array = new_pixels.reshape(img_array.shape).astype(np.uint8)

    hex_codes = np.empty((img_array.shape[0], img_array.shape[1]), dtype=object)
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            r, g, b = new_img_array[i, j]
            hex_codes[i, j] = rgb_to_hex(r, g, b)

    hex_codes_list = hex_codes.flatten()
    color_counts = Counter(hex_codes_list)

    total_pixels = img_array.shape[0] * img_array.shape[1]
    color_percentages = [(color, round(count / total_pixels * 100, 3)) for color, count in
                         color_counts.most_common(num_colors)]

    return color_percentages

