# Image Processor

This project converts all images from a specified input folder.

During the conversion process, each image is:

- Resized to the desired dimensions.
- Converted to grayscale.
- make it blur.
- Converted to PNG format.

The processed images are then saved to a new output folder specified by the user.

How It Works
The user provides the path to the input folder containing the images.
The user specifies the name or path of the output folder.
The application processes every image in the input folder.
The converted images are saved in the output folder.

## How to use it
```python
python3 image_processor.py Pokedex/ Processed/
```

- Pokedex will be the input_folder where the images are
- Processed will be the output folder where the processed images will be stored

## Used libraries
- pathlib - built-in
- pillow - installed