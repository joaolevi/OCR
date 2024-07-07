# OCR com Pytesseract e Llama3

Esse repositório contêm uma API para extração de campos de um documento com a simples ideia de captação do texto de um documento com o Tesseract e a extração dos campos/informações utilizando o Llama3 como ferramente de NLP.

#### Vantagens: 
- Implementação simples: precisamos simplesmente de duas ferramentas, o Tesseract e o Llama3 (pode ser substituido pelo GPT-4o, GPT-4, GPT-3.5-turbo da OpenAI com a chave de API).
- Extração via prompt: Não há necessidade de manipularmos strings com expressões regulares ou criar lógicas complexas. A LLM através do prompt fornecido usando linguagem natural já fará isso por nós.

#### Desvantagens:
- Um pouco de imprevisibilidade: dependendo do tipo de LLM usada a chances do retorno não ser exatamente o que é esperado.
- Alto poder computacional esperado: para rodar a LLM localmente é necessário ao menos 16gb de RAM ou uma GPU. Mas esses requisitos mínimos tem dificuldade de processar e podem levar em média 2 minutos para responder a requisição. Para um bom desempenho, ao menos 32gb de RAM e uma GPU com mais de 4gb de RAM.

## Rodando o projeto:

Para rodar o projeto é necessário ter o Docker instalado. Todas as bibliotecas e dependências serão instaladas via Docker.

1. No diretório do projeto digite: `docker build -t ocrapi .`
2. Após o build: `docker run -dp 5001:5001 --name ocrapi ocrapi`

O comando o argumento `-dp 50001:5001` roda o container no modo detached e binda a porta 5001 para que fique disponível para requisição externa.

Com o container rodando, é possível fazer uma requisição para a API passando a URL como argumento do body json e o prompt como segundo argumento. Exemplo:

```
{
    "url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fmanuais.ifsp.edu.br%2Fbooks%2Fcgi-documentos-eletronicos-suap%2Fpage%2F9-vinculando-documentos&psig=AOvVaw2ue09NuhvtNjPm2JkphtT-&ust=1720449963858000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCMiU09mVlYcDFQAAAAAdAAAAABAE",
    "prompt": "você é um assistente que analisa documentos. Dado o texto do documento, extraia o qualquer nome que exista no documento e devolva no formato json."
}
```

# Guia de Engenharia de Prompt (by João Levi Gomes de Lima)

## Introdução

Engenharia de prompt é a arte e ciência de criar instruções claras e precisas para que um modelo de inteligência artificial (IA) compreenda e execute tarefas específicas. Com a evolução dos modelos de linguagem, como o GPT-4 e o Llama3, a habilidade de formular prompts eficazes tornou-se crucial para desenvolvedores que desejam maximizar a eficiência e precisão das respostas geradas pela IA.

## O que é Engenharia de Prompt?

Engenharia de prompt envolve a criação de comandos textuais (prompts) que orientam o comportamento de um modelo de IA. Um prompt bem elaborado deve ser:

1. **Claro**: Evite ambiguidades e certifique-se de que o modelo entenda exatamente o que deve fazer.
2. **Conciso**: Use a menor quantidade de palavras possível para transmitir a mensagem.
3. **Contextualizado**: Inclua contexto suficiente para que o modelo compreenda o cenário e forneça uma resposta relevante.
4. **Específico**: Detalhe exatamente o que o modelo deve buscar ou verificar.

## Modelos de Prompt

- Embeddings (mais utilizado) - O texto é vetorizado e embarcado e é feita uma pesquisa usando indexação e técnicas matemáticas para encontrar a resposta solicitada no prompt. Esse modelo é muito utilizado para extração de informações.
- Chat - A partir da definição das `roles` e dos `contents` fornecidos, como se fosse uma conversa, o modelo aprende a responder as novas mensagens se baseando no que foi fornecido. Esse tipo de aprendizado se chama "Few-short learning" ou "Fining tuning" dependendo da quantidade de dados fornecida e/ou do tipo de aprendizado. Muito utilizado para chatbots.

### Role, Task e Context

Para criar um prompt eficaz, é importante considerar três componentes essenciais: **Role** (Papel), **Task** (Tarefa) e **Context** (Contexto).

1. **Role (Papel)**:
    - Define o papel ou a identidade que o modelo deve assumir. Isto ajuda a alinhar o comportamento do modelo com as expectativas do usuário.
    - Exemplo: "Você é um assistente que verifica documentos de pagamentos."

2. **Task (Tarefa)**:
    - Especifica a tarefa ou objetivo principal que o modelo deve alcançar. Esta seção deve ser clara e precisa para evitar interpretações errôneas.
    - Exemplo: "Você deve analisar o texto extraído dos documentos de pagamentos onde uma das páginas contém o boleto e outra deve conter o comprovante de pagamento."

3. **Context (Contexto)**:
    - Fornece informações adicionais que ajudam o modelo a entender a situação e a responder de maneira adequada.
    - Exemplo: "Verifique os seguintes pontos e retorne um JSON com as informações encontradas."

## Exemplo de Prompt Único (Pesquisa por Embedding)

Vamos analisar um exemplo de prompt para um assistente que verifica documentos de pagamentos. O objetivo deste prompt é instruir o modelo a analisar o texto extraído de documentos de pagamento, identificar informações específicas e retornar um JSON com os dados encontrados.

### Prompt

```
Você é um assistente que verifica documentos de pagamentos. Você deve analisar o texto extraído dos documentos de pagamentos onde uma das páginas contém o boleto e outra deve conter o comprovante de pagamento. Verifique os seguintes pontos e retorne um JSON com as informações encontradas. As perguntas são:

1. Existe um boleto e um comprovante de pagamento? Responda com true ou false.
2. Quando o boleto foi gerado?
3. Qual a validade do boleto?
4. Os valores em dinheiro do boleto e comprovante coincidem, desconsiderando o tipo da moeda ou se um dos valores não apresenta o tipo da moeda? Caso mostre e haja apenas uma diferença de dígito, responda como true, ignore a diferença de pontos e vírgulas.
5. Se o comprovante mostra o código do boleto, ele coincide com o código apresentado no boleto sem considerar os "-"? Caso não mostre e exista um comprovante, responda como true. Caso mostre e haja apenas uma diferença de dígito, responda como true.
6. Qual o banco do comprovante?
7. Qual o CNPJ apresentado no boleto?
8. Qual o CNPJ apresentado no comprovante?
9. Qual o nome da empresa apresentado no boleto?
10. Qual o nome da empresa apresentado no comprovante?
11. Qual o tipo de boleto? Responda com BOLETO_FGTS, BOLETO_DARF, BOLETO_INSS ou BOLETO_SINDICATO

Modelo do JSON de resposta, não adicione comentários no JSON e deve ser retornado como resposta:
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
    "document_type": string
}
```'
``` 

#### Atentem-se para o  ```json { }````!
Esse formato força a LLM a retornar uma resposta com o json dentro do ```json { }```` permitindo que o software consiga extrair e converter a resposta para o formato json padrão.

### Análise do Prompt

1. **Role (Papel)**: "Você é um assistente que verifica documentos de pagamentos." Isso define a identidade do modelo, guiando suas ações.
2. **Task (Tarefa)**: "Você deve analisar o texto extraído dos documentos de pagamentos onde uma das páginas contém o boleto e outra deve conter o comprovante de pagamento." Isso especifica claramente a tarefa que o modelo deve realizar.
3. **Context (Contexto)**: As perguntas fornecem o contexto necessário para que o modelo saiba exatamente quais informações buscar e como organizá-las na resposta (O modelo JSON informado é um exemplo).


### Adicionando, editando ou removendo perguntas:

Caso queiramos extrair mais informações ou retirar algumas já solicitadas, podemos manipular o prompt simplesmente adicionando ou removendo as perguntas e os campos do json.

#### Adicionando: 

Supondo que queremos extrair a informação do valor em dinheiro do comprovante. Podemos criar uma nova pergunta `12. Qual o valor pago no comprovante?` podemos definir como queremos que ele devolva o valor `12. Qual o valor pago no comprovante? Devolva apenas os números e pontuações sem R$`. E agora adicionamos como queremos que o campo seja devolvido no JSON juntamente do tipo de dado:

```
...
9. Qual o nome da empresa apresentado no boleto?
10. Qual o nome da empresa apresentado no comprovante?
11. Qual o tipo de boleto? Responda com BOLETO_FGTS, BOLETO_DARF ou BOLETO_INSS
12. Qual o valor pago no comprovante? Devolva apenas os números e pontuações sem o R$
...
```

```
{
    ...
    "nome_empresa_comprovante": string,
    "document_type": string,
    "valor_pago": float,
}
```

#### Editando:

Agora no lugar de saber o CNPJ da empresa pagante, queremos o CNPJ do banco que gerou o comprovante (caso seja possível coletar essa informação). Podemos simplesmente editar a pergunta `8. Qual o CNPJ apresentado no comprovante?` para `8. Qual o CNPJ do banco gerador do comprovante?`. Assim, alteramos a regra imposta na pergunta definindo bem o que e de quem queremos extrair a informação.

#### Removendo:

Supondo que a pergunta abaixo não nos interesse mais:

`11. Qual o tipo de boleto? Responda com BOLETO_FGTS, BOLETO_DARF, BOLETO_INSS ou BOLETO_SINDICATO`

Podemos removê-la do prompt na região das perguntas e da região do modelo json fornecido. 

## Exemplo de Prompt no Modelo Chat

```
{"role": "system", "content": "Você é uma assistente virtual para um delivery"}
{"role": "user", "content": "Olá, estou com um problema com meu pedido. Ele ainda não chegou."}
{"role": "assistant", "content": "Olá! Desculpe pelo inconveniente. Por favor, forneça o número do seu pedido para que possamos verificar."}
{"role": "user", "content": "Meu pedido veio errado, recebi um item diferente."}
{"role": "assistant", "content": "Peço desculpas por isso. Você poderia nos dizer qual foi o item que veio errado e qual deveria ter vindo?"}
{"role": "user", "content": "Eu gostaria de saber quanto tempo leva para a entrega."}
{"role": "assistant", "content": "Normalmente, nosso tempo de entrega é de aproximadamente 30 a 45 minutos. Pode variar dependendo do tráfego e da demanda."}
```

- Sempre que iniciamos o modelo chat precisamos definir qual será a função do assistente. Para isso, definimos a `role` como `system` e dizemos qual papel queremos que a assistente assuma no campo `content`.

- A partir desse momento, todas as mensagens devem conter uma mensagem do usuário com a role `user` e uma resposta da assistente com a role `assistant`.

- Não é obrigatório definir o `system` ou seguir a sequência `user` -> `assistant` porém, isso ajudará na organização dos dados e entendimento por parte da LLM.

# Modelo de Prompt Genérico para Extração de Informação

Abaixo, segue um modelo de prompt para ser editado e utilizado em diversos casos. Atentem-se sempre a fornecer um contexto com mais detalhes possíveis e a definir bem as roles e tasks. Quanto melhor definimos qual o papel da LLM e quais regras ela deve seguir, mais evitamos que ela se perca e comece a alucinar (quando ela foge do contexto).

```
Você é um assistente que [PAPEL DO ASSISTENTE]. Você deve analisar [CONTEXTO]. 

## REGRAS:

Verifique os seguintes pontos e retorne um JSON com as informações encontradas. As perguntas são:

1. Pergunta número 1?
2. Pergunta número 2?
3. Pergunta número 3?
4. Pergunta número 4?
...

## FORMATO DA SAÍDA

Modelo do JSON de resposta, não adicione comentários no JSON e deve ser retornado como resposta:
```json
{
    "campo_a_ser_retornado_1": boolean,
    "campo_a_ser_retornado_2": datetime,
    "campo_a_ser_retornado_3": string,
    "campo_a_ser_retornado_4": float,
    ...
}
```'
```
## Outros tipos de saídas

No exemplo de extração de informações do documento, solicitamos que a saída viesse no formato JSON, mas também podemos solicitar em diversos outros formatos como XML, CSV, DOCX, etc. Sempre fornecendo um exemplo, conseguimos limitar o modo como o modelo irá responder fazendo-o retornar exatamente da maneira que queremos receber a resposta.

### XML

```
Modelo de saída XML, não adicione comentários no XML e deve ser retornado como resposta:
```xml
<nome_do_documento>
    <campo1>[string]</campo1>
    <campo2>[string]</campo2>
    <campo3>[datetime]</campo3>
    <campo4>[string]</campo4>
    <conteudo_principal>[string]</conteudo_principal>
    <anexos>
        <anexo>[string]</anexo>
        <!-- Repita o elemento <anexo> conforme necessário -->
    </anexos>
</nome_do_documento>
```'
```

### CSV

```
Modelo de saída CSV, não adicione comentários no CSV e deve ser retornado como resposta:
```csv
nota,titulo,texto_revisao,caracteristica_mencionada,problema_mencionado
[float],[string],[string],[string],[string]
```'
```

### Docx

```
Modelo de saída DOCX, não adicione comentários no DOCX e deve ser retornado como resposta. Estruture o documento da seguinte forma:

Título: [string]
Autores: [string]
Resumo: [string]
Data de Publicação: [datetime]
Revista/Conferência: [string]
Palavras-chave: [string]
Conclusão Principal: [string]
```

### SQL

```
## Extração de informações de registros de clientes com saída em SQL:

Você é um assistente que analisa registros de clientes. Você deve ler os registros e extrair informações importantes. As perguntas são:

1. Qual é o ID do cliente?
2. Qual é o nome do cliente?
3. Qual é o e-mail do cliente?
4. Qual é a data de registro do cliente?
5. Qual é o status do cliente (ativo/inativo)?

Modelo de saída SQL, não adicione comentários no SQL e deve ser retornado como resposta:
```sql
INSERT INTO clientes (id_cliente, nome_cliente, email_cliente, data_registro, status_cliente) VALUES ([int], '[string]', '[string]', '[datetime]', '[string]');
```'
```
