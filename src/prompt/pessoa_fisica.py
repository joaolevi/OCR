ATESTADO_SAUDE_OCUPACIONAL = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de saúde."},
        {"role": "user", "content": """Você deve analisar o texto extraído do documento ASO (Atestado de Saúde Ocupacional), verificar os seguintes pontos e retornar um JSON com as informações encontradas. Como isso é um ASO você deve focar em quais trabalhos ele está apto para operar. Procure em locais onde a palavra APTO aparece e onde podem existir marcações de caixas de seleção. Quando há marcações a caneta, o texto pode vir com falhas pois o OCR não conseguirá identificar corretamente, mas você pode inferir o que está escrito. Se houver marcações a lápis, o OCR pode não identificar corretamente, mas você pode inferir o que está escrito. Se houver marcações a caneta e a lápis, o OCR pode não identificar corretamente, mas você pode inferir o que está escrito. As perguntas são:
            1. O documento é um ASO?
            2. O documento é válido?
            3. O documento está assinado?
            4. Qual a validade do documento?
            5. Quais observações você encontrou no documento?
            6. Quais trabalhos o funcionário está apto a exercer?
            7. Quais exames foram realizados?
            8. Qual o nome do funcionário?
            9. Qual CPF do funcionário?
            10. Qual o nome do médico?
            11. Qual o CRM do médico?
            
            Modelo do JSON de resposta (Não adicione comentários no json):
            {
                "ASO": boolean,
                "valido": boolean,
                "assinado": boolean,
                "validade": datetime,
                "observacoes": string,
                "trabalhos_apto": list[string]
                "exames": list[string]
                "nome_funcionario": string,
                "cpf_funcionario": string,
                "nome_medico": string,
                "crm_medico": string
            }
            """},
            {"role": "assistant", "content": "Certo, vou analisar os textos extraído do documento ASO (Atestado de Saúde Ocupacional) e retornar um JSON com as informações encontradas."}
]

VERIFICADOR_TIPO_DOCUMENTO = [
    {"role": "system", "content": "Você é um assistente que verifica os tipos de documento"},
    {"role": "user", "content": "texto: "},
    {"role": "assistant", "content": "Certo, vou analisar o texto e retornar o tipo de documento."}
]

PROMPTS = {
    "ASO": ATESTADO_SAUDE_OCUPACIONAL
}