from peewee import *

db = PostgresqlDatabase('elements', user='postgres', password='',host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
class Elements(BaseModel):
    name = CharField()
    abbreviation = CharField()

def flashcards():
    db.create_tables([Elements])
    card1 = Elements(name = 'Hydrogen', abbreviation = 'H')
    card1.save()
    
    card2 = Elements(name = 'Helium', abbreviation = 'He')
    card2.save()
    
    card3 = Elements(name = 'Lithium', abbreviation = 'Li')
    card3.save()
    
    card4 = Elements(name = 'Beryllium', abbreviation = 'Be')
    card4.save()
    
    card5 = Elements(name = 'Boron', abbreviation = 'B')
    card5.save()

    card6 = Elements(name = 'Carbon', abbreviation = 'C')
    card6.save()

    card7 = Elements(name = 'Nitrogen', abbreviation = 'N')
    card7.save()

    card8 = Elements(name = 'Oxygen', abbreviation = 'O')
    card8.save()

    card9 = Elements(name = 'Fluorine', abbreviation = 'F')
    card9.save()

    card10 = Elements(name = 'Neon', abbreviation = 'N')
    card10.save()

    card11 = Elements(name = 'Sodium', abbreviation = 'Na')
    card11.save()

    card12 = Elements(name = 'Magnesium', abbreviation = 'Mg')
    card12.save()

    card13 = Elements(name = 'Aluminum', abbreviation = 'Al')
    card13.save()

    card14 = Elements(name = 'Silicon', abbreviation = 'Si')
    card14.save()

    card15 = Elements(name = 'Phosphorus', abbreviation = 'P')
    card15.save()

    card16 = Elements(name = 'Sulfur', abbreviation = 'S')
    card16.save()

    card17 = Elements(name = 'Chlorine', abbreviation = 'Cl')
    card17.save()

    card18 = Elements(name = 'Argon', abbreviation = 'Ar')
    card18.save()

    card19 = Elements(name = 'Potassium', abbreviation = 'K')
    card19.save()

    card20 = Elements(name = 'Calcium', abbreviation = 'Ca')
    card20.save()

    card21 = Elements(name = 'Scandium', abbreviation = 'Sc')
    card21.save()

    card22 = Elements(name = 'Titanium', abbreviation = 'Ti')
    card22.save()

    card23 = Elements(name = 'Vanadium', abbreviation = 'V')
    card23.save()

    card24 = Elements(name = 'Chromium', abbreviation = 'Cr')
    card24.save()

    card25 = Elements(name = 'Manganese', abbreviation = 'Mn')
    card25.save()

    card26 = Elements(name = 'Iron', abbreviation = 'Fe')
    card26.save()

    card27 = Elements(name = 'Cobalt', abbreviation = 'Co')
    card27.save()

    card28 = Elements(name = 'Nickel', abbreviation = 'Ni')
    card28.save()

    card29 = Elements(name = 'Copper', abbreviation = 'Cu')
    card29.save()

    card30 = Elements(name = 'Zinc', abbreviation = 'Zn')
    card30.save()

    card31 = Elements(name = 'Gallium', abbreviation = 'Ga')
    card31.save()

    card32 = Elements(name = 'Germanium', abbreviation = 'Ge')
    card32.save()

    card33 = Elements(name = 'Arsenic', abbreviation = 'As')
    card33.save()

    card34 = Elements(name = 'Selenium', abbreviation = 'Se')
    card34.save()

    card35 = Elements(name = 'Bromine', abbreviation = 'Br')
    card35.save()

    card36 = Elements(name = 'Krypton', abbreviation = 'Kr')
    card36.save()

    card37 = Elements(name = 'Rubidium', abbreviation = 'Rb')
    card37.save()

    card38 = Elements(name = 'Strontium', abbreviation = 'Sr')
    card38.save()

    card39 = Elements(name = 'Yttrium', abbreviation = 'Y')
    card39.save()

    card40 = Elements(name = 'Zirconium', abbreviation = 'Zr')
    card40.save()

    card41 = Elements(name = 'Niobium', abbreviation = 'Nb')
    card41.save()

    card42 = Elements(name = 'Molybdenum', abbreviation = 'Mo')
    card42.save()

    card43 = Elements(name = 'Technetium', abbreviation = 'Tc')
    card43.save()

    card44 = Elements(name = 'Ruthenium', abbreviation = 'Ru')
    card44.save()

    card45 = Elements(name = 'Rhodium', abbreviation = 'Rh')
    card45.save()

    card46 = Elements(name = 'Palladium', abbreviation = 'Pd')
    card46.save()

    card47 = Elements(name = 'Silver', abbreviation = 'Ag')
    card47.save()

    card48 = Elements(name = 'Cadmium', abbreviation = 'Cd')
    card48.save()

    card49 = Elements(name = 'Indium', abbreviation = 'In')
    card49.save()

    card50 = Elements(name = 'Tin', abbreviation = 'Sn')
    card50.save()

    card51 = Elements(name = 'Antimony', abbreviation = 'Sb')
    card51.save()

    card52 = Elements(name = 'Tellurium', abbreviation = 'Te')
    card52.save()

    card53 = Elements(name = 'Iodine', abbreviation = 'I')
    card53.save()

    card54 = Elements(name = 'Xenon', abbreviation = 'Xe')
    card54.save()

    card55 = Elements(name = 'Cesium', abbreviation = 'Cs')
    card55.save()

    card56 = Elements(name = 'Barium', abbreviation = 'Ba')
    card56.save()

    card57 = Elements(name = 'Lanthanum', abbreviation = 'La')
    card57.save()

    card58 = Elements(name = 'Cerium', abbreviation = 'Ce')
    card58.save()

    card59 = Elements(name = 'Praseodymium', abbreviation = 'Pr')
    card59.save()

    card60 = Elements(name = 'Neodymium', abbreviation = 'Nd')
    card60.save()

    card61 = Elements(name = 'Promethium', abbreviation = 'Pm')
    card61.save()

    card62 = Elements(name = 'Samarium', abbreviation = 'Sm')
    card62.save()

    card63 = Elements(name = 'Europium', abbreviation = 'Eu')
    card63.save()

    card64 = Elements(name = 'Gadolinium', abbreviation = 'Gd')
    card64.save()

    card65 = Elements(name = 'Terbium', abbreviation = 'Tb')
    card65.save()

    card66 = Elements(name = 'Dysprosium', abbreviation = 'Dy')
    card66.save()

    card67 = Elements(name = 'Holmium', abbreviation = 'Ho')
    card67.save()

    card68 = Elements(name = 'Erbium', abbreviation = 'Er')    
    card68.save()

    card69 = Elements(name = 'Thulium', abbreviation = 'Tm')
    card69.save()

    card70 = Elements(name = 'Ytterbium', abbreviation = 'Yb')
    card70.save()

    card71 = Elements(name = 'Lutetium', abbreviation = 'Lu')
    card71.save()

    card72 = Elements(name = 'Hafnium', abbreviation = 'Hf')
    card72.save()

    card73 = Elements(name = 'Tantalum', abbreviation = 'Ta')
    card73.save()

    card74 = Elements(name = 'Tungsten', abbreviation = 'W')
    card74.save()

    card75 = Elements(name = 'Rhenium', abbreviation = 'Re')
    card75.save()

    card76 = Elements(name = 'Osmium', abbreviation = 'Os')
    card76.save()

    card77 = Elements(name = 'Iridium', abbreviation = 'Ir')
    card77.save()

    card78 = Elements(name = 'Platinum', abbreviation = 'Pt')
    card78.save()

    card79 = Elements(name = 'Gold', abbreviation = 'Au')
    card79.save()

    card80 = Elements(name = 'Mercury', abbreviation = 'Hg')
    card80.save()

    card81 = Elements(name = 'Thallium', abbreviation = 'Tl')
    card81.save()

    card82 = Elements(name = 'Lead', abbreviation = 'Pb')
    card82.save()

    card83 = Elements(name = 'Bismuth', abbreviation = 'Bi')
    card83.save()

    card84 = Elements(name = 'Polonium', abbreviation = 'Po')
    card84.save()

    card85 = Elements(name = 'Astatine', abbreviation = 'At')
    card85.save()

    card86 = Elements(name = 'Radon', abbreviation = 'Rn')
    card86.save()

    card87 = Elements(name = 'Francium', abbreviation = 'Fr')
    card87.save()

    card88 = Elements(name = 'Radium', abbreviation = 'Ra')
    card88.save()

    card89 = Elements(name = 'Actinium', abbreviation = 'Ac')
    card89.save()

    card90 = Elements(name = 'Thorium', abbreviation = 'Th')
    card90.save()

    card91 = Elements(name = 'Protactinium', abbreviation = 'Pa')
    card91.save()

    card92 = Elements(name = 'Uranium', abbreviation = 'U')
    card92.save()

    card93 = Elements(name = 'Neptunium', abbreviation = 'Np')
    card93.save()

    card94 = Elements(name = 'Plutonium', abbreviation = 'Pu')
    card94.save()

    card95 = Elements(name = 'Americium', abbreviation = 'Am')
    card95.save()

    card96 = Elements(name = 'Curium', abbreviation = 'Cm')
    card96.save()

    card97 = Elements(name = 'Berkelium', abbreviation = 'Bk')
    card97.save()

    card98 = Elements(name = 'Californium', abbreviation = 'Cf')
    card98.save()

    card99 = Elements(name = 'Einsteinium', abbreviation = 'Es')
    card99.save()

    card100 = Elements(name = 'Fermium', abbreviation = 'Fm')
    card100.save()

    card101 = Elements(name = 'Mendelevium', abbreviation = 'Md')
    card101.save()

    card102 = Elements(name = 'Nobelium', abbreviation = 'No')
    card102.save()

    card103 = Elements(name = 'Lawrencium', abbreviation = 'Lr')
    card103.save()

    card104 = Elements(name = 'Rutherfordium', abbreviation = 'Rf')
    card104.save()

    card105 = Elements(name = 'Dubnium', abbreviation = 'Db')
    card105.save()

    card106 = Elements(name = 'Seaborgium', abbreviation = 'Sg')
    card106.save()

    card107 = Elements(name = 'Bohrium', abbreviation = 'Bh')
    card107.save()

    card108 = Elements(name = 'Hassium', abbreviation = 'Hs')
    card108.save()

    card109 = Elements(name = 'Meitnerium', abbreviation = 'Mt')
    card109.save()

    card110 = Elements(name = 'Darmstadtium', abbreviation = 'Ds')
    card110.save()

    card111 = Elements(name = 'Roentgenium', abbreviation = 'Rg')
    card111.save()

    card112 = Elements(name = 'Ununbiium', abbreviation = 'Uub')
    card112.save()

    card113 = Elements(name = 'Ununquadium', abbreviation = 'Uuq')
    card113.save()




