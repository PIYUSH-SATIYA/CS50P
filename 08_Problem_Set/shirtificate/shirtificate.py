from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 24)
        self.cell(0, 20, "CS50 Shirtificate", ln=True, align="C")


def main():
    name = input("Name: ")

    pdf = PDF()
    pdf.add_page()

    pdf.image("shirtificate.png", x=0, y=40, w=210)

    pdf.set_font("Arial", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 90)
    pdf.cell(210, 40, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
