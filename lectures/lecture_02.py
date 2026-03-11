from execute_util import link, image, text

def main():
    text("# FORE20067：面向语言信息处理的语言逻辑理论 \n## Natural Language Logic and Natural Language Processing")
    image("images/stuff.png", width=600)

    set_theory()
    relations_and_functions()
    propositional_logic()
    Q_and_A()

def set_theory():
    text("**1. Set Theory**")
    text("**1.1 Definitions of Some Concepts**")

    text("**set**: a set is an abstract collection of distinct objects.")
    text("**members/elements**: distinct objects")
    text("- examples: {2,7,10} this is a set.")
    text("- the number 2, the number 7 and the number 10 are the members of the sets.")
    text("- 2 ∈ {2,7,10}   '2 is a number of the set containing 2, 7 and 10.'")
    text("- 3 ∉ {2,7,10}   '3 is not an element of the set containing 2, 7 and 10.'")

    text("**singleton**: a set has only one member {3}")
    text("**empty set**: {}/∅")

    text("**cardinality**: the cardinality of a set is the number of elements it contains.")
    text("- |{2,7,10}| = 3   'the cardinality of the set containing 2, 7, and 10 is 3'")

    text("**predicate notation / set-builder notation**:")
    text("- we use it to describe the set of things meeting a certain condition.")
    text("- {n | n ∈ ℤ and n < 0}")
    text("- 'the set of all n such that n is an integer and n is less than 0'")
    text("- variable + vertical bar + a description containing the variable")

    text("**subset**: ")
    text("- a set A is a subset of a set B if and only if every member of A (if any) is a member of B.")
    text("- A ⊆ B iff for all x: if x ∈ A then x ∈ B")

    text("**proper subset**: ")
    text("- A is a proper subset of B, written A ⊂ B, if and only if A is a subset of B and A is not equal to B.")
    text("- A ⊂ B iff (i) for all x: if x ∈ A then x ∈ B and (ii) A ≠ B")

    text("**powerset**: ")
    text("- the set of all the subsets of a given set.")
    text("- ℘({a,b}) = {{}, {a}, {b}, {a,b}}")

    text("**superset**: ")
    text("- A is a superset of B, written A ⊇ B, if and only if every member of B is a member of A.")
    text("- A ⊇ B iff for all x: if x ∈ B then x ∈ A")

    text("**proper superset**: ")
    text("- A is a proper superset of B, written A ⊃ B, if and only if A is a superset of B and A is not equal to B.")
    text("- A ⊃ B iff (i) for all x: if x ∈ B then x ∈ A and (ii) A ≠ B")

    text("**intersection**: ")
    text("- the intersection of A and B, written A ∩ B, is the set of all entities x that are both a member of A and a member of B.")
    text("- A ∩ B = {x | x ∈ A and x ∈ B}")

    text("**Euler Diagram**")
    text("**[and/some]** John is a lawyer and a doctor. / Some lawyers are doctors.")
    text("intersection between the set of lawyers and the set of doctors")

    image("images/euler_diagram1.png", width=400)
    text("- **[no]** No musicians snores.")
    text("- disjoint: the intersection is empty")

    image("images/euler_diagram2.png", width=450)
    text("- **[or]** John is a lawyer or a doctor.")
    text("- The union of A and B.")

    text("**Subtracting / Difference of A and B / Relative Complement of A and B**")
    text("- A−B / A \\ B: the set of all things that are in A but not in B.")
    text("- A−B = {x | x ∈ A and x ∉ B}")
    image("images/subtracting.png", width=400)

def relations_and_functions():
    text("**2. Relations and Functions**")
    text("**2.1 Some Basic Concepts**")

    text("**The denotation of common nouns / intransitive verbs:**")
    text("- ⟦cellist⟧ = the set of cellists")
    text("- ⟦snores⟧ = the set of individuals who snore")

    text("**The denotation of transitive verbs:**")
    text("- ⟦admire / love / respect⟧ = relations between two individuals (using ordered pairs)")

    text("**Ordered Pairs**")
    text("some features:")
    text("1) the elements of an ordered pair are ordered. Using angle brackets, we write <a,b> to designate the ordered pair in which a is the first member and b is the second member. Thus <a,b> ≠ <b,a>")
    text("2) the members of an ordered pair can be anything (numbers / sets / ordered pairs)")
    text("3) Cartesian Product of A and B, written A × B. For example: {a,b,c} × {1,2,3} = {<a,1>,<a,2>,<a,3>,<b,1>,<b,2>,<b,3>,<c,1>,<c,2>,<c,3>}")
    text("---")
    text("**2.2 Relations**")
    text("the semantics of **transitive verbs** like *love* / *admire* / *respect*")
    text("the semantics of **certain nouns** like *neighbor* / *mother* / *friend* (relations between individuals)")
    text("the semantics of **prepositions** like *in* / *beside*")
    text("types of relations: binary relations / ternary relations / quaternary relations")
    text("the relation from A to B is a set of ordered pairs whose first member is an element of A and whose second member is an element of B. Not all elements of A and B need necessarily be involved in the relation.")

    text("**different types of relations**")
    text("**reflexive**: a reflexive relation is one that relates everything to itself, that is, for any x, the pair <x,x> is in the relation.")
    text("**symmetric**: a relation is symmetric if and only if: for any a and b, if <a,b> is in the relation, then <b,a> is also in the relation.")
    text("- Paul is standing next to George.")
    text("- ∴ George is standing next to Paul.")
    text("**transitive**: a transitive relation is one that licenses inferences like this:")
    text("- Paul is taller than George.")
    text("- George is taller than Ringo.")
    text("- ∴ Paul is taller than Ringo.")
    text("**equivalence relation**: a relation that is **reflexive**, **symmetric**, and **transitive**.")
    text("---")
    text("**2.3 Functions**")
    text("a function is a special type of relation (like a vending machine)")
    text("\t input (arguments):")
    text("a specification of which item you would like to buy")
    text("\t output (values):")
    text("a particular bag of chocolate-covered raisins")

    text("an example of function is a relation that maps a person to their height in feet and inches")
    image("images/example_of_relation.png", width=240)


    text("**Features:**")
    text("- every function is a relation (by definition), but not every relation is a function.")
    text("- A relation from A to B is a function only if every element of A is mapped to one and only one member of B.")
    image("images/features_of_relation1.png", width=400)
    image("images/features_of_relation2.png", width=400)

    text("**Characteristic Function**")
    text("- a set A: a function that takes an entity and returns 1 (True) if that entity is a member of A and 0 (False) otherwise.")
    image("images/characteristic_function.png", width=240)
    text("- the set of ABBA band members is {Agnetha, Björn, Benny, Frida}. this is the domain.")
    text("- the characteristic function of the set {Agnetha, Frida} is a function that takes input an ABBA member")
    text("- and returns 1 (True) if the input is a member of this set and 0 if not.")

def propositional_logic():
    text("**1. Basic Concepts**")
    text("**1.1 Logic**")

    text("**Definition**")
    text("- A formal language that is equipped with a notion of entailment, and a way to determine when that notion applies, is called a LOGIC.")

    text("**Propositional Logic**")
    text("Also called SENTENTIAL LOGIC")
    text("In propositional logic, **placeholders** (占位符 / 变量) stand for entire clauses or sentences:")
    text("\t If it rained last night, then the lawn is wet.\n\t It rained last night.\n\t ∴ The lawn is wet.")

    text("**1.2 L<sub>Prop</sub> (Propositional Language)**")
    text("- “the specific propositional language we are building up.”")
    text("- L<sub>Prop</sub> refers to the formal language used to describe propositional logic.")
    text("- It includes **a set of symbols** (*propositional letters, logical connectives*)")
    text("- and **syntactical rules** for constructing logical expressions and formulas.")

    text("**1.3 Propositional Letters (or Propositional Variables)**")
    text("**Definition**")
    text("- A propositional letter is a **symbol** that represents roughly the kind of thing that is expressed by **a simple declarative clause or sentence** that **does not contain any of the words *and*, *or*, *not*, *if*, *then***.")

    text("**p, q, and r are propositional letters.**")
    text("- In principle, any set of symbols can be used as propositional letters.")
    text("- When more letters are needed, it is customary to use primes as in p, p′, p′′, etc.")

    text("**1.4 Formula**")
    text("**Definition**")
    text("- The counterpart in logic of a grammatical sentence is called a FORMULA or WFF (well-formed formula).")
    text("**L<sub>Prop</sub> V.S. Formula**")
    text("- **L<sub>Prop</sub>** is an *abstract language system* that specifies the symbols")
    text("- (such as propositional variables and logical connectives)")
    text("- and how these symbols can be legally combined.")
    text("- **Formula** is a *specific logical expression* constructed according to")
    text("- the symbols and rules of L<sub>Prop</sub>.")

    text("**The Structure of Formula**")
    text("Formulas in propositional logic may be built up from smaller formulas")
    text("with **syntactic rules** (*rules of formation*) and **semantic rules**.")
    text("**Syntactic Rules**")
    text("- Specify how to build formulas.")
    text("- **Atomic Formula:** Propositional letters: p, q, r.(Any propositional letter is a formula.)" )
    text("- **Complex Formula**: Formulas with connectives.")
    text("**Semantic Rules**")
    text("- Specify how to interpret them (how to map them to T or F).")
    text("- **The Denotation of a Formula: Truth Value**")
    text("- In order to know if a formula is true or false, we need to map the formula with truth values.")
    text("- Thus we have *Interpretation Functions* and *Denotation Functions*.")
    text("- **Compositionality**: Assign denotations to larger formulas in ways that depend only on the denotations of the smaller formulas.")

    text("**Interpretation Function (or just 'Interpretation')**")
    text("- An interpretation function for a given propositional language is a function that *maps each propositional letter of that language to a truth value*.")
    image("images/interpretation_function.png", width=400)

    text("------------------------------------------------")

    text("**Boolean Connectives**")
    text("Formulas in propositional logic can be combined and assembled into larger formulas using **logical connectives**.")

    text("**2.1 Unary Connective**")
    text("Negation (¬) : '¬p'")
    text("- Read as 'not p' or 'it is not the case that p'")
    text("- Sometimes written as '~'")
    text("- If φ is a formula, then ¬φ is also a formula.")
    text("- (This is called the negation of φ.)")
    text("- Truth Table:")
    image("images/negation_truth_table.png", width=160)

    text("**2.2 Binary Connectives**")
    text("**Conjunction (∧): [p ∧ q]**")
    text("- Can be read 'p **AND** q'")
    text("- Sometimes written as '&'")
    text("- It is a CONJUNCTION in which p and q are the two CONJUNCTS.")
    text("- If φ and ψ are formulas, then [φ ∧ ψ] is also a formula.")
    text("- Truth Table:")
    image("images/conjunction_truth_table.png", width=160)
    image("images/conjunction.png", width=400)

    text("**Disjunction (∨): [p ∨ q]**")
    text("- Can be read 'p **OR** q'")
    text("- Sometimes written as '|'")
    text("- It is a DISJUNCTION in which p and q are the two DISJUNCTS.")
    text("- If φ and ψ are formulas, then [φ ∨ ψ] is also a formula.")
    text("- Truth Table:")
    image("images/disjunction_truth_table.png", width=160)
    image("images/disjunction.png", width=400)

    text("**Exclusive Disjunction (XOR, for eXclusive OR): [p XOR q]**")
    text("- **“∨” is actually Inclusive Disjunction.**")
    text("- Example: *Susan volunteers on Monday or Wednesday (14)*.")
    text("- Inclusive interpretation: The sentence **is still true if she volunteers on both days**.")
    text("- Exclusive interpretation: specifies that **only one of the disjuncts is true**.")
    text("- *Susan volunteers on Monday or Wednesday, but not both.*")
    text("- Truth Table:")
    image("images/xor_truth_table.png", width=160)

    text("------------------------------------------------")

    text("**2.3 Truth Value Computation**")

    text("Truth tables can be used to compute the truth values for arbitrarily complex formulas using these connectives:.")
    image("images/truth_value_computation.png", width=200)

    text("**Premises and Principles**")
    text("Ⅰ: ∧, ∨, and ¬ are **Truth-Functional**.")
    text("- The truth value of a complex expression that is produced by combining one of these connectives with the appropriate number of formulas **depends solely on the truth values of the connectives**.")
    text("ⅠⅠ: **Logical Consequence View**")
    text("- **The logical consequence view** corresponds to specific ways to fill in placeholders in an argument form.")
    text("- **The necessary consequence view** corresponds to specific possible world. (The two perspectives are equivalent only when the intrinsic meanings of propositional letters are independent.)")

    text("Example:")
    text("\t p: Tomorrow is Tuesday.\n\t q: Today is Tuesday.")
    text("↑↑↑Even though 'p ∧ q' cannot both be true in any possible world, we still list it in the truth table.")
    text("**Therefore the consequence here is logical consequence.**")

    text("ⅠⅠⅠ: **Brackets and Scopes**")
    text("The SCOPE of a connective in a formula is the part of the formula that stands in for the meta-variable(s) in its syntactic rule.")
    text("Example:")
    text("[[p ∧ q] ∨ r]  is not equivalent to  [p ∧ [q ∨ r]]")

    text("------------------------------------------------")

    text("**Applications:**")

    text("**Help define Equivalence**")
    text("When A and B have the same truth values in every case,")
    text("we say they are Equivalent.")
    text("Example:")
    text("¬[p ∧ q]  ≡  [¬p ∨ ¬q]")
    image("images/equivalence.png", width=300)

    text("**Help prove Entailment**")
    text("Definition:")
    text("A entails B iff there is no circumstance in which A is true but B is false.")
    text("In a truth table, if there is nowhere A is True but B is not, then we can say A entails B.")
    text("Example:")
    text("[p ∧ q] entails p")
    image("images/entailment.png", width=160)

    text("**Help understand Scopal Ambiguity**")

    text("*Geordi didn't consult both Troi and Worf.*")
    text("Reading A:")
    text("*Geordi consulted neither Troi nor Worf.*")
    text("Reading B:")
    text("*It is not the case that Geordi consulted both Troi and Worf.*")

    text("Logical representations:")

    text("a. ¬[p ∧ r]")
    text("b. [¬p ∧ ¬r]")
    text("→ These two formulas are not equivalent.")

    text("------------------------------------------------")

    text("**3. Conditionals and Biconditionals**")

    text("**3.1 Conditional**")
    text("**Conditional V.S. Material Conditional(“→”):**")
    text("- **Conditional**: statements of the form 'if A then B'")
    text("- **Material Conditional**: a connective written as → (also ⊃), pronounced ‘if...then...’. The material conditional is the truth-functional connective that comes closest to conditional statements in natural language.")

    text("**Antecedent & Consequent**")
    text("In a conditional sentence of the form ‘**if p then q**’, **p** is called the **ANTECEDENT** and **q** is called the **CONSEQUENT**.")

    text("Truth Table for [p → q]:")

    image("images/antecedent_consequent1.png", width=400)

    text("For 3&4, if it’s not sunny, then whether it’s warm is irrelevant (the claim only pertains to situations where it’s sunny). So 3&4 would not falsify [p → q]. In general, a formula of the form [p → q] is false only when p is true and q is false, and true otherwise：")

    image("images/antecedent_consequent2.png", width=160)

    text("------------------------------------------------")

    text("**3.2 Biconditional (↔)**")

    text("Example:")

    text("a. *If yesterday was Sunday, then today is Monday.*")
    text("b. *If today is Monday, then yesterday was Sunday.*")
    text("→ *Today is Monday iff yesterday was Sunday.*")

    text("“↔”： Sometimes pronounced ‘if and only if’ (although it is just the closest thing to that idea we can express as a truth-functional connective).")
    text("Truth Table:")
    image("images/biconditional.png", width=160)

    text("[p ↔ q] is true whenever p and q have the same truth value — either both true or both false.")

def Q_and_A():
    text("# 问答环节：欢迎大家提问！")
    image("images/stuff.png", width=600)


if __name__ == "__main__":
    main()
