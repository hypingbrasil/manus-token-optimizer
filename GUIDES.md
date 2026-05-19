# Guia de Otimização de Tokens 🧠

Este guia detalha estratégias técnicas para reduzir o consumo de tokens e aumentar a velocidade de resposta do Manus.

## 1. Engenharia de Prompt Concisa
A verbosidade é a maior inimiga da eficiência.
- **Evite polidez excessiva**: "Por favor, você poderia gentilmente criar..." → "Crie..."
- **Elimine redundâncias**: "Explique de forma detalhada e com muitos pormenores..." → "Explique detalhadamente..."

## 2. Técnicas Avançadas
### Skeleton-of-Thought (SoT)
Em vez de pedir um texto gigante de uma vez, peça primeiro o sumário ou estrutura.
1. **Passo 1**: "Crie o sumário para um artigo sobre [X]."
2. **Passo 2**: "Escreva a seção 1 baseada no sumário anterior."
*Isso evita que a IA se perca e gere conteúdo irrelevante no meio de um texto longo.*

### Delimitadores de Contexto
Use delimitadores claros para separar instruções de dados.
- Exemplo: `### CONTEXTO ###`, `--- DADOS ---`.
- Isso ajuda a IA a identificar rapidamente o que é comando e o que é informação, reduzindo o processamento de "ruído".

## 3. Controle de Saída
Definir o formato de saída é crucial para economizar tokens de resposta.
- **Tabelas**: Frequentemente mais densas em informação e usam menos tokens que parágrafos longos.
- **Listas (Bullet Points)**: Evitam conectivos gramaticais desnecessários.
- **Limites de Caracteres**: "Resuma em no máximo 100 palavras."

## 4. Otimização de Dados de Entrada
- **Limpeza de Texto**: Se estiver enviando um artigo para análise, remova menus de navegação, rodapés e anúncios antes de colar no chat.
- **Compressão de Contexto**: Se precisar referenciar um código longo, envie apenas as funções ou classes relevantes.

## 5. Uso de Ferramentas (Tools)
O Manus possui ferramentas poderosas. Em vez de pedir para ele "imaginar" ou "simular" algo que gaste muitos tokens de raciocínio:
- Use `shell` para cálculos complexos.
- Use `webpage_extract` para ler sites (é mais eficiente que pedir para o navegador ler e resumir visualmente).
