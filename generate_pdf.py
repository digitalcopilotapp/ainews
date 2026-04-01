from weasyprint import HTML

HTML('passagens_pato_branco.html').write_pdf(
    'passagens_pato_branco_08ago2026.pdf',
    presentational_hints=True
)
print("PDF gerado: passagens_pato_branco_08ago2026.pdf")
