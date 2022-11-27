Echipa:

Ene Daniel Florin - 144

Manolache Andrei Bogdan - 144

Ficuta Vlad Stefan - 144

Casapu Stefan Georgian - 144



Descriere:

"wordle.py" este jocul wordle fara limita de incercari. Programul ia un cuvant random din fisierul "words.txt" si
afiseaza in terminal folosind "colorama" cuvantul primit prin input, cu litere colorate:

            - verde daca litera se afla pe pozitia buna
             
            - galben daca litera se afla in cuvant dar nu este pe pozitia buna
             
            - rosu daca litera nu se afla in cuvant
             
De asemenea, programul transmite literele verzi, galbene si rosii prin fisierul "feedback.txt".
La final sunt afisate in terminal: average guess, minimum guesss si maximum guess.



"wordle_guesser.py" este programul care ghiceste cuvantul cautat. Programul ia cuvantul cu cele mai comune litere
distincte pe pozitii din lista de cuvinte, il scrie in terminal-ul primului program folosind "pyautogui", iar apoi face
un update listei de cuvinte in functie de feedback-ul primit prin fisierul "feedback.txt":

          - elimina cuvintele care contin litere rosii
        
          - pastreaza doar cuvintele care contin litere verzi pe pozitiile respective
        
          - pastreaza doar cuvintele care contin litere galbene, dar nu pe pozitiile respective
        
Cand programul citeste fisierul "feedback.txt" si vede ca a ghicit toate literele verzi, el incepe din nou sa ghiceasca
cuvinte din lista initiala.



"wordle_auto_guesser.py" este programul obtinut prin combinarea "wordle.py" si "wordle_guesser.py", folosit pentru
generearea fisierului "solutii.txt".



Instructiuni:

Se deschide primul terminal, se executa "python wordle.py" si se introduce numarul de cuvinte care trebuie ghicite

Se deschide al doilea terminal, se executa "python worlde_guesser.py", iar apoi click in primul terminal

PS: "pyautogui.typewrite()" nu merge in masina virtuala



Average guess: 4.50261917234154
