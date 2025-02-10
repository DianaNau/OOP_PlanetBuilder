from abc import ABC, abstractmethod
# ABC = Abstract Base Class
 
 
class Tier(ABC):
    @abstractmethod
    def geräusch_machen(self):
        pass
 
class Hund(Tier):
    def geräusch_machen(self):
        return "Wuffidewuff!!!"
   
class Katze(Tier):
    def geräusch_machen(self):
        return "MauzideMauz!!!"
   
class Löwe(Tier):
    def geräusch_machen(self):
        return "Brüllt ich will in den Urlaub!!!"
   
class Elefant(Tier):
    def geräusch_machen(self):
        return "Törömtömtöm"
   
class Ente(Tier):
    def geräusch_machen(self):
        return "QUAK QUAK"
   
 
#################################################################
 
class TierFactory(ABC):
    @abstractmethod
    def erzeuge_tier(self):
        pass
 
class HaustierFactory(TierFactory):
    def erzeuge_tier(self):
        return Katze()
 
 
class WildtierFactory(TierFactory):
    def erzeuge_tier(self):
        return Elefant()
   
 
def tier_ausgabe(factory):
    haustier = factory.erzeuge_tier()
    print(f"Dein erzeugtes Tier macht {haustier.geräusch_machen()}")
 
 
haustierfactory = HaustierFactory()
tier_ausgabe(haustierfactory)
 
wildtierFactory = WildtierFactory()
tier_ausgabe(wildtierFactory)
 
class AmerikanischeSteckdose:
    spannung = 110
 
    def spannung_ausgeben(self):
        return f"{self.spannung} V Liegen auf der Amerikanischen Steckdose"
 
 
 
class EuropäischeSteckdose:
    spannung = 230
 
    def spannung_ausgeben(self):
        return f"{self.spannung} V liegen auf der Europäischen Steckdose"
   
 
 
class SteckdosenAdapter(EuropäischeSteckdose):
    def __init__(self, gefundene_steckdose):
        self.gefundene_steckdose = gefundene_steckdose
 
    def spannung_ausgeben(self):
        return f"Adapter wandelt um von {self.gefundene_steckdose.spannung_ausgeben()} auf {self.spannung}"
   
 
gefundene_steckdose = AmerikanischeSteckdose()    
adapter_stecker = SteckdosenAdapter(gefundene_steckdose)
print(adapter_stecker.spannung_ausgeben())
 
 