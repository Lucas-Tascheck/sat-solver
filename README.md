# SAT solver
Este projeto implementa um resolvedor SAT (Satisfiability Problem) utilizando o algoritmo DPLL (Davis-Putnam-Logemann-Loveland). O resolvedor lê fórmulas em formato CNF (Conjunctive Normal Form) a partir de arquivos de texto e determina se as fórmulas são satisfazíveis ou não, produzindo um arquivo de saída com as atribuições das variáveis.
## Uso

1. **Prepare o Arquivo CNF**: Crie ou edite um arquivo com a extensão `.cnf` seguindo o formato DIMACS.

2. **Execute o Código**: Execute o script Python passando o diretório do arquivo `.cnf` como argumento :

   ```bash
   python3 sat_solver.py /diretorio/para/arquivo.cnf
   ```

3. **Verifique o Resultado**: Após a execução, um arquivo com a extensão `.res` será gerado com o mesmo nome do arquivo de entrada. O arquivo de saída conterá:

   - A primeira linha será `SAT` se a fórmula for satisfazível, ou `UNSAT` se não for.
   - Se a fórmula for satisfazível, a segunda linha terá a valoração das variáveis, terminando com `0`.

   Exemplo de saída:

   ```
   SAT
   1 -2 3 -4 5 0
   ```