import PyPDF2
import sys
import os

path = "C:\\Users\\Kinjal Gujral\\OneDrive\\Desktop\\editimgs"
merger=PyPDF2.PdfMerger()

for file in os.listdir(path):
    if(file.endswith(".pdf")):
        full_path = os.path.join(path, file)  # Join path and filename to get full file path
        print(full_path)  # Print full file path for verification
        merger.append(full_path)
merger.write("C:\\Users\\Kinjal Gujral\\OneDrive\\Desktop\\editimgs\\combineddocs.pdf")
merger.close()  # Close the merger object after writing the file

print("Merged PDF files successfully!")

#