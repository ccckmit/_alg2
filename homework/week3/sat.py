def parse_clause(clause_str):
    """
    將文字變數表示（例如 'A', '~B'）解析為 CNF 的單個 Clause（子句）。
    正項存入 set，負項去掉 ~ 後存入 set。
    """
    clause = set()
    for literal in clause_str.split():
        clause.add(literal)
    return clause


def dpll(clauses, assignment):
    """
    DPLL 演算法主體
    :param clauses: list of set，即 CNF（合取範式）邏輯運算式
    :param assignment: dict，紀錄變數目前的 True/False 賦值
    :return: (bool, dict) - 是否可滿足，以及變數對應的 True/False 賦值
    """
    # 1. 如果子句集合為空，代表所有子句皆已被滿足 -> 可滿足 (SAT)
    if not clauses:
        return True, assignment

    # 2. 如果存在空子句 set()，代表當前賦值產生矛盾 -> 不可滿足 (UNSAT)
    if any(len(clause) == 0 for clause in clauses):
        return False, {}

    # 3. 單子句消元 (Unit Propagation)
    # 如果某個子句只剩一個 Literal，該 Literal 的值被強制確定
    for clause in clauses:
        if len(clause) == 1:
            unit = next(iter(clause))
            var = unit.lstrip('~')
            val = not unit.startswith('~')

            # 簡化 CNF 邏輯表達式
            new_clauses = simplify(clauses, var, val)
            new_assignment = assignment.copy()
            new_assignment[var] = val
            return dpll(new_clauses, new_assignment)

    # 4. 純文字消元 (Pure Literal Elimination)
    # 如果某個變數在所有子句中只以正項或負項單一型態出現
    all_literals = set().union(*clauses)
    for lit in all_literals:
        var = lit.lstrip('~')
        neg_lit = f"~{var}" if not lit.startswith('~') else var
        
        # 檢查 negated literal 是否不存在於所有子句中
        if neg_lit not in all_literals:
            val = not lit.startswith('~')
            new_clauses = simplify(clauses, var, val)
            new_assignment = assignment.copy()
            new_assignment[var] = val
            return dpll(new_clauses, new_assignment)

    # 5. 分支選擇與回溯 (Splitting / Backtracking)
    # 挑選第一個尚未確定的變數進行嘗試
    chosen_var = list(all_literals)[0].lstrip('~')

    # 嘗試 賦值為 True
    solvable, res_assignment = dpll(simplify(clauses, chosen_var, True), {**assignment, chosen_var: True})
    if solvable:
        return True, res_assignment

    # 若 True 失敗，回溯嘗試 賦值為 False
    return dpll(simplify(clauses, chosen_var, False), {**assignment, chosen_var: False})


def simplify(clauses, var, val):
    """
    根據變數 var = val 簡化 clauses：
    1. 包含被滿足 Literal 的子句直接移除
    2. 包含相反 Literal 的項從子句中刪除
    """
    true_lit = var if val else f"~{var}"
    false_lit = f"~{var}" if val else var

    new_clauses = []
    for clause in clauses:
        # 如果該子句已被滿足，直接忽略該子句
        if true_lit in clause:
            continue
        # 如果子句包含不滿足的 Literal，移除該 Literal
        new_clause = clause - {false_lit}
        new_clauses.append(new_clause)

    return new_clauses


# ==================== 測試範例 ====================
if __name__ == "__main__":
    # 邏輯表達式以 CNF (合取範式) 格式呈現
    # 範例 1: (A or B) and (~A or C) and (~B or ~C)
    cnf_formula_1 = [
        parse_clause("A B"),
        parse_clause("~A C"),
        parse_clause("~B ~C")
    ]

    print("--- 測試 1 : (A or B) and (~A or C) and (~B or ~C) ---")
    satisfiable, assignment = dpll(cnf_formula_1, {})
    if satisfiable:
        print("結果: SAT (可滿足)")
        print("變數賦值:", assignment)
    else:
        print("結果: UNSAT (不可滿足)")

    # 範例 2: 必定衝突的邏輯 (A) and (~A)
    cnf_formula_2 = [
        parse_clause("A"),
        parse_clause("~A")
    ]

    print("\n--- 測試 2 : (A) and (~A) ---")
    satisfiable, assignment = dpll(cnf_formula_2, {})
    if satisfiable:
        print("結果: SAT (可滿足)")
        print("變數賦值:", assignment)
    else:
        print("結果: UNSAT (不可滿足)")