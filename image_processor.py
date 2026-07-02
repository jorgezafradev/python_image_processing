from PIL import Image, ImageFilter
from pathlib import Path
import sys

PNG_EXTENSION = 'png'

input_folder_name, output_folder_name = sys.argv[1], sys.argv[2]

input_folder = Path(input_folder_name)
output_folder = Path(output_folder_name)
output_folder.mkdir(parents=True, exist_ok=True)

for file in input_folder.iterdir():
    if file.is_file():
        # bringing image
        img = Image.open(f'{input_folder_name}{file.name}')

        # processing image
        gray = img.convert('L')
        resized = gray.resize((300, 300))
        blur = resized.filter(ImageFilter.BLUR)
        final_name = f'{file.stem}.{PNG_EXTENSION}'

        # saving result image
        location = f'{output_folder_name}{final_name}'
        blur.save(location, PNG_EXTENSION)
        blur.close()
