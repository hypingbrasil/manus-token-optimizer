# Ferramentas Python para Otimização Cognitiva do Manus 🛠️

Este diretório contém scripts Python projetados para atuar como "aditivos de foguete" para o Manus, otimizando seu fluxo de trabalho e expandindo suas capacidades cognitivas através da manipulação eficiente de dados e tarefas.

## 📂 Estrutura do Diretório `scripts/`

| Arquivo | Descrição |
| :--- | :--- |
| `semantic_compressor.py` | Comprime informações textuais, extraindo palavras-chave e resumos para reduzir o volume de tokens de entrada. |
| `recursive_orchestrator.py` | Divide tarefas complexas em sub-tarefas menores e gerenciáveis, permitindo que o Manus lide com problemas de grande escala de forma recursiva. |
| `structured_output_refiner.py` | Valida e refina saídas geradas, especialmente JSON e texto, garantindo a integridade e a limpeza dos dados. |

## 🚀 Como Usar

### 1. `semantic_compressor.py`

**Função**: `semantic_compressor(text, top_n_keywords=5, summary_sentences=3)`

**Descrição**: Recebe um texto longo e retorna as palavras-chave mais relevantes e um resumo conciso. Ideal para pré-processar grandes volumes de texto antes de enviá-los ao Manus, economizando tokens.

**Exemplo de Uso (no seu ambiente Python)**:

```python
from scripts.semantic_compressor import semantic_compressor

long_text = "Seu texto muito longo aqui..."
compressed_data = semantic_compressor(long_text, top_n_keywords=10, summary_sentences=5)
print(f"Palavras-chave: {compressed_data['keywords']}")
print(f"Resumo: {compressed_data['summary']}")
```

### 2. `recursive_orchestrator.py`

**Função**: `orchestrate_task(task_description, max_depth=2, current_depth=0)`

**Descrição**: Simula a quebra de uma tarefa complexa em sub-tarefas. Embora a implementação atual seja uma simulação, a lógica pode ser estendida para integrar chamadas reais ao Manus para cada sub-tarefa, permitindo a execução de projetos ambiciosos.

**Exemplo de Uso (no seu ambiente Python)**:

```python
from scripts.recursive_orchestrator import orchestrate_task
import json

complex_project = "Desenvolver um aplicativo de gerenciamento de projetos com IA"
orchestration_plan = orchestrate_task(complex_project, max_depth=3)
print(json.dumps(orchestration_plan, indent=2, ensure_ascii=False))
```

### 3. `structured_output_refiner.py`

**Funções**: 
- `refine_json_output(json_string)`
- `validate_and_clean_text(text, allowed_chars=None)`

**Descrição**: Garante que as saídas do Manus (ou de outras fontes) estejam no formato esperado e limpas. `refine_json_output` tenta corrigir JSONs malformados, e `validate_and_clean_text` remove caracteres indesejados e espaços extras.

**Exemplo de Uso (no seu ambiente Python)**:

```python
from scripts.structured_output_refiner import refine_json_output, validate_and_clean_text

malformed_json_str = "{\'item\': \'valor\'}"
cleaned_json = refine_json_output(malformed_json_str)
print(f"JSON Refinado: {cleaned_json}")

dirty_input = "Texto com !@# caracteres e   espaços extras."
clean_text = validate_and_clean_text(dirty_input)
print(f"Texto Limpo: {clean_text}")
```

## 💡 Filosofia

Estas ferramentas são projetadas para serem usadas em conjunto com o Manus, agindo como uma camada de pré-processamento e pós-processamento. Elas permitem que o Manus se concentre em sua inteligência central, enquanto as tarefas repetitivas ou de formatação são delegadas a scripts eficientes, maximizando a "cognição" total do sistema. Pense nelas como o "oxigênio" que permite ao Manus operar em altitudes mais elevadas de complexidade e eficiência.
