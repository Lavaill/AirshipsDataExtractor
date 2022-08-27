import string
import json5

import module
import modules


# Very unsafe method. FIXME Make me throw an error or something.
def is_gun(module_data):
    if module_data.get("flippedFrom") is not None and "WEAPON" not in module_data.get("categories", []):
        print("Not a gun")
        return False
    else:
        print("A gun")
        return True


def to_module(module_data):
    match module_data:
        case dict():
            return module.WeaponModule(name=module_data.get("name"),
                                       cost=to_bonusable_value(module_data.get("cost")),
                                       crew=to_bonusable_value(module_data.get("crew")),
                                       weight=to_bonusable_value(module_data.get("weight")),
                                       pierce=to_bonusable_value(module_data.get("penDmg")),
                                       blast=to_bonusable_value(module_data.get("blastDmg")),
                                       direct=to_bonusable_value(module_data.get("directDmg")),
                                       radius=to_bonusable_value(module_data.get("blastSplashRadius")),
                                       pellets=to_bonusable_value(module_data.get("numShots")),
                                       clip=to_bonusable_value(module_data.get("clip")),
                                       ammo=to_bonusable_value(module_data.get("ammoPerClip")),
                                       reload=to_bonusable_value(module_data.get("reload")),
                                       clip_reload=to_bonusable_value(module_data.get("clipReloadTime")))
        case _:
            print(type(module_data))
    return


def to_bonusable_value(value_data):
    print("Calling to_bonusable_value")

    match value_data:
        case dict():
            print("Bonusable value found")
            return module.BonusableValue(base=value_data.get("base"), multipliers=value_data.get("multipliers"))
        case _:
            #print(type(value_data))
            return value_data


def load_modules_from_json(json_str):
    print("Loading module")
    object_set = json5.loads(json_str)
    match object_set:
        case dict():
            raise ValueError("Incorrect Json format for Airships. Please use the module file directly.")
        case list():
            print("It's a list, proceeding.")
            print(len(object_set))

            weapon_modules = [x for x in object_set if is_gun(x)]
            print(weapon_modules)
            return weapon_modules
        case _:
            print("Welp")
            raise Exception("Value is neither an object nor a list. At any rate, we can only work with lists yet.")


print(to_module(load_modules_from_json(modules.cannon)[0]))
