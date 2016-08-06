"""물질의 조합에 관한 딕셔너리
제일 위의 코드는 조합에 대한 코드, combination 코드에 물질을 입력하면 combination_dictionary 에서 물질을 찾아서 결과값을 보여주도록 조직함"""
def combination(a,b):
    if "comb(a,b)" or "comb(b,a)" in Combination_dictionary:
        return Combination_dictionary["comb(a,b)"]
    else:
        return "fail"
material = "입력된 코드"
def create(material):

    return
Combination_dictionary={"comb(fire,water)" : create("Steam"), "comb(fire, earth)" : create("Lava"), "comb(water, air)" : create("Ice"),
                        "comb(earth,earth)" : create("Stone"), "comb(water, earth)" : create("Plant"), "comb(stone, fire)" : create("Metal"), "comb(plant,earth)" : create("Oil"),
                        "comb(plant, fire)" : create("Methane"), "comb(plant, plant)" : create("wood")}

