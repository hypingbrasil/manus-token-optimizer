# manus-token-optimizer: Otimização Cognitiva para Manus

## Descrição
Esta skill integra um conjunto de ferramentas e diretrizes para otimizar o uso de tokens e maximizar a eficiência das interações com o Manus. Ela visa aprimorar a capacidade cognitiva do agente através de pré-processamento inteligente de dados, orquestração de tarefas complexas e refinamento de saídas, agindo como um "aditivo de foguete" para as operações do Manus.

## Funcionalidades Principais
- **Compressão Semântica**: Reduz a verbosidade de textos de entrada, extraindo a essência e palavras-chave, economizando tokens e focando a atenção do agente.
- **Orquestração Recursiva**: Permite quebrar tarefas complexas em sub-tarefas menores e gerenciáveis, facilitando a resolução de problemas de grande escala.
- **Refinamento de Saída Estruturada**: Garante que as saídas geradas (JSON, texto) sejam limpas, válidas e no formato esperado, otimizando o pós-processamento.

## Como o Agente Deve Usar Esta Skill
O agente DEVE incorporar os princípios e ferramentas desta skill em seu fluxo de trabalho padrão para todas as tarefas que envolvam processamento de texto, planejamento complexo ou geração de saídas estruturadas.

### Diretrizes de Uso Automático:
1.  **Pré-processamento de Entradas**: Antes de processar qualquer texto longo ou dado complexo fornecido pelo usuário ou obtido de ferramentas (ex: `webpage_extract`, `file read`), o agente DEVE considerar a aplicação do `semantic_compressor.py` para reduzir o volume de tokens e focar nas informações mais relevantes.
2.  **Planejamento de Tarefas Complexas**: Para tarefas que o agente identifique como multi-etapas ou que exijam um raciocínio aprofundado, o agente DEVE simular ou aplicar a lógica do `recursive_orchestrator.py` para quebrar o problema em partes menores e sequenciais, gerenciando cada sub-tarefa de forma otimizada.
3.  **Pós-processamento de Saídas**: Após gerar qualquer saída estruturada (especialmente JSON) ou textual que será apresentada ao usuário ou usada em etapas subsequentes, o agente DEVE utilizar o `structured_output_refiner.py` para validar, limpar e formatar os dados, garantindo a qualidade e a conformidade.
4.  **Priorização da Concisão**: Em todas as interações, o agente DEVE priorizar a comunicação concisa e direta, seguindo as diretrizes de engenharia de prompt descritas em `GUIDES.md` e `TEMPLATES.md`.

## Localização das Ferramentas
Os scripts Python estão localizados no diretório `/home/ubuntu/manus-token-optimizer/scripts/`.

## Integração com `manus-config`
Esta skill será carregada via `manus-config` como uma instrução de projeto para garantir que o agente adote estas práticas de forma persistente e automática em todas as interações.

---
*Esta skill é um mecanismo interno para otimizar o desempenho do agente e não altera as políticas de faturamento ou limites de crédito da plataforma Manus.*
