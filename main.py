
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n) if self.n else []
        if self.n:
            self.build(data, 1, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return

        mid = (start + end) // 2
        self.build(data, 2 * node, start, mid)
        self.build(data, 2 * node + 1, mid + 1, end)
        self.tree[node] = (
            self.tree[2 * node] + self.tree[2 * node + 1]
        )

    def query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return (
            self.query(2 * node, start, mid, left, right)
            + self.query(2 * node + 1, mid + 1, end, left, right)
        )

    def range_sum(self, left, right):
        if not self.n or left < 0 or right >= self.n or left > right:
            raise ValueError("Invalid range")
        return self.query(1, 0, self.n - 1, left, right)


def main():
    books = [
        {"title": "Python Basics", "pages": 120},
        {"title": "Data Structures", "pages": 250},
        {"title": "Algorithms", "pages": 300},
        {"title": "Database Systems", "pages": 180},
    ]

    pages = [book["pages"] for book in books]
    segment_tree = SegmentTree(pages)

    print("Index de livres")
    print("----------------")

    for i, book in enumerate(books):
        print(f"{i}: {book['title']} - {book['pages']} pages")

    print(
        "\nTotal pages des livres 1 à 3 :",
        segment_tree.range_sum(1, 3)
    )


if __name__ == "__main__":
    main()
