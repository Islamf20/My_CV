from fpdf import FPDF

class CV(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Islam Ud Din', 0, 1, 'C')
        self.cell(0, 10, 'Computer Engineering', 0, 1, 'C')
        self.ln(10)

    def add_section(self, title, content):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('Arial', '', 12)
        for line in content:
            self.multi_cell(0, 10, line)
        self.ln(5)

pdf = CV()
pdf.add_page()
pdf.add_section('Education', [
    'B.S. in Computer Engineering, National University Of Technology Islamabad, 2024',
    'Relevant Courses: AI, Machine Learning, Data Structures'
])
pdf.add_section('Experience', [
    'Software Engineer at XYZ Company, Year-Year',
    'Responsibilities: Developed X, Y, Z'
])
pdf.output('your_cv.pdf')
