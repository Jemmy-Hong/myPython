def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参
describe_pet("hamster", "harry")
describe_pet("dog", "willie")

#关键字实参(参数位置无关紧要了)
describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="willie", animal_type="dog")

#默认值
def describe_pet(pet_name, animal_type="dog"):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
