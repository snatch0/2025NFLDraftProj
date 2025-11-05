
inp = open("interface.txt", "w")
infoPrint = open("plrinfo.txt", "r")
inp.write("2025 NFL ROOKIE LATEST GAME STATS\n")
inp.write("If strings return empty, player may not have played yet.\n\n")
user = str(input("Enter a 2025 draft pick number (1-262): "))
inp.write(user)

for line in infoPrint:
    if line.startswith(user):
        player_name = line.split("\t")[1]
        inp.write("\nRookie no. " + str(user) + " " + player_name + "\n")
        inp.write("date of recent game: " + line.split("\t")[2] + "\n" + "team: " + line.split("\t")[3] + "\n" + "opponent: " + line.split("\t")[4] + "\n" + "W/L: " + line.split("\t")[5] + "\n" + "score: " + line.split("\t")[6] )
        break
