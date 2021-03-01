# Challenge - Die Story

Einer unserer Kunden hat ein Fehlverhalten einer Software festgestellt. Nun wurde **CGI** gebeten, sich das zügig an zu schauen und die Fehler zu fixen. 
Dabei hat der Kunde noch den Anspruch seine Applikation mit neuen Features erweitert zu bekommen. 

Daher schicken wir nun eine Entwicklerin zum Kunden, um das Problem an zu gehen und entsprechend eine gute Performance ab zu geben.

*Das erwartet sie!!*

## Aufgabe 1
Bug: Die Form wird nicht vollständig zurückgesetzt.

## Aufgabe 2
Es soll eine neue Seite erstellt werden, um alle Kommentare von der API zu laden und anzuzeigen.

Method: GET  
URL: '/api/comments'

Beispiel Response:
```
[
    {
        "comment": "Ich mag diese Seite sehr gerne!",
        "id": 1,
        "name": "Paul"
    },
    {
        "comment": "Ich mag diese Seite überhaupt nicht!",
        "id": 2,
        "name": "Kim"
    },
    {
        "comment": "Ich kenne diese Seite.",
        "id": 3,
        "name": "Teddy"
    }
]
```

## Aufgabe 3
Es sollen Sentiments (Gefühle/Empfindungen) zu jedem Kommentar ermitteln und angezeigt werden.
Die Art und Weise ist nicht vorgegeben, soll aber einem Mindestmaß an Esthetik entsprechen, den man einem potentiellen Kunden zumuten möchte.

*(Die API kann mehrere Texte entgegen nehmen.)*

**Es sollen folgende Kodierungen für Empfindungen verwendet werden:**  
Farben: 
- positiv = grün
- negativ = rot
- neutral = blau
- mixed = gelb

**Es steht folgende KI API zur Verfügung**

Method: POST  
URL: '/api/sentiment'  
Beispiel Body: ["Text1", "Text2"]

Das ist ein **Beispiel Response**:
```
[
    {
        "confidence_scores": {
            "negative": 0.03,
            "neutral": 0.94,
            "positive": 0.03
        },
        "id": "0",
        "sentiment": "neutral",
        "text": "Text1"
    },
    {
        "confidence_scores": {
            "negative": 0.03,
            "neutral": 0.94,
            "positive": 0.03
        },
        "id": "1",
        "sentiment": "neutral",
        "text": "Text2"
    }
]
```

## Aufgabe 4
1. Bitte zeigen Sie nur Kommentare an, deren *Negative* Confidence Score **kleiner** ist als der *Positive* Score und gleichzeitig **nicht** 75% überschreitet.
2. Ist der *Negative* Score eines Kommentars bei **mehr** als 40% wird dieser **immer** farblich hellrot markiert.
