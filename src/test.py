from sympy import symbols
from sympy.logic.boolalg import Not, And, Or, Implies, Equivalent

# Define the symbols
p, q, r = symbols('p q r')

# Statement A expressions
expr1 = Not(Or(p, And(Not(p), q)))
expr2 = And(Not(p), Not(q))

# Check if Statement A expressions are equivalent
equiv_A = Equivalent(expr1, expr2)

# Statement B is a tautology
exprB = Implies(And(p, q), Or(p, q))

# Statement C expressions are not equivalent by definition
# But we can still check the equivalence for the sake of the exercise
exprC1 = Implies(Implies(p, q), r)
exprC2 = Implies(p, Implies(q, r))

# Check if Statement C expressions are equivalent
equiv_C = Equivalent(exprC1, exprC2)

# Calculate the results
equivalence_A = equiv_A.simplify()
tautology_B = exprB.simplify()
equivalence_C = equiv_C.simplify()

(equivalence_A, tautology_B, equivalence_C)
