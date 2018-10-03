import csv
# this program should be executed as __main__ program only 
if __name__ == "__main__":

    with open('soccer_players.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        Sharks=[]
        Dragons=[]
        Raptors=[]
        experienced=[]
        non_experienced=[]
        list1=list(csv_reader)

 # below function creates  classifies experienced and non-experienced players
        def players():
            for row in list1[1:].copy():
                if row[2]== 'YES':  # yes is for experinced players
                    row.pop(1)      # removes hight as it is not required in the output text file
                    experienced.append(row)
                    list1.pop(list1.index(row))
                else:
                    row.pop(1)
                    non_experienced.append(row)
                    list1.pop(list1.index(row))
            return experienced , non_experienced

            # the ouput of player() are teams of the league
        players()
        def teams():
            for m in experienced.copy():
                for t in non_experienced.copy():
                    if len(Sharks)<=(int(len(experienced+non_experienced)/3)-1):
                        Sharks.append(t)
                        Sharks.append(m)
                    if len(Dragons)<=(int(len(experienced+non_experienced)/3)-1):
                        Dragons.append(t)
                        Dragons.append(m)
                    if len(Raptors)<=(int(len(experienced+non_experienced)/3)-1):
                        Raptors.append(t)
                        Raptors.append(m)
            return Sharks,Dragons,Raptors

        teams()
        # below  function creates  teams text file
        def teams_file():
            with open ("teams.text","a") as file:
                file.write("Sharks")
                file.write("\n")
                for element in Sharks:
                    file.write(" , ".join(element))
                    file.write("\n")
                file.write("Dragons")
                file.write("\n")
                for element in Dragons:
                    file.write(" , ".join(element))
                    file.write("\n")
                file.write("Raptors")
                file.write("\n")
                for element in Raptors:
                    file.write(" , ".join(element))
                    file.write("\n")

        teams_file()
