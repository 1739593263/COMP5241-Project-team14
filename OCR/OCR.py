import os
import fitz  # PyMuPDF

# Path to the resources folder
resources_folder = 'Resources'
output_folder = 'extracted_texts'

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Walk through the resources folder
for root, dirs, files in os.walk(resources_folder):
    for file in files:
        if file.endswith('.pdf'):
            pdf_path = os.path.join(root, file)
            # Open the PDF file
            pdf_document = fitz.open(pdf_path)
            
            # Initialize text variable
            extracted_text = ""
            
            # Perform text extraction on each page
            for page_num in range(len(pdf_document)):
                page = pdf_document.load_page(page_num)
                text = page.get_text()
                extracted_text += text + "\n"
            
            # Save the extracted text to a corresponding .txt file
            txt_filename = os.path.splitext(file)[0] + '.txt'
            txt_path = os.path.join(output_folder, txt_filename)
            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                txt_file.write(extracted_text)