Hur kör du våran kod?
Kräver: Python 3.3 - Ladda ner om din version inte stämmer. 
Kan verifieras i din text-editor med: python --version

1: PIP
Skapa en “Path” till pip. 
Verifiera genom att skriva: path i kommandotolken (CMD) - Ser du en path som slutar med .../Scripts har du en path och kan hoppa över nästa steg.

2: PIP (path)
Skriv: 
setx PATH “C:\[Din path till PIP];%PATH%”

Ex till Python-mapp vilket rekommenderas: 
setx PATH "C:\Users\[Användarnamn]\Python\Python38-32\Scripts;%PATH%"

Efter detta bör du få upp ett meddelande som bekräftar att en Path har skapats korrekt. (SUCCESS: Specified value was saved.)

Notering: Försök skapa path direkt i CMD om du använder PowerShell. Vid felmeddelande klistra in i en googlesökning för att felsöka. 

3: GITHUB
Gå in på din GitHub Desktop och klona vårt repository.
GitHub Desktop: 
File -> Clone a repository -> URL ( i navbar) -> Skriv in: 
https://github.com/leomellbergholm/akademigastrologi 

Klona och fetcha changes för att se till att du har senaste versionen. 

4: Virtual Env
Öppna CMD och navigera genom (CD) kommandot till det directory du vill skapa din environment på. 
Skriv sedan: 
py -m venv venv. 

Efter lite tid kommer en mapp skapas i ditt directory (Platsen du valde). 
Kopiera mappen. 

Gå sedan till GitHub mappen på din dator och hitta Akademigastrologi, klicka dig in och kopiera in din egna venv-mapp in i mappen. 

5: Activate VENV

Navigera dig till din venv mapp i Akademigastrologi-mappen inne i CMD
Tips: Du kan gå till mappen och kopiera hela sökvägen för att sedan klistra in i CMD efter du använd “CD /” för att gå tillbaka till root-mappen. 

Sökvägen bör likna: C:\Users\[Användarnamn]\Documents\GitHub\akademigastrologi\app_data\venv\Scripts

Gå in i CMD och skriv “cd + sökvägen ovan” så kommer du till Scripts-mappen i projektmappen.
Skriv sedan: \activate
Du vet att du lyckats när det kommer upp “venv” framför din rad inne i CMD. 

6: Ladda ner requirements:

För att köra våran hemsida krävs en del ramverk och tillägg, för att ladda ner dessa använder du dig av våran requirement-textfil. 
Navigera dig tillbaka till huvudmappen för projektet (app_data) genom kommandot “CD ..”

Skriv sedan pip install -r requirements.txt 
Vänta tills samtliga objekt laddats ner. 

7: Starta hemsidan: 

När du lyckats med de tidigare stegen skriver du i samma mapp directory som tidigare följande kommandon: 

set flask_app=run.py -> Enter 
set flask_env=development -> Enter 
flask run -> Enter

Efter detta bör hemsidan börja köra på din localhost och du bör få ett meddelande som liknar: 'Running on http://127.0.0.1:5000/'

Öppna din web-browser och surfa in till denna adress. 




 

