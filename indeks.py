"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    My care is loss of care with old care done.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""
def clean_and_split(text: str) -> list[str]:
    """Funkcja pomocnicza usuwająca interpunkcję i dzieląca tekst na słowa."""

    cleaned = "".join(c.lower() if c.isalnum() or c.isspace() else " " for c in text)

    return cleaned.split()

def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.
    """
    results = []

    doc_word_counts = []
    for doc in documents:
        words = clean_and_split(doc)
        counts = {}
        for word in words:
            counts[word] = counts.get(word, 0) + 1
        doc_word_counts.append(counts)


    for query in queries:
        query_lower = query.lower().strip()
        matched_docs = []


        for doc_id, counts in enumerate(doc_word_counts):
            if query_lower in counts:
                frequency = counts[query_lower]
                matched_docs.append((doc_id, frequency))


        if not matched_docs:
            results.append([])
            continue


        matched_docs.sort(key=lambda x: (-x[1], x[0]))


        sorted_ids = [doc_id for doc_id, freq in matched_docs]
        results.append(sorted_ids)

    return results




    ### return [[]] - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)



# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    n = int(input("Podaj liczbę dokumentów: "))
    documents = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(n):
        documents.append(input())

    # Pobranie liczby zapytań
    m = int(input("Podaj liczbę zapytań: "))
    queries = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(m):
        queries.append(input().strip())

    # Przetworzenie zapytań
    results = index_documents(documents, queries)

    # Wypisanie wyników
    print("Wyniki:")
    for res in results:
        print(res)