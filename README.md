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
<img width="1217" height="223" alt="Screenshot From 2026-09-06 17-26-30" src="https://github.com/user-attachments/assets/5d90f937-52eb-474c-8aac-f4388ac1e39c" />

