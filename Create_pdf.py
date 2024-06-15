from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="a4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, topic in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=20, txt=topic["Topic"], align="c", ln=1, border=0)

    #set footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=0, txt=topic["Topic"], align="R")

    #lines for the pdf
    # for i in range(3, 29):
    #     pdf.line(10, i*10, 200, i*10)
    for y in range(30, 290, 10):
        pdf.line(10, y, 200, y)

    for i in range(topic["Pages"]-1):
        pdf.add_page()
        # set footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=0, txt=topic["Topic"], align="R")
        # lines for the pdf
        for i in range(2, 29):
            pdf.line(10, i * 10, 200, i * 10)

pdf.output("output.pdf")