# 🔢 Gerador de CPF em Python

Este projeto é um **gerador de CPF válido**, desenvolvido em **Python**, que cria números de CPF seguindo corretamente o **cálculo oficial dos dígitos verificadores**, além de exibir o CPF já **formatado no padrão brasileiro**.

Projeto ideal para fins **educacionais**, testes de sistemas e estudos de lógica de programação.

---

## 🚀 Funcionalidades

- Geração automática dos **9 dígitos base** do CPF  
- Cálculo correto do **1º e 2º dígitos verificadores**  
- Validação matemática do CPF gerado  
- Formatação no padrão: `XXX.XXX.XXX-XX`  
- Execução simples via terminal  

---

## 🧠 Como funciona

1. Gera aleatoriamente os 9 primeiros dígitos do CPF  
2. Calcula o primeiro dígito verificador com peso decrescente  
3. Calcula o segundo dígito verificador com base no CPF parcial  
4. Retorna um CPF **válido e formatado**

---

## 🧩 Código principal

O projeto utiliza funções bem definidas para manter o código organizado:

- `gerar_cpf_base()` → gera os 9 dígitos iniciais  
- `calculo_digito()` → calcula os dígitos verificadores  
- `gerar_cpf()` → monta o CPF completo  
- `formatar_cpf()` → aplica a máscara padrão  

---

## ▶️ Como executar

### Pré-requisitos
- Python 3.x instalado

### Passos
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/nome-do-repositorio.git

# Acesse a pasta do projeto
cd nome-do-repositorio

# Execute o script
python nome_do_arquivo.py
```

📌 Exemplo de saída
```bash
123.456.789-09
CPF válido
```

## ⚠️ Aviso legal

Este projeto foi criado apenas para fins educacionais e testes de software.

CPFs gerados não devem ser utilizados para fins ilegais ou fraudulentos.

---

## 📈 Possíveis melhorias futuras

- 🔍 Função para validar CPFs informados pelo usuário
- 🧪 Testes automatizados
- 🖥️ Interface gráfica (GUI)
- 🌐 Versão web

---

## 🛠️ Tecnologias utilizadas

- Python  
- Biblioteca padrão (`random`, `os`)

---

## 📜 Licença

Este projeto pode ser distribuído sob a licença MIT.

Sinta-se à vontade para estudar, modificar e melhorar o código.

---

## 👨‍💻 Autor

Desenvolvido por **Gilvane Maule**

📌 Formado em Análise e Desenvolvimento de Sistemas  
📌 Cursando Pós-Graduação em IA e Ciência de Dados
