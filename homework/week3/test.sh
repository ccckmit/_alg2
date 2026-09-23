#!/usr/bin/env bash

# 確保 sat_solver.py 存在
if [ ! -f "sat_solver.py" ]; then
    echo "錯誤: 找不到 sat_solver.py"
    exit 1
fi

echo "=========================================="
echo "          SAT Solver 測試套件"
echo "=========================================="

# 測試案例陣列: "表達式|預期結果"
tests=(
    "A|SAT"
    "not A|SAT"
    "A and not A|UNSAT"
    "A or not A|SAT"
    "(A or B) and (not A or C) and (not B or not C)|SAT"
    "(A or B) and (not A) and (not B)|UNSAT"
    "(A and B) or (not A and not B)|SAT"
    "not (A and B) == (not A or not B)|SAT"
    "(A or B or C) and (not A or not B) and (not B or not C) and (not C or not A)|SAT"
    "(A or B) and (B or C) and (C or A) and (not A or not B) and (not B or not C) and (not C or not A)|UNSAT"
    "(A and B and C) and (not A or not B or not C)|UNSAT"
    "(P or Q or R) and (not P or Q) and (not Q or R) and (not R or P) and (not P or not Q or not R)|UNSAT"
    "(W or X) and (Y or Z) and (not W or not Y) and (not X or not Z)|SAT"
)

pass_count=0
fail_count=0
total=${#tests[@]}

for i in "${!tests[@]}"; do
    case_num=$((i + 1))
    IFS='|' read -r expr expected <<< "${tests[i]}"

    # 執行 Python 程式並取得輸出
    output=$(python3 sat_solver.py "$expr")
    
    # 解析結果是 SAT 還是 UNSAT
    if [[ "$output" == SAT* ]]; then
        actual="SAT"
    else
        actual="UNSAT"
    fi

    # 比對結果
    if [ "$actual" == "$expected" ]; then
        echo -e "[\033[32mPASS\033[0m] Test #$case_num"
        echo "       算式: $expr"
        echo "       輸出: $output"
        ((pass_count++))
    else
        echo -e "[\033[31mFAIL\033[0m] Test #$case_num"
        echo "       算式: $expr"
        echo "       預期: $expected, 實際: $output"
        ((fail_count++))
    fi
    echo "------------------------------------------"
done

echo "測試完成: 通過 $pass_count / $total 個案例。"

if [ $fail_count -gt 0 ]; then
    exit 1
fi