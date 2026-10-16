facts = {"Rain"}
rules = [
    ({"Rain"}, "WetGround"),
    ({"WetGround"}, "Slippery"),
    ({"Slippery"}, "DriveSlowly"),
]
def forward_chain(facts, rules):
    inferred = set(facts)
    changed = True
    trace = []
    while changed:
        changed = False
        for premises, conclusion in rules:
            if premises.issubset(inferred) and conclusion not in inferred:
                inferred.add(conclusion)
                trace.append((premises, conclusion))
                changed = True
    return inferred, trace
knowledge, trace = forward_chain(facts, rules)
print("Inferred knowledge:", sorted(knowledge))
for premises, conclusion in trace:
    print(set(premises), "=>", conclusion)