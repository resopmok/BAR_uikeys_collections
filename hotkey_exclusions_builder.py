# This script generates a chain of exclusions that you can use in your hotkeys. For example, the default settings
# in this script will find all units that (1) have a description that contains the substring 'Constr' or 'Combat Engineer'
# and (2) have a description that does not contain the substring 'Tech 2'. This leaves all t1 constructors.
# It then uses this to generate the exclusions filter Not_IdMatches_armaap_Not_IdMatches_armaca_Not_IdMatches_armack ...
# , which you can use as part of a Filter in a custom keybind.
#
# To run this script, save it to a directory, open command prompt, navigate to that directory in command prompt, then run
# python hotkey_exclusions_builder.py
#
# You can then copy and paste the exclusions from the terminal into your hotkey file.


import requests


url = "https://raw.githubusercontent.com/beyond-all-reason/Beyond-All-Reason/master/language/en/units.json"


names_to_match = {}
descriptions_to_match = {"Constr", "Combat Engineer"}
names_to_avoid = {}
descriptions_to_avoid = {"Tech 2"}


def load_json_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to fetch JSON data from the URL")


def find_matching_names(json_data):
    if not len(names_to_match) + len(descriptions_to_match):
        print("names_to_match or descriptions_to_match can't both be empty.")
        return []
    matching_names = []
    units_data = json_data.get("units", {})
    names_data = units_data.get("names", {})
    descriptions_data = units_data.get("descriptions", {})

    for name_key in names_data.keys():
        name_value = names_data[name_key]
        description = descriptions_data.get(name_key)
        if not description:
            continue
        m1 = not len(names_to_match) or any(
            match in name_value for match in names_to_match
        )
        m2 = not len(descriptions_to_match) or any(
            match in description for match in descriptions_to_match
        )
        a1 = not any(avoid in name_value for avoid in names_to_avoid)
        a2 = not any(avoid in description for avoid in descriptions_to_avoid)
        condition = m1 and m2 and a1 and a2
        if len(names_to_match) and len(descriptions_to_match):
            condition = m1 or m2 and a1 and a2
        if condition:
            print(
                "Adding {} with name={} and description={}".format(
                    name_key, name_value, description
                )
            )
            matching_names.append(name_key)
    return matching_names


if __name__ == "__main__":
    try:
        json_data = load_json_from_url(url)
        matching_names = find_matching_names(json_data)
        if not len(matching_names):
            print("couldn't find matches")
        else:
            print("\nGot these exclusions:\n")
            print("_".join(["Not_IdMatches_" + i for i in matching_names]))
    except Exception as e:
        print(f"Error: {e}")
