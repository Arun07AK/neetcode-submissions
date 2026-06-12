from typing import List, Tuple

def get_marks(scores: List[Tuple[str, int]])->int:
    name,mark=scores
    return mark
def best_student(scores: List[Tuple[str, int]]) -> str:
    scores_sorted=sorted(scores,key=get_marks,reverse=True)
    name,score=scores_sorted[0]
    return name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
