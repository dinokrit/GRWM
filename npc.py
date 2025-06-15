class NPC:
    def __init__(self,name,hp,mana):
        self.name = name
        self.hp = hp
        self.mana = mana
    def stat(self):
        print("Name:", self.name)
        print("HP:", self.hp)
        print("Mana:", self.mana)
        print("-" * 20)

npc1 = NPC("Ken",100,150)
npc2 = NPC("Nara",100,180)

npc1.stat()
npc2.stat()