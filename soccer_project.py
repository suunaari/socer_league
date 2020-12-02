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
        def experts():
            for row in list1[1:]:
                if row[2]=="YES":
                    row.pop(1)
                    experienced.append(row)
                else :
                    row.pop(1)
                    non_experienced.append(row)
            return experienced , non_experienced
        experts()
        def teams():
            for rows in  experienced:
                if len(Sharks)<3:
                    Sharks.append(rows)
                    experienced.remove(rows)
            for rows in  non_experienced:
                if len(Sharks)<6:
                    Sharks.append(rows)
                    non_experienced.remove(rows)
            for rows in  experienced:
                if len(Dragons)<3:
                    Dragons.append(rows)
                    experienced.remove(rows)
                
            for rows in  non_experienced:
                if len(Dragons)<6:
                    Dragons.append(rows)
                    non_experienced.remove(rows)
            for rows in  experienced:
                if len(Raptors)<3:
                    Raptors.append(rows)
                    
                
            for rows in  non_experienced:
                if len(Raptors)<6:
                    Raptors.append(rows)
                    
                
            return Sharks,Dragons,Raptors
            
        teams()

        
        def teams_file():
            with open ("teams.txt","a") as file:
                file.write("Sharks")
                file.write("\n=======")
                file.write("\n")
                for element in Sharks:
                    file.write(" , ".join(element))
                    file.write("\n")
                file.write("\n"*2)
                file.write("Dragons")
                file.write("\n=======")
                file.write("\n")
                for element in Dragons:
                    file.write(" , ".join(element))
                    file.write("\n")
                file.write("\n"*2)
                file.write("Raptors")
                file.write("\n=======")
                file.write("\n")
                for element in Raptors:
                    file.write(" , ".join(element))
                    file.write("\n")

        teams_file()
