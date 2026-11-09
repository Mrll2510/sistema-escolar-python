# Sistema Escolar em Python

Projeto de estudos desenvolvido em Python para praticar lógica de programação, programação orientada a objetos (POO), listas, validação de dados e integração com uma API de IA.

## Funcionalidades

- Cadastro, remoção e listagem de alunos
- Armazenamento dos dados dos alunos em objetos da classe `Aluno`
- Validação de notas e identificação de turma
- Menu interativo
- Chatbot integrado à API da Groq, capaz de responder perguntas usando os dados dos alunos cadastrados

## Tecnologias

- Python
- Programação orientada a objetos (POO)
- SDK da OpenAI, configurado para usar a API compatível da Groq
- Google Colab para execução e armazenamento seguro da chave

## Como configurar

1. Abra o projeto no Google Colab.
2. Instale a dependência:

   ```bash
   pip install openai
   ```

3. Crie uma chave de API na Groq.
4. No Google Colab, abra **Secrets** e salve a chave com o nome `GROQ_API_KEY`.
5. Habilite o acesso ao segredo no notebook.
6. Execute as células do projeto.

O código busca a chave com `userdata.get("GROQ_API_KEY")`.

## Observações

- Os dados dos alunos ficam em memória durante a execução; eles não são salvos permanentemente.
- Este é um projeto educacional. O sistema de login e o armazenamento atual não devem ser usados para proteger dados reais.
- Use apenas dados fictícios nos testes do chatbot. Evite enviar informações pessoais ou notas de alunos reais para serviços externos.

## Status

Projeto em desenvolvimento.
