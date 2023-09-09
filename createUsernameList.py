# Definerer klub ID og intervallet for de 4 cifre
club_id = "120"
start = 1
end = 9999

# Skriver kombinationerne til en fil
with open("usernames-list.txt", "w") as f:
    for number in range(start, end + 1):
        username = f"{club_id}-{number:04}"  # :04 formatterer tallet til altid at være 4 cifre langt, f.eks. "0001", "0010", osv.
        f.write(username + "\n")