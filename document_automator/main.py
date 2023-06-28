import pandas as pd
from docxtpl import DocxTemplate
from datetime import datetime

doc = DocxTemplate("en-template-manager-info.docx")
my_context = { 'my_phone' : "(123) 456789)",
              'my_email': 'juanignaciogiacobbe@gmail.com',
              'my_address': 'big street 1',
              'my_name': 'Juan Ignacio Giacobbe',
              'fecha_hoy': datetime.today().strftime("%d %b, %Y")}

df = pd.read_csv('en_fake_data.csv')

for index, row in df.iterrows():
    context = {
        'hiring_manager_name': row['name'],
        'address': row['address'],
        'phone_number': row['phone_number'],
        'email': row['email'],
        'job_position': row['job'],
        'company_name': row['company']
    }

    context.update(my_context)

    doc.render(context)
    doc.save(f"generated_doc_{index + 1}.docx")