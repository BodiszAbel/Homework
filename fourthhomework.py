
class Team:
    def __init__(self,name,project,role):
            self.name = name
            self.project = project
            self.role = role
            print("-- Developer létrehozva. --")
            print(f"{name} a {project} -en dolgozik {role} szerepkörben.")


    def __eq__(self, other):
        return self.project == other.project

def workmates(workteam):
    for index_i, item_i in enumerate(workteam):
        for index_j, item_j in enumerate(workteam):
            if item_i.project == item_j.project  and index_i < index_j:
                print(f"{item_i.name} és {item_j.name} dolgoznak egy projektben.")

        pass

def alldevelopers():

    dev1 = Team("Ricsi", "Solarch", "Frontend")
    dev2 = Team("Angéla", "ZerTeng", "Tesztelő")
    dev3 = Team("Peti", "KefERP", "Frontend")
    dev4 = Team("Éva", "KefERP", "Backend")

    alldeveloperslist = [dev1, dev2, dev3, dev4]
    workmates(alldeveloperslist)


if __name__ == "__main__":

   alldevelopers()





