# SAT 布林滿足問題求解

我用 gemini, 對話網址 -- https://share.gemini.google/XyuiIAMivN4r


* [sat_solver.py](./sat_solver.py)

執行結果

```sh
(.venv) ccc@teacherdeiMac week3 % ./test.sh
==========================================
          SAT Solver 測試套件
==========================================
[PASS] Test #1
       算式: A
       輸出: SAT {'A': True}
------------------------------------------
[PASS] Test #2
       算式: not A
       輸出: SAT {'A': False}
------------------------------------------
[PASS] Test #3
       算式: A and not A
       輸出: UNSAT
------------------------------------------
[PASS] Test #4
       算式: A or not A
       輸出: SAT {'A': True}
------------------------------------------
[PASS] Test #5
       算式: (A or B) and (not A or C) and (not B or not C)
       輸出: SAT {'A': True, 'B': False, 'C': True}
------------------------------------------
[PASS] Test #6
       算式: (A or B) and (not A) and (not B)
       輸出: UNSAT
------------------------------------------
[PASS] Test #7
       算式: (A and B) or (not A and not B)
       輸出: SAT {'A': True, 'B': True}
------------------------------------------
[PASS] Test #8
       算式: not (A and B) == (not A or not B)
       輸出: SAT {'A': True, 'B': True}
------------------------------------------
[PASS] Test #9
       算式: (A or B or C) and (not A or not B) and (not B or not C) and (not C or not A)
       輸出: SAT {'A': True, 'B': False, 'C': False}
------------------------------------------
[PASS] Test #10
       算式: (A or B) and (B or C) and (C or A) and (not A or not B) and (not B or not C) and (not C or not A)
       輸出: UNSAT
------------------------------------------
[PASS] Test #11
       算式: (A and B and C) and (not A or not B or not C)
       輸出: UNSAT
------------------------------------------
[PASS] Test #12
       算式: (P or Q or R) and (not P or Q) and (not Q or R) and (not R or P) and (not P or not Q or not R)
       輸出: UNSAT
------------------------------------------
[PASS] Test #13
       算式: (W or X) and (Y or Z) and (not W or not Y) and (not X or not Z)
       輸出: SAT {'W': True, 'X': False, 'Y': False, 'Z': True}
------------------------------------------
測試完成: 通過 13 / 13 個案例。
```

應該要自己說明（不靠 AI) 理解的程度，解釋程式運作的原理
