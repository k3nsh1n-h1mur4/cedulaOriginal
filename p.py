from fpdf import FPDF
from fpdf.enums import StrokeJoinStyle

pdf = FPDF()
pdf.add_page()
with pdf.local_context(stroke_join_style=StrokeJoinStyle.ROUND):
    pdf.rect(25, 30, 170, 80, round_corners=True, style="D")
    pdf.rect(26, 31, 168, 78, round_corners=True, style="D")
pdf.output("squares.pdf")