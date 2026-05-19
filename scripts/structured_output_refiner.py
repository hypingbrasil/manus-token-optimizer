import json

def refine_json_output(json_string):
    """
    Tenta carregar uma string como JSON e retorna o JSON formatado.
    Se falhar, tenta corrigir problemas comuns (ex: aspas simples para duplas).
    """
    try:
        data = json.loads(json_string)
        return json.dumps(data, indent=2, ensure_ascii=False)
    except json.JSONDecodeError as e:
        print(f"Erro de JSONDecodeError: {e}. Tentando correção...")
        # Tentativa de correção: substituir aspas simples por duplas
        corrected_json_string = json_string.replace("\\'", "\"")
        try:
            data = json.loads(corrected_json_string)
            return json.dumps(data, indent=2, ensure_ascii=False)
        except json.JSONDecodeError as e_corrected:
            return f"Falha ao refinar JSON: {e_corrected}"

def validate_and_clean_text(text, allowed_chars=None):
    """
    Valida e limpa um texto, removendo caracteres não permitidos ou espaços extras.
    """
    if allowed_chars is None:
        # Exemplo: permitir letras, números, espaços e pontuação básica
        allowed_chars = r"[a-zA-Z0-9áéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕçÇ.,!?;:()\s-]"
    
    cleaned_text = "".join(re.findall(allowed_chars, text))
    cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip() # Remover múltiplos espaços
    return cleaned_text

if __name__ == "__main__":
    # Exemplo de refinamento JSON
    malformed_json = "{\'nome\': \'Manus\', \'funcao\': \'IA\', \'versao\': 1.0}"
    refined = refine_json_output(malformed_json)
    print("--- Refinador de Saída Estruturada (JSON) ---")
    print(refined)

    valid_json = "{\"item\": \"caneta\", \"quantidade\": 10}"
    refined_valid = refine_json_output(valid_json)
    print("\n--- Refinador de Saída Estruturada (JSON Válido) ---")
    print(refined_valid)

    # Exemplo de validação e limpeza de texto
    dirty_text = "  Este é um texto com   muitos  espaços e caracteres especiais! @#$ %^&* "
    cleaned = validate_and_clean_text(dirty_text)
    print("\n--- Refinador de Saída Estruturada (Texto) ---")
    print(f"Texto Sujo: 
\""" {dirty_text} ""\"")
    print(f"Texto Limpo: 
\""" {cleaned} ""\"")

    custom_allowed_chars = r"[a-zA-Z0-9\s]" # Apenas letras e números
    cleaned_custom = validate_and_clean_text(dirty_text, allowed_chars=custom_allowed_chars)
    print(f"Texto Limpo (Custom): 
\""" {cleaned_custom} ""\"")
