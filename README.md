# Bruter
Tiny bruteforce script written on python

Libraries:
 * Passlib 
 * Pyfiglet
 * argparse
 * Hashid

Start:
```bash
python3 brute.py -h
usage: brute.py [-h] [-t TARGET] [-w WORDLIST] [-m METHOD] [-l LIST]

options:
  -h, --help            show this help message and exit
  -t, --target TARGET   Your target hash
  -w, --wordlist WORDLIST
                        Wordlist path
  -m, --method METHOD   type of hash
  -l, --list LIST       print list of methods (python3 brute.py -l show)

```

example:
```shell
 python3 brute.py -t "$2a$12$R9h/cIPz0gi.URNNX3kh2OPST9/PgBkqquzi.Ss7KIUgO2t0jWMUW" -m bcrypt -w path/to/your/wordlist
```

<img width="1218" height="217" alt="Screenshot From 2026-09-06 17-22-07" src="https://github.com/user-attachments/assets/f66bdf65-e935-48ac-a61d-964d9d631c7b" />
