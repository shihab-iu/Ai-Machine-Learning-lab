parents = {
    ("Rahim", "Karim"),
    ("Karim", "Nadia"),
    ("Rahim", "Mina"),
    ("Mina", "Rafi"),
}
def children_of(person):
    return sorted(child for parent, child in parents if parent == person)
def infer_grandparents():
    result = set()
    for p1, c1 in parents:
        for p2, c2 in parents:
            if c1 == p2:
                result.add((p1, c2))
    return sorted(result)
print("Children of Rahim:", children_of("Rahim"))
print("Grandparent relations:", infer_grandparents())