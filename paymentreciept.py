from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Function to create a PDF receipt
def generate_receipt(customer_name, invoice_number, payment_amount):
    # Create a PDF document
    pdf_filename = f"receipt_{invoice_number}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Create a table for the receipt content
    data = [
        ["Invoice Number:", invoice_number],
        ["Customer Name:", customer_name],
        ["Payment Amount:", f"${payment_amount:.2f}"],
    ]

    table = Table(data, colWidths=200, rowHeights=30)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # Build and save the PDF
    elements = []
    elements.append(table)
    doc.build(elements)

    print(f"Receipt saved as {pdf_filename}")

# Example usage
if __name__ == "__main__":
    customer_name = input("Enter name-----")
    invoice_number = input("Enter invoice number------")
    payment_amount = int(input("Enter Amount-------"))

    generate_receipt(customer_name, invoice_number, payment_amount)
