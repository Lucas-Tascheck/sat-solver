# Resolutor SAT usando DPLL

Este projeto implementa um resolvedor SAT (Satisfiability Problem) utilizando o algoritmo DPLL (Davis-Putnam-Logemann-Loveland). O resolvedor lê fórmulas em formato CNF (Conjunctive Normal Form) a partir de arquivos de texto e determina se as fórmulas são satisfazíveis ou não, produzindo um arquivo de saída com as atribuições das variáveis.

## Requisitos

- Python 3.x
- Nenhuma biblioteca externa é necessária.

## Estrutura do Projeto

```
/resolutor_sat
│
├── resolutor.py       # Código-fonte do resolvedor SAT
├── formula.cnf       # Exemplo de arquivo CNF (substitua com seu próprio arquivo)
└── README.md          # Este arquivo
```

## Formato do Arquivo CNF

Os arquivos CNF devem seguir o formato DIMACS. Aqui está um exemplo de como um arquivo CNF deve ser estruturado:

```
c Exemplo de arquivo no formato CNF
c Mais uma linha de comentário
p cnf 5 3
1 -5 -4 0
-1 5 3 4 0
-3 -4 0
```

- A linha que começa com `p` define o número de variáveis e cláusulas.
- Cada cláusula é uma linha com literais separados por espaço, terminando com `0`.
- Literais positivos representam variáveis e literais negativos representam suas negações.

## Uso

1. **Prepare o Arquivo CNF**: Crie ou edite um arquivo com a extensão `.cnf` seguindo o formato DIMACS.

2. **Execute o Código**: Execute o script Python:

   ```bash
   python resolutor.py
   ```

3. **Verifique o Resultado**: Após a execução, um arquivo com a extensão `.res` será gerado com o mesmo nome do arquivo de entrada. O arquivo de saída conterá:

   - A primeira linha será `SAT` se a fórmula for satisfazível, ou `UNSAT` se não for.
   - Se a fórmula for satisfazível, a segunda linha terá a valoração das variáveis, terminando com `0`.

   Exemplo de saída:

   ```
   SAT
   1 -2 3 -4 5 0
   ```

## Exemplo de Execução

1. Crie um arquivo chamado `formula.cnf` com o seguinte conteúdo:

   ```
   c Exemplo de arquivo no formato CNF
   p cnf 5 3
   1 -5 -4 0
   -1 5 3 4 0
   -3 -4 0
   ```

2. Execute o script:

   ```bash
   python resolutor.py
   ```

3. Verifique o arquivo de saída `formula.res`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Você pode fazer isso enviando um pull request ou abrindo um problema.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Sinta-se à vontade para personalizar este README conforme necessário ou adicionar mais informações específicas sobre seu projeto!