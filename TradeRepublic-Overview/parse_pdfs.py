import os
import re
import PyPDF2

def parse_pdf(file):
    with open(file, "rb") as infile:
        pdf_reader = PyPDF2.PdfFileReader(infile)
        extracted_text = pdf_reader.getPage(0).extractText()
        isin_t = re.findall(r"ISIN: (.*?) ", extracted_text)[0]

        isin = isin_t[:12]
        quantity = isin_t[12:]
        price = re.findall(r" Stk\.(.*?) ", extracted_text)[0]

        print(f"Bought {quantity} x {isin} at {price}")
    
    dic = dict()
    dic["isin"] = isin
    dic["quantity"] = float(quantity)
    dic["price"] = float(price.replace(",", "."))

    return dic

def export_values(folder, values):
    with open(os.path.join(folder, "positions.csv"), "w") as csv:
        csv.write("ISIN;QUANTITY;PRICE;\n")
        for dic in values:
            csv.write(";".join([dic.get("isin"), str(dic.get("quantity")), \
                str(dic.get("price"))]) + "\n")

def parse_pdfs(folder):
    values = []

    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".pdf"):
                value = parse_pdf(os.path.join(root, file))
                values.append(value)

    export_values(folder, values)

    return values