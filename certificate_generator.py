from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.pdfbase.pdfmetrics import stringWidth
from datetime import datetime


def generate_certificate(name, course, file_path):

    width, height = landscape(A4)

    c = canvas.Canvas(file_path, pagesize=(width, height))

    # Background
    c.setFillColor(colors.HexColor("#F8F5ED"))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Outer border
    c.setStrokeColor(colors.HexColor("#17365D"))
    c.setLineWidth(8)
    c.rect(25, 25, width - 50, height - 50)

    # Gold inner border
    c.setStrokeColor(colors.HexColor("#D4AF37"))
    c.setLineWidth(3)
    c.rect(40, 40, width - 80, height - 80)

    # Top blue strip
    c.setFillColor(colors.HexColor("#17365D"))
    c.rect(0, height - 18, width, 18, fill=1, stroke=0)

    # Title
    title = "CERTIFICATE OF COMPLETION"

    c.setFillColor(colors.HexColor("#17365D"))
    c.setFont("Helvetica-Bold", 28)

    title_width = stringWidth(title, "Helvetica-Bold", 28)

    c.drawString(
        (width - title_width) / 2,
        height - 115,
        title
    )

    # Subtitle
    subtitle = "This certificate is proudly presented to"

    c.setFillColor(colors.HexColor("#555555"))
    c.setFont("Helvetica", 14)

    subtitle_width = stringWidth(subtitle, "Helvetica", 14)

    c.drawString(
        (width - subtitle_width) / 2,
        height - 155,
        subtitle
    )

    # Name
    c.setFillColor(colors.HexColor("#111111"))
    c.setFont("Helvetica-Bold", 30)

    name_width = stringWidth(name, "Helvetica-Bold", 30)

    c.drawString(
        (width - name_width) / 2,
        height - 215,
        name
    )

    # Gold underline
    c.setStrokeColor(colors.HexColor("#D4AF37"))
    c.setLineWidth(2)

    c.line(
        width / 2 - 170,
        height - 230,
        width / 2 + 170,
        height - 230
    )

    # Completion text
    c.setFillColor(colors.HexColor("#555555"))
    c.setFont("Helvetica", 14)

    text = "for successfully completing the course"

    text_width = stringWidth(text, "Helvetica", 14)

    c.drawString(
        (width - text_width) / 2,
        height - 270,
        text
    )

    # Course
    c.setFillColor(colors.HexColor("#17365D"))
    c.setFont("Helvetica-Bold", 22)

    course_width = stringWidth(course, "Helvetica-Bold", 22)

    c.drawString(
        (width - course_width) / 2,
        height - 310,
        course
    )

    # Date
    date = datetime.now().strftime("%d %B %Y")

    c.setFillColor(colors.HexColor("#555555"))
    c.setFont("Helvetica", 11)

    c.drawString(90, 95, f"Date: {date}")

    # Signature line
    c.setStrokeColor(colors.HexColor("#333333"))
    c.setLineWidth(1)

    c.line(
        width - 250,
        110,
        width - 90,
        110
    )

    c.setFillColor(colors.HexColor("#333333"))
    c.setFont("Helvetica-Bold", 11)

    c.drawCentredString(
        width - 170,
        90,
        "Authorized Signature"
    )

    # Certificate seal
    c.setStrokeColor(colors.HexColor("#D4AF37"))
    c.setLineWidth(3)

    c.circle(
        width / 2,
        90,
        30,
        fill=0,
        stroke=1
    )

    c.setFillColor(colors.HexColor("#17365D"))
    c.setFont("Helvetica-Bold", 8)

    c.drawCentredString(
        width / 2,
        87,
        "CERTIFIED"
    )

    # Bottom strip
    c.setFillColor(colors.HexColor("#D4AF37"))
    c.rect(0, 18, width, 7, fill=1, stroke=0)

    c.setFillColor(colors.HexColor("#17365D"))
    c.rect(0, 0, width, 18, fill=1, stroke=0)

    # Save PDF
    c.save()