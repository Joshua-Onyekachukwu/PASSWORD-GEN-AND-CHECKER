import os
from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO



def add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path):
    # Read the watermark PDF
    with open(watermark_pdf_path, 'rb') as watermark_file:
        watermark_reader = PdfReader(watermark_file)
        watermark_page = watermark_reader.pages[0]  # Assuming the watermark is on the first page

        # Read the input PDF
        with open(input_pdf_path, 'rb') as input_file:
            input_reader = PdfReader(input_file)
            output_writer = PdfWriter()

            # Add watermark to each page
            for page_num in range(len(input_reader.pages)):
                page = input_reader.pages[page_num]
                page.merge_page(watermark_page)  # Merge watermark with the page
                output_writer.add_page(page)

            # Save the result to a new PDF
            with open(output_pdf_path, 'wb') as output_file:
                output_writer.write(output_file)

def watermark_single_pdf(input_pdf_path, watermark_pdf_path, output_pdf_path):
    add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path)
    print(f"Watermarked single PDF saved to {output_pdf_path}")

def watermark_all_pdfs_in_folder(folder_path, watermark_pdf_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all PDFs in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            input_pdf_path = os.path.join(folder_path, filename)
            output_pdf_path = os.path.join(output_folder, f"watermarked_{filename}")

            add_watermark(input_pdf_path, watermark_pdf_path, output_pdf_path)
            print(f"Watermarked {filename} saved to {output_pdf_path}")

# Usage example:
watermark_pdf = "./pdf/wtr.pdf"  # Path to the PDF you want to use as a watermark
input_pdf = "Super.pdf"       # Path to the input PDF you want to watermark
output_pdf = "watermarked_Super.pdf"  # Output path for the watermarked PDF

# Watermark a single PDF
watermark_single_pdf(input_pdf, watermark_pdf, output_pdf)

# Watermark all PDFs in a folder
input_folder = "pdf"  # Folder containing PDFs to watermark
output_folder = "watermarked_pdfs"  # Folder to save watermarked PDFs

watermark_all_pdfs_in_folder(input_folder, watermark_pdf, output_folder)
