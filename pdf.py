import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print (pdf)
        merger.append(pdf)
    merger.write('Super.pdf')
    merger.close()

pdf_combiner(inputs)














# print(PyPDF2.__version__)
# print(dir(PyPDF2))

# with open('./pdf/220 - dummy.pdf', 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     page = reader.pages[0]
#     page.rotate(90)
#
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#
#     with open('./pdf/22 - superTilt.pdf', 'wb') as output_file:
#         writer.write(output_file)