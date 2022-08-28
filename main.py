import string
import json5

import config
import file_helper
import module
import modules
import file_helper


# Very unsafe method. FIXME Make me throw an error or something.
def is_gun(module_data):
    if module_data.get("flippedFrom") is not None or "WEAPONS" not in module_data.get("categories", []):
        print("Not a gun")
        return False
    else:
        print("A gun")
        return True


# We ignore single use modules and any module that we single out by name.
def is_relevant(module_data):
    return module_data["name"] not in config.ignored_modules and module_data.get("canResupplyInCombat", True) is True


def to_module(module_data):
    match module_data:
        case dict():
            print("Trying to find the culprit at : " + module_data.get("name"))
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
    match value_data:
        case dict():
            print("Bonusable value found")

            # Modifiers are weirdly formatted. Here we go:
            modifier_keys = list(set(value_data.keys()) - set(["base", "multipliers", "dividers", "deltas"]))
            if "cases" in modifier_keys:
                print("YOYO WHAT STOP RIGHT HERE CRIMINAL SCUM")
                raise TypeError("That's not ok")
            modifiers = {}
            for modifier in modifier_keys:
                modifiers[modifier] = value_data[modifier]

            return module.BonusableValue(base=value_data.get("base"),
                                         modifiers=modifiers,
                                         deltas=value_data.get("deltas", {}),
                                         multipliers=value_data.get("multipliers", {}),
                                         dividers=value_data.get("dividers", {}))
        case None:
            return None
        case _:
            return module.BonusableValue(base=value_data)


def load_modules_from_json(json_str):
    print("Loading module")
    object_set = json5.loads(json_str)
    match object_set:
        case dict():
            raise ValueError("Incorrect Json format for Airships. Please use the module file directly.")
        case list():
            print("It's a list, proceeding.")
            print(len(object_set))

            weapon_modules = [to_module(x) for x in object_set if is_gun(x) and is_relevant(x)]
            # print(weapon_modules)
            return weapon_modules
        case _:
            raise Exception("Value is neither an object nor a list. At any rate, we can only work with lists yet.")


def get_all_weapons():
    files = file_helper.get_file_array_from_folder(config.module_type_folder)
    all_weapon_lists = [load_modules_from_json(file) for file in files]
    print("All wepaon lists len " + str(len(all_weapon_lists)))
    # Python needs an easier to read flatmap in their list comprehension. This is bonkers readability.
    all_weapons = [module_data for weapon_list in all_weapon_lists for module_data in weapon_list]
    print("All weapons len " + str(len(all_weapons)))
    return all_weapons


def get_all_relevant_bonuses_from_weapons(weapons):
    # print("Weapons : " + str(weapons))
    bonusable_values = []
    relevant_bonuses = []

    for weapon in weapons:
        bonusable_values_lists = []
        bonusable_values_lists.append(module.WeaponModule.get_all_bonusable_values_as_list(weapon))
        print("Currently working on: " + weapon.name)
        print(bonusable_values_lists)
        for bonusable_value_list in bonusable_values_lists:
            [print(x) for x in bonusable_value_list]
            for bonusable_value in bonusable_value_list:
                [relevant_bonuses.append(x) for x in bonusable_value.get_all_relevant_techs() if
                 x not in relevant_bonuses]

    print(relevant_bonuses)
    # return [module.BonusableValue.get_all_relevant_techs(x) for x in bonusable_values]


# get_all_relevant_bonuses_from_weapons(load_modules_from_json(modules.cannon))
get_all_relevant_bonuses_from_weapons(get_all_weapons())
# [print(weapon.name) for weapon in get_all_weapons_from_folder()]
# print(get_all_relevant_bonuses_from_weapons(
#    load_modules_from_json(file_helper.get_file_contents(config.module_type_folder, "ROCKETS.json"))))
