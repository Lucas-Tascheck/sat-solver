def parse_cnf_file(filepath):
    clauses = []
    num_variables = 0
    num_clauses = 0

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('c'):  # Ignorar linhas de comentários
                continue
            if line.startswith('p'):  # Linha de problema
                _, _, num_variables, num_clauses = line.split()
                num_variables = int(num_variables)
                num_clauses = int(num_clauses)
            else:  # Linhas das cláusulas
                clause = [int(x) for x in line.split() if int(x) != 0]
                if clause:
                    clauses.append(clause)
    return num_variables, num_clauses, clauses


def is_clause_satisfied(clause, assignment):
    for literal in clause:
        var = abs(literal)
        if var in assignment:
            if literal > 0 and assignment[var]:
                return True
            if literal < 0 and not assignment[var]:
                return True
    return False


def is_formula_satisfied(clauses, assignment):
    return all(is_clause_satisfied(clause, assignment) for clause in clauses)


def dpll(clauses, assignment):
    if is_formula_satisfied(clauses, assignment):
        return True

    for clause in clauses:
        if all(abs(literal) in assignment and
               ((literal > 0 and not assignment[abs(literal)]) or (literal < 0 and assignment[abs(literal)]))
               for literal in clause):
            return False

    unassigned_vars = {abs(literal) for clause in clauses for literal in clause if abs(literal) not in assignment}

    if not unassigned_vars:
        return False

    variable = unassigned_vars.pop()

    assignment[variable] = True
    if dpll(clauses, assignment):
        return True

    assignment[variable] = False
    if dpll(clauses, assignment):
        return True

    del assignment[variable]
    return False


def solve_cnf(filepath):
    num_variables, num_clauses, clauses = parse_cnf_file(filepath)

    assignment = {}
    satisfiable = dpll(clauses, assignment)

    if satisfiable:
        for var in range(1, num_variables + 1):
            if var not in assignment:
                assignment[var] = False
        return assignment
    else:
        return None


def write_output(filepath, assignments):
    output_filepath = filepath.replace('.cnf', '.res')
    with open(output_filepath, 'w') as output_file:
        if assignments is not None:
            output_file.write("SAT\n")
            output_file.write(" ".join(str(var if assignments[var] else -var) for var in range(1, len(assignments) + 1)) + " 0\n")
        else:
            output_file.write("UNSAT\n")


if __name__ == "__main__":
    filepath = "formula.cnf"  # Especificar o caminho do arquivo .cnf

    result = solve_cnf(filepath)
    write_output(filepath, result)
