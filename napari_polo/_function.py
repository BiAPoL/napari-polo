from napari_plugin_engine import napari_hook_implementation
from napari_tools_menu import register_function
from napari_time_slicer import time_slicer


@napari_hook_implementation
def napari_experimental_provide_function():
    return [generate_clean_orientation_image]


@register_function(menu="Segmentation / labeling > Generate clean labeled orientation image")
@time_slicer
def generate_clean_orientation_image(raw_orientation_image: 'napari.types.ImageData', step_size: int = 10,
                                     erosion_footprint_width: int = 3) -> 'napari.types.LabelsData':
    from .utilities import prepro_orientation
    from ._core_functions import percentile_pairs, filter_arr_vals, label_expansion

    normalized_image = prepro_orientation([raw_orientation_image])[0]

    idx_steps, arr_steps, bin_limits = percentile_pairs(normalized_image, step_size)

    filtered_images = filter_arr_vals(normalized_image, bin_limits)

    labeled_images, counts = label_expansion(filtered_images, noise_se_size=erosion_footprint_width)

    return labeled_images.astype(int)
