from PIL import Image
import os

# Define input and output folders
input_folder = '../Python Scraping/jpeg images'  # Path to the folder containing JPEG images
output_folder = '../Python Scraping/png images'  # Path where PNG images will be saved

# Create the output folder if it doesn't already exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    # Check if the file is a JPEG (or JPG)
    if filename.lower().endswith(('.jpg', '.jpeg')):
        # Construct full file path
        img_path = os.path.join(input_folder, filename)

        # Open the JPEG image
        with Image.open(img_path) as img:
            # Convert filename to PNG format by changing the extension
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(output_folder, png_filename)

            # Convert to PNG and save to the output folder
            img.save(png_path, 'PNG')
            print(f"Converted {filename} to {png_filename} and saved to {output_folder}")

print("All JPEG images have been converted to PNG format.")
