class SimpleGraph:
    def __init__(self, edges: list[tuple[int]]) -> None:

        # Edges
        self.E: list[tuple[int]] = edges

        # Matrix
        self.n: int = max(max(e) for e in edges) + 1
        self.matrix: list[list[int]] = [
            [0 for _ in range(self.n)] for _ in range(self.n)]
        for u, v in edges:
            self.matrix[u][v] = 1
            self.matrix[v][u] = 1

        # Vertices
        self.V: set[int] = set(range(self.n))

    def degree(self, u: int) -> int:
        """
        Returns the degree of a vertex.
        """
        return sum(self.matrix[u])
