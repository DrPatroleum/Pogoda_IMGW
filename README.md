# Pogoda IMGW

Aplikacja Pogoda IMGW to prosta aplikacja desktopowa napisana w języku Python, która umożliwia sprawdzenie bieżących warunków pogodowych w wybranych miejscach w Polsce. Aplikacja korzysta z danych dostarczanych przez IMGW (Instytut Meteorologii i Gospodarki Wodnej) poprzez ich publiczne API.

## Funkcje

- Wybór lokalizacji z listy dostępnych miast w Polsce.
- Pobieranie i wyświetlanie aktualnych danych pogodowych dla wybranej lokalizacji.
- Wyświetlanie informacji takich jak temperatura, prędkość wiatru, kierunek wiatru, wilgotność, suma opadów i ciśnienie atmosferyczne.
- Obsługa różnych kategorii siły wiatru i kierunków wiatru.

## Instrukcja użycia

1. Wybierz lokalizację z dostępnej listy miast w rozwijanym menu.
2. Kliknij przycisk "Pokaż", aby sprawdzić aktualne dane pogodowe dla wybranej lokalizacji.
3. Wyniki zostaną wyświetlone poniżej na ekranie w formie czytelnych informacji tekstowych.

## Konfiguracja

Aby uruchomić aplikację na swoim komputerze, wykonaj następujące kroki:

1. Upewnij się, że masz zainstalowanego Pythona na swoim komputerze (wersja 3.7 lub nowsza).
2. Sklonuj ten projekt na swoje urządzenie.
3. Otwórz terminal i przejdź do katalogu projektu.
4. Zainstaluj potrzebne biblioteki, wpisując poniższą komendę:
   ```
   pip install requests tkinter
   ```
5. Uruchom aplikację, wpisując w terminalu:
   ```
   python pogoda.py
   ```

## Zależności

Aplikacja korzysta z następujących zależności:

- `requests` - do wykonywania żądań HTTP w celu pobierania danych pogodowych.
- `tkinter` - do tworzenia interfejsu graficznego użytkownika.

## Autor

Aplikację stworzył DrPatroleum. Jeśli masz pytania lub sugestie, skontaktuj się ze mną.
