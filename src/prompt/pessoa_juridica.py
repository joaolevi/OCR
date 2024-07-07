PAGAMENTOS = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de pagamentos"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de pagamentos onde uma das páginas contem o boleto e outra deve contar o comprovante de pagamento. Verifique os seguintes pontos e retorne um JSON com as informações encontradas. As perguntas são:
            1. Existe um boleto e um comprovante de pagamento? Responda com true ou false.
            2. Quando o boleto foi gerado?
            3. Qual a validade do boleto?
            4. Os valores em dinheiro do boleto e comprovante coincidem, desconsiderando o tipo da moeda ou se um dos valores não apresenta o tipo da moeda? Caso mostre e haja apenas uma diferença de digito, responda como true, ignore a diferença de pontos e vírgulas.
            5. Se o comprovante mostra o código do boleto, ele coincide com o código apresentado no boleto sem considerar os "-"? Caso não mostre e exista um comprovante, responda como true. Caso mostre e haja apenas uma diferença de digito, responda como true.
            6. Qual o banco do comprovante?
            7. Qual o CNPJ apresentado no boleto? 
            8. Qual o CNPJ apresentado no comprovante?
            9. Qual o nome da empresa apresentado no boleto?
            10. Qual o nome da empresa apresentado no comprovante?
            11. Qual o tipo de boleto? Responda com BOLETO_FGTS, BOLETO_DARF, BOLETO_INSS ou BOLETO_SINDICATO
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "existe_boleto_comprovante": boolean,
                "data_geracao": datetime,
                "validade": datetime,
                "valores_coincidem": boolean,
                "numero_boleto_coincide": boolean,
                "banco_comprovante": string,
                "cnpj_boleto": string,
                "cnpj_comprovante": string,
                "nome_empresa_boleto": string,
                "nome_empresa_comprovante": string,
                "document_type": string,
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

PROTESTOS = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de protestos"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de protestos, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Nome do orgão emissor
            2. Data da emissão
            3. Constatação de protesto: responda com CONSTA ou NÃO CONSTA
            4. Nome da empresa
            5. CNPJ da empresa
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "orgao_emissor": string,
                "data_emissao": datetime,
                "constatacao_protesto": string,
                "nome_empresa": string,
                "cnpj_empresa": string
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

INSCRICAO_MUNICIPAL = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de inscrição municipal"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de inscrição municipal, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Razão social
            2. Nome fantasia
            3. CNPJ da empresa
            4. Inscrição municipal
            5. Data da inscrição
            6. CNAE principal
            7. CNAE secundário 
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "razao_social": string,
                "nome_fantasia": string,
                "cnpj_empresa": string,
                "inscricao_municipal": string,
                "data_inscricao": datetime,
                "cnae_principal": string,
                "cnae_secundario": string
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

DECLARACAO_GERAL = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de declaração"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de declaração, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Nome do declarante
            2. CPF do declarante
            3. Data da declaração
            4. Descrição da declaração
            5. Título da declaração
            6. Está assinado?
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "nome_declarante": string,
                "cpf_declarante": string,
                "data_declaracao": datetime,
                "descricao_declaracao": string,
                "titulo_declaracao": string,
                "assinado": boolean
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

APOLICE_SEGURO = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de apólice de seguro"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de apólice de seguro, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Nome do segurado
            2. CNPJ do segurado
            3. Data de início da vigência
            4. Data de fim da vigência
            5. Valor segurado
            6. Tipo de seguro
            7. Número da apólice
            8. Nome da seguradora
            9. Data da emissão
            10. Está assinado?

            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "nome_segurado": string,
                "cnpj_segurado": string,
                "data_inicio_vigencia": datetime,
                "data_fim_vigencia": datetime,
                "valor_segurado": float,
                "tipo_seguro": string,
                "numero_apolice": string,
                "nome_seguradora": string,
                "data_emissao": datetime,
                "assinado": boolean
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

CONTRATO_SOCIAL = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de contrato social"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de contrato social, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Razão social
            2. Nome fantasia
            3. CNPJ da empresa
            4. Data de abertura
            5. Nome dos sócios
            6. CPF dos sócios
            7. Participação dos sócios
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "razao_social": string,
                "nome_fantasia": string,
                "cnpj_empresa": string,
                "data_abertura": datetime,
                "socios": list[string],
                "cpf_socios": list[string],
                "participacao_socios": list[float]
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

CARTAO_CNPJ = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de cartão CNPJ"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de cartão CNPJ, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. Razão social
            2. Nome fantasia
            3. CNPJ da empresa
            4. Data de abertura
            5. CNAE principal
            6. CNAE secundário
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "razao_social": string,
                "nome_fantasia": string,
                "cnpj_empresa": string,
                "data_abertura": datetime,
                "cnae_principal": string,
                "cnae_secundario": string
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

CERTIFICADO_REGULARIDADE_FGTS = [
        {"role": "system", "content": "Você é um assistente que verifica documentos de certificado de regularidade do FGTS"},
        {"role": "user", "content": """Você deve analisar o texto extraído dos documentos de certificado de regularidade do FGTS, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. CNPJ da empresa
            2. Data de emissão
            3. Data de validade
            4. Está regular?
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            ```json
            {
                "cnpj_empresa": string,
                "data_emissao": datetime,
                "data_validade": datetime,
                "regular": boolean
            }
            ```
            """},
        {"role": "assistant", "content": "Certo, vou analisar os textos extraidos dos documentos e retornar um JSON com as informações encontradas."}
]

CERTIDAO_NEGATIVA_DEBITO = [
        """Você é um assistente que verifica documentos de certidão negativa de débito federal. Você deve analisar o texto extraído dos documentos de certidão negativa de débito federal, verificar os seguintes pontos e retornar um JSON com as informações encontradas. As perguntas são:
            1. CNPJ da empresa
            2. Data de emissão
            3. Data de validade
            4. Situação? Responda com POSITIVA, NEGATIVA ou POSITIVA COM EFEITO NEGATIVO
            
            Modelo do JSON de resposta, não adicione comentários no json e deve ser retornado como resposta:
            {
                "cnpj_empresa": string,
                "data_emissao": datetime,
                "data_validade": datetime,
                "situacao": string
            }
            """
]

VERIFICADOR_TIPO_DOCUMENTO = [
        {"role": "system", "content": "Você é um assistente que verifica o tipo de documento de pessoa jurídica"},
        {"role": "user", "content": "Você deve analisar o texto extraído do documento de pessoa jurídica, e dizer se o documento é um CONTRATO_SOCIAL, CARTAO_CNPJ, CERTIFICADO_REGULARIDADE_FGTS, CERTIDAO_NEGATIVA_DEBITO, APOLICE_SEGURO, INSCRICAO_MUNICIPAL, DECLARACAO_GERAL, PROTESTOS ou PAGAMENTOS. Responda com apenas com uma palavra."},
        {"role": "assistant", "content": "Certo, vou analisar o texto extraido do documento e retornar o tipo de documento com apenas uma palavra."}
]

PROMPTS = {
    "CONTRATO_SOCIAL": CONTRATO_SOCIAL,
    "CARTAO_CNPJ": CARTAO_CNPJ,
    "CERTIFICADO_REGULARIDADE_FGTS": CERTIFICADO_REGULARIDADE_FGTS,
    "CERTIDAO_NEGATIVA_DEBITO": CERTIDAO_NEGATIVA_DEBITO,
    "APOLICE_SEGURO": APOLICE_SEGURO,
    "INSCRICAO_MUNICIPAL": INSCRICAO_MUNICIPAL,
    "DECLARACAO_GERAL": DECLARACAO_GERAL,
    "PROTESTOS": PROTESTOS,
    "PAGAMENTOS": PAGAMENTOS
}