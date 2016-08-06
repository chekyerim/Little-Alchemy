
#1. Tower_Dictionary
"""물질의 특성을 기록 해 놓은 딕셔너리.
구성은  1.힘 2. 범위 3.공격속도 4.색깔
Dictionary which records the traits of materials
It is consist of
1. Power 2. Range 3. Speed 4. Color
"""
def p_level(n):
	return 10*n
def r_level(n):
	return 10*n
def s_level(n):
	return n

#색 정의
blue = (0, 0, 255)
red = (255, 0, 0)
lavender = (230, 230, 250)
peru = (205, 133, 63)
lightskyblue = (135,206,250)
darkorange = (255,140, 0)
azure = (240, 255, 255)
lime = (0, 255, 0)
gray = (128, 128, 128)
lightslategray = (119, 136, 153)
maroon = (128, 0, 0)
navy = (0, 0, 128)
saddlebrown = (139, 69, 19)

#물질에 다른 특성 정의
Water = {p_level(1), r_level(1), s_level(1), blue}
Fire = {p_level(1), r_level(1), s_level(1), red}
Air = {p_level(1), r_level(1), s_level(1), lavender}
Earth = {p_level(1), r_level(1), s_level(1), peru}
Steam = {p_level(2), r_level(2), s_level(2), lightskyblue}
Lava = {p_level(2), r_level(2), s_level(2), darkorange}
Ice = {p_level(2), r_level(2), s_level(2),  azure}
Plant = {p_level(2), r_level(2), s_level(2), lime}
Stone = {p_level(2), r_level(2), s_level(2), gray}
Metal = {p_level(3), r_level(3), s_level(3), lightslategray}
Oil = {p_level(3), r_level(3), s_level(3), maroon}
Methane = {p_level(4), r_level(4), s_level(4), navy}
Wood = {p_level(4), r_level(4), s_level(4), saddlebrown}

Tower_Dictionary = {"Water" : Water, "Fire" : Fire, "Air" : Air, "Earth" : Earth, "Steam" : Steam, "Lava" : Lava, "Ice" : Ice, "Plant" : Plant, "Stone" : Stone, "Metal" : Metal, "Oil" : Oil, "Methane" : Methane, "Wood" : Wood}

"""color name & code
water - blue : #0000FF RGB(0, 0, 255)
fire - red : #FF0000 RGB(255, 0, 0)
air - lavender #E6E6FA RGB(230, 230, 250)
earth - peru #CD853F RGB(205, 133, 63)
steam - lightskyblue : #87CEFA RGB(135, 206, 250)
lava - darkorange : #FF8C00 RGB(255, 140, 0)
ice - azure : #F0FFFF RGB(240, 255, 255)
plant - Lime : #00FF00 RGB(0, 255, 0)
metal - LIGHTSLATEGRAY : #778899 RGB(119, 136, 153)
stone - gray : #808080 RGB(128, 128, 128)
oil - Maroon : #800000 RGB(128, 0, 0)
methane - Navy : #000080 RGB(0, 0, 128)
wood - SADDLEBROWN : #8B4513 RGB(139, 69, 19)
Nytroglycerin - Aquamarine : #7FFFD4 RGB(127, 255, 212)
Membrane - Deeppink : #FF1493 RGB(255, 20, 147)
Thermite - Firebrick : #B22222 RGB(178, 34, 34)
A_Thermite - Orange : #FFA500 RGB(255, 165, 0)
Plutonium - Rosybrown : #BC8F8F RGB(188, 143, 143)
brown : #A52A2A"""

#2 Combination_Dictionary
"""물질의 조합에 관한 딕셔너리
제일 위의 코드는 조합에 대한 코드, combination 코드에 물질을 입력하면 combination_dictionary 에서 물질을 찾아서 결과값을 보여주도록 조직함"""
def combination(a,b):
    if "comb(a,b)" or "comb(b,a)" in Combination_dictionary:
        return Combination_dictionary["comb(a,b)"]
    else:
        return "fail"
material = "입력된 코드"

#초반 설정
available_tower = [Water, Fire, Air, Earth]

###value 값에 대한 정의 - 조합이 성공한 경우에 해당 타워를 이용할 수 있게 함
def create(material):
    available_tower.append(material)

#조합을 정리해 놓은 dictionary
Combination_dictionary={"comb(fire,water)" : create("Steam"), "comb(fire, earth)" : create("Lava"), "comb(water, air)" : create("Ice"),
                        "comb(earth,earth)" : create("Stone"), "comb(water, earth)" : create("Plant"), "comb(stone, fire)" : create("Metal"),
                        "comb(plant,earth)" : create("Oil"), "comb(plant, fire)" : create("Methane"), "comb(plant, plant)" : create("wood")}


