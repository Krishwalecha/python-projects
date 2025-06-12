import colorgram as cg

colors_list = []

def extract_colors(file, num_colors):
    """
    Extract colors from an image and save them as RGB tuples in colors_list.

    Args:
        file (str): Image file path.
        num_colors (int): Number of colors to extract.
    """
    global colors_list
    colors_list.clear() # Clear previous colors if any
    colors = cg.extract(file, num_colors)
    for color in colors:
        red = color.rgb.r
        green = color.rgb.g
        blue = color.rgb.b
        color_tuple = (red, green, blue)
        colors_list.append(color_tuple)

