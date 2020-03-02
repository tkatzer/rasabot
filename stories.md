## Get started
* get_started
  - utter_get_started
## Greetings
* chitchat.greet
  - utter_hi
## Farewells
* chitchat.bye
  - utter_bye
## happy path
* Begruessung
  - utter_Begruessung
* Bestaetigen
  - utter_name_interessent
* Name{"Name_Interessent":"Mister X"}
  - slot{"Name_Interessent":"Mister X"}
  - utter_Frage_E-Mail
* E-Mail{"E-Mail_Interessent":"beispiel@irgendwas.de"}
  - slot{"E-Mail_Interessent":"beispiel@irgendwas.de"}
  - utter_date_picker
> happy_path__branches
## happy path__Heute
> happy_path__branches
* Treffen_heute
  - utter_Vorschlag_Zeiten
* Treffen_Zeit_10
  - utter_Frage_Infomaterial
* Infomaterial_Bestaetigt
  - utter_Verabschiedung
  - write_database
## happy path__Morgen
> happy_path__branches
* Treffen_morgen
  - utter_Vorschlag_Zeiten
* Treffen_Zeit_10
  - utter_Frage_Infomaterial
* Infomaterial_Bestaetigt
  - utter_Verabschiedung
  - write_database
