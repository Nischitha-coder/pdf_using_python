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
    pdf.line(10, 30, 200, 30)

    #set footer
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0, h=0, txt=topic["Topic"], align="R")

    for i in range(topic["Pages"]-1):
        pdf.add_page()
        # set footer
        pdf.ln(278)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=0, txt=topic["Topic"], align="R")



pdf.output("output.pdf")