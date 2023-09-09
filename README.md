# GolfBox IT Security Analysis

## Introduktion

Hej alle,

Mit navn er Lukas Jurs Schmidt. Som en del af min dybdegående interesse for IT-sikkerhed og softwareudvikling, faldt jeg over GolfBox's platform, mens jeg overvejede at tage golfsporten op. Dette projekt er et resultat af min observation og analyse af nogle potentielle sikkerhedsbrister i systemet.

## Sikkerhedsmæssige Observationer

1. **Test Login** 
   - Først og fremmest bør jeres [test login](https://www.golfbox.dk/portal/login/testLogin.asp?user=120-4515&pass=1234) ikke være så let tilgængeligt eller forudsigeligt.

2. **Passwordpolitik** 
   - Platformen tillader passwords med kun fire tegn uden krav til specialtegn. Denne begrænsning, kombineret med det faktum, at brugernavne starter med en identificerbar klubkode, kan udgøre en sikkerhedsrisiko.

3. **Loginmekanisme** 
   - Systemets login-feedback afslører detaljer, som kan hjælpe en angriber i at differentiere mellem:
     - Ugyldig bruger : "Capps log"
     - Ugyldigt password : "Capps log + Antal forsøg tilbage inden din konto bliver låst: 4!"
     - Gyldigt login => "ok"

4. **Mangel på CAPTCHA** 
   - Login-formularen indeholder ikke en CAPTCHA eller en tilsvarende mekanisme for at forhindre automatiserede loginforsøg. Dette kan udsætte platformen for potentielle brute force-angreb.

5. **Anonyme bookinganmodninger** 
   - Jeg bemærkede, at systemet tillader brugere at foretage anonyme bookinganmodninger.

## Projektstruktur og Forklaring

### `createUsernameList.py`
- **Beskrivelse**: Genererer en kombination af alle tænkelige brugernavne inden for en bestemt klub.
- **Hvordan man kører**: 
  ```python
  python3 createUsernameList.py
  ```

### `createPasswordList.py`
- **Beskrivelse**: Tager en wordliste rockyou.txt og filtrerer alle passwords som ikke indeholder specialtegn og kun indeholder fire tegn.
- **Hvordan man kører:**
```python
python3 createPasswordList.py 
```
### `checkUsernames.py`
- **Beskrivelse**: Checker alle kombinationer af brugernavne og identificerer eksisterende brugere.
- **Hvordan man kører:**
```python
python3 checkUsernames.py
```
### `main.py`
- **Beskrivelse:** Kode til at gætte brugeres passwords. Jeg har ikke afprøvet denne del, og den er mest baseret på mine egne antagelser om, hvad der kunne fungere.

## Afslutning
Mit hovedformål med at dele dette projekt er at belyse de sikkerhedsrisici, som GolfBox-platformen kan stå over for. Jeg har ikke forsøgt at få uautoriseret adgang til platformen, og dette arbejde er udelukkende til oplysende og uddannelsesmæssige formål.

Hvis nogen har feedback, spørgsmål eller ønsker at diskutere yderligere, er du velkommen til at åbne en issue eller sende mig en besked direkte.

**Med venlig hilsen**

Lukas Jurs Schmidt

Softwareudvikler og IT-sikkerhedsentusiast

53592705

lukas@dailydose.dk
