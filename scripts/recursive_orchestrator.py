import json

def orchestrate_task(task_description, max_depth=2, current_depth=0):
    """
    Simula a orquestração de uma tarefa complexa, dividindo-a em sub-tarefas.
    Para fins de demonstração, as sub-tarefas são geradas de forma simplificada.
    """
    if current_depth >= max_depth:
        return {"task": task_description, "status": "executado", "detail": "Tarefa atômica finalizada."}

    print(f"{'  ' * current_depth}Orquestrando: {task_description}")
    sub_tasks = [
        f"Sub-tarefa A de '{task_description}'",
        f"Sub-tarefa B de '{task_description}'"
    ]

    results = []
    for sub_task in sub_tasks:
        results.append(orchestrate_task(sub_task, max_depth, current_depth + 1))
    
    return {
        "task": task_description,
        "status": "concluído",
        "sub_task_results": results
    }

if __name__ == "__main__":
    complex_task = "Desenvolver um sistema de recomendação de produtos"
    orchestration_result = orchestrate_task(complex_task, max_depth=3)
    print("\n--- Orquestrador de Tarefas Recursivas ---")
    print(json.dumps(orchestration_result, indent=2, ensure_ascii=False))

    another_task = "Escrever um relatório de mercado"
    orchestration_result_simple = orchestrate_task(another_task, max_depth=2)
    print("\n--- Orquestrador de Tarefas Recursivas (Simples) ---")
    print(json.dumps(orchestration_result_simple, indent=2, ensure_ascii=False))
