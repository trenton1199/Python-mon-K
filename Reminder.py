from datetime import date
import os
def pdf():
    pdf = input(f"would you like to turn  {file_name} into a pdf file? [y/n] ").lower()
    if pdf == 'y':
        pdf_name = input("what would you like the pdf file to be named ") + ".pdf"
        font_size = int(input("what would you like your font size to be?"))
        # Python program to convert
        # text file to pdf file

        from fpdf import FPDF

        # save FPDF() class into
        # a variable pdf
        pdf = FPDF()

        # Add a page
        pdf.add_page()

        # set style and size of font
        # that you want in the pdf
        pdf.set_font("Arial", size=font_size)

        # open the text file in read mode
        f = open(file_name, "r")

        # insert the texts in pdf
        for x in f:
            pdf.cell(200, 10, txt=x, ln=1, align='C')

        # save the pdf with name .pdf
        pdf.output(pdf_name)
question = input("Option A: create a new file or option B: continue with another file [a/b]").lower()
if question == 'a':
    date = str(date.today())
    file_name = input("what would you like the file name of this Reminder to be:") + ".txt"
    body = input("write your reminder here:")
    with open(file_name, 'w') as f:
        f.write(f"date: ")
        f.write(date)
        f.write(os.linesep)
        f.write(body)
        f.write(os.linesep)
        f.write(
            '----------------------------------------------------------------------------------------------------------------------------')
        f.write(os.linesep)
    pdf()
elif question == 'b':
    file_name = input("what is the previous file name for the To do list? (please do not provide file type):") + ".txt"
    date = str(date.today())
    body = input("write your reminder here:")
    with open(file_name, 'a') as f:
        f.write(f"date: ")
        f.write(date)
        f.write(os.linesep)
        f.write("To do:")
        f.write(body)
        f.write(os.linesep)
        f.write(
            '----------------------------------------------------------------------------------------------------------------------------')
        f.write(os.linesep)
    pdf()
