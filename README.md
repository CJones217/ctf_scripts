# ctf_scripts
rabbit_hole.sh : script that unzips a file as many times as you want. It may be missings some formats

power.py : script to find the max power usage of a day from logs

words.py : script that takes in the words used in a wordle clone and does the math found in the javascript to find which word will be used in the game

## US Cyber Games

pyshell : takes in guess and if it matches the flag, prints it out. solved with solver_pyshell and netcat version with nc_solver_pyshell

solver_pyshell : sends guess to pyshell and if the guess takes longer than the previous one, add that guessed letter to the solved answer as the longer the script takes, the more letters are right for the flag

nc_solver_pyshell : same as solver_pyshell but connects to netcat for the real ctf flag. the time might have to be corrected for "end - correct_end" as that will change based on your connection strength

solver_corrupt_flag : will read the bytes of a corrupt png and tries to fix the headers to make the picture work again

solve_wordy : quickly posts bs wordly guess to api endpoint, gets correct word from the response, and sends the correct word to the generated game_id to get the flag before the game_id expires
