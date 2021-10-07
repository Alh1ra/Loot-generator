# Python program to make first tests with classes, database, game-loot

'''     Targets:
            - Create random loot:
                - Weapons; different dph(maybe even dps) stats
                - Armor; different defense stats
            - Create database for player inventory; small inventory; items sellable for gold; upon
              inspecting inventory show remaining inventory slots and gold amount; 
            - Create savegame feature
'''

'''     Next Steps:
            - Block generation if inventory is full
'''

'''     Important Notes:
            - ...
'''


import sqlite3
import os
import random
import math

import armrstts
import wpnsstts

con = sqlite3.connect('usrdt.db')
cursor = con.cursor()

    # definition to clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print("")
print("Hello, user. Welcome to the loot dungeon.")
print("")

    # ask for continue or creation of new character; new characters get written to usrdt.db
new_or_continue = input("Would you like to create a (n)ew character or continue with your (l)ast one? ")

if new_or_continue == "n":
    print("")
    new_character_name = input("Splendid. Please enter the name of your character: ")
    print("")
    cursor.execute("INSERT INTO UserData(CharacterName,Gold,Inventory1,Inventory2,Inventory3,Inventory4,Inventory5,Inventory6,Inventory7) VALUES (?,?,?,?,?,?,?,?,?)", ((new_character_name),"0","0","0","0","0","0","0","0"))
    con.commit()
    print("Great,", new_character_name, "now let's go to the party.")
    selected_character = new_character_name
elif new_or_continue == "l":
    print("")
    print("Please select one of your characters:")
    print("")
    cursor.execute("SELECT CharacterName FROM UserData")
    for row in cursor:
        print(row[0])
    print("")
    selected_character = input("Please typ in the chosen characters name: ")
    cls()
    print("")
    print("Character", selected_character, "successfully loaded!")
    print("")
else:
    print("")
    print("I said chose between creating a [N]ew character or continuing with one of your [L]ast played ones.")
    print("")
    input()
    exit()


print("")
input("Please press ENTER to continue")

main_screen_loop = True
while main_screen_loop == True:
    cls()
    cursor.execute("SELECT * FROM UserData WHERE CharacterName=?", [selected_character])
    print("")
    for row in cursor:
        print("CharacterName = ", row[1])
        print("Gold = ", row[2])
    cursor.execute("SELECT Inventory1, Inventory2, Inventory3, Inventory4, Inventory5, Inventory6, Inventory7 FROM UserData WHERE CharacterName=?", [selected_character])
    print("")
    for row in cursor:
        inventory_1_id = row[0]
        inventory_2_id = row[1]
        inventory_3_id = row[2]
        inventory_4_id = row[3]
        inventory_5_id = row[4]
        inventory_6_id = row[5]
        inventory_7_id = row[6]
    if inventory_1_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_1_id])
        for row in cursor:
            inventory_1_name = row[0]
            print("Inventory Slot 1 contains =", inventory_1_name)
    else:
        print("Inventory Slot 1 contains = - Nothing -")
    if inventory_2_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_2_id])
        for row in cursor:
            inventory_2_name = row[0]
            print("Inventory Slot 2 contains =", inventory_2_name)
    else:
        print("Inventory Slot 2 contains = - Nothing -")
    if inventory_3_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_3_id])
        for row in cursor:
            inventory_3_name = row[0]
            print("Inventory Slot 3 contains =", inventory_3_name)
    else:
        print("Inventory Slot 3 contains = - Nothing -")
    if inventory_4_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_4_id])
        for row in cursor:
            inventory_4_name = row[0]
            print("Inventory Slot 4 contains =", inventory_4_name)
    else:
        print("Inventory Slot 4 contains = - Nothing -")
    if inventory_5_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_5_id])
        for row in cursor:
            inventory_5_name = row[0]
            print("Inventory Slot 5 contains =", inventory_5_name)
    else:
        print("Inventory Slot 5 contains = - Nothing -")
    if inventory_6_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_6_id])
        for row in cursor:
            inventory_6_name = row[0]
            print("Inventory Slot 6 contains =", inventory_6_name)
    else:
        print("Inventory Slot 6 contains = - Nothing -")
    if inventory_7_id != 0:
        cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_7_id])
        for row in cursor:
            inventory_7_name = row[0]
            print("Inventory Slot 7 contains =", inventory_7_name)
    else:
        print("Inventory Slot 7 contains = - Nothing -")
    print("")
    print("")
    print("What would you like to do next?")
    print("")
    print("1) Generate new weapon")
    print("2) Generate new armor")
    print("3) Sell loot")
    print("4) End program")
    print("")
    chosen_action = input("Please enter the number and hit ENTER: ")

    if chosen_action == "1":
        cls()
        print("")
        print("You generated:")
        print("")
        generated_weapon_class = random.choice(wpnsstts.possible_weapons_list)
        if generated_weapon_class == "Sword":
            generated_weapon_name = random.choice(wpnsstts.sword_possible_name_list)
            print(generated_weapon_name)
            generated_weapon_dmg = random.choice(wpnsstts.sword_base_dmg_range)
            print(generated_weapon_dmg)
            generated_weapon_durability_max = int(random.choice(wpnsstts.sword_durability_range))
            print(generated_weapon_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_weapon_durability_cur = math.floor((generated_weapon_durability_max / 100) * generated_dmg_quotient)
            print(generated_weapon_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_weapon_name),(generated_weapon_class),(generated_weapon_dmg),(generated_weapon_durability_max),(generated_weapon_durability_cur)))
            con.commit()
        elif generated_weapon_class == "Spear":
            generated_weapon_name = random.choice(wpnsstts.spear_possible_name_list)
            print(generated_weapon_name)
            generated_weapon_dmg = random.choice(wpnsstts.spear_base_dmg_range)
            print(generated_weapon_dmg)
            generated_weapon_durability_max = int(random.choice(wpnsstts.spear_durability_range))
            print(generated_weapon_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_weapon_durability_cur = math.floor((generated_weapon_durability_max / 100) * generated_dmg_quotient)
            print(generated_weapon_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_weapon_name),(generated_weapon_class),(generated_weapon_dmg),(generated_weapon_durability_max),(generated_weapon_durability_cur)))
            con.commit()
        elif generated_weapon_class == "Bow":
            generated_weapon_name = random.choice(wpnsstts.bow_possible_name_list)
            print(generated_weapon_name)
            generated_weapon_dmg = random.choice(wpnsstts.bow_base_dmg_range)
            print(generated_weapon_dmg)
            generated_weapon_durability_max = int(random.choice(wpnsstts.bow_durability_range))
            print(generated_weapon_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_weapon_durability_cur = math.floor((generated_weapon_durability_max / 100) * generated_dmg_quotient)
            print(generated_weapon_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_weapon_name),(generated_weapon_class),(generated_weapon_dmg),(generated_weapon_durability_max),(generated_weapon_durability_cur)))
            con.commit()
        cursor.execute("SELECT * FROM UserData WHERE CharacterName=?", [selected_character])
        for row in cursor:
            inventory1 = row[3]
            inventory2 = row[4]
            inventory3 = row[5]
            inventory4 = row[6]
            inventory5 = row[7]
            inventory6 = row[8]
            inventory7 = row[9]
        if inventory1 == 0:
            cursor.execute("UPDATE UserData SET Inventory1 = Inventory1 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory2 == 0:
            cursor.execute("UPDATE UserData SET Inventory2 = Inventory2 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory3 == 0:
            cursor.execute("UPDATE UserData SET Inventory3 = Inventory3 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory4 == 0:
            cursor.execute("UPDATE UserData SET Inventory4 = Inventory4 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory5 == 0:
            cursor.execute("UPDATE UserData SET Inventory5 = Inventory5 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory6 == 0:
            cursor.execute("UPDATE UserData SET Inventory6 = Inventory6 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory7 == 0:
            cursor.execute("UPDATE UserData SET Inventory7 = Inventory7 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        main_screen_loop = True
        print("")
        input("Press ENTER to continue.")
        print("")
    elif chosen_action == "2":
        cls()
        print("")
        print("You generated:")
        print("")
        generated_armor_class = random.choice(armrstts.possible_armor_list)
        if generated_armor_class == "Chest Plate":
            generated_armor_name = random.choice(armrstts.chest_plate_possible_name_list)
            print(generated_armor_name)
            generated_armor_protection = random.choice(armrstts.chest_plate_base_armor_range)
            print(generated_armor_protection)
            generated_armor_durability_max = int(random.choice(armrstts.chest_plate_durability_range))
            print(generated_armor_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_armor_durability_cur = math.floor((generated_armor_durability_max / 100) * generated_dmg_quotient)
            print(generated_armor_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_armor_name),(generated_armor_class),(generated_armor_protection),(generated_armor_durability_max),(generated_armor_durability_cur)))
            con.commit()
        elif generated_armor_class == "Helmet":
            generated_armor_name = random.choice(armrstts.helmet_possible_name_list)
            print(generated_armor_name)
            generated_armor_protection = random.choice(armrstts.helmet_base_armor_range)
            print(generated_armor_protection)
            generated_armor_durability_max = int(random.choice(armrstts.helmet_durability_range))
            print(generated_armor_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_armor_durability_cur = math.floor((generated_armor_durability_max / 100) * generated_dmg_quotient)
            print(generated_armor_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_armor_name),(generated_armor_class),(generated_armor_protection),(generated_armor_durability_max),(generated_armor_durability_cur)))
            con.commit()
        elif generated_armor_class == "Shield":
            generated_armor_name = random.choice(armrstts.shield_possible_name_list)
            print(generated_armor_name)
            generated_armor_protection = random.choice(armrstts.shield_base_armor_range)
            print(generated_armor_protection)
            generated_armor_durability_max = int(random.choice(armrstts.shield_durability_range))
            print(generated_armor_durability_max)
            generated_dmg_quotient = int(random.randint(55, 95))
            generated_armor_durability_cur = math.floor((generated_armor_durability_max / 100) * generated_dmg_quotient)
            print(generated_armor_durability_cur)
            generated_item_id = int(random.randint(10000000, 99999999))
            cursor.execute("INSERT INTO ItemData(ItemID,ItemName,ItemClass,ItemDmg,ItemDurabilityMax,ItemDurabilityCur) VALUES (?,?,?,?,?,?)", ((generated_item_id),(generated_armor_name),(generated_armor_class),(generated_armor_protection),(generated_armor_durability_max),(generated_armor_durability_cur)))
            con.commit()
        cursor.execute("SELECT * FROM UserData WHERE CharacterName=?", [selected_character])
        for row in cursor:
            inventory1 = row[3]
            inventory2 = row[4]
            inventory3 = row[5]
            inventory4 = row[6]
            inventory5 = row[7]
            inventory6 = row[8]
            inventory7 = row[9]
        if inventory1 == 0:
            cursor.execute("UPDATE UserData SET Inventory1 = Inventory1 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory2 == 0:
            cursor.execute("UPDATE UserData SET Inventory2 = Inventory2 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory3 == 0:
            cursor.execute("UPDATE UserData SET Inventory3 = Inventory3 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory4 == 0:
            cursor.execute("UPDATE UserData SET Inventory4 = Inventory4 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory5 == 0:
            cursor.execute("UPDATE UserData SET Inventory5 = Inventory5 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory6 == 0:
            cursor.execute("UPDATE UserData SET Inventory6 = Inventory6 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        elif inventory7 == 0:
            cursor.execute("UPDATE UserData SET Inventory7 = Inventory7 + ? WHERE CharacterName=?", [generated_item_id,selected_character])
            con.commit()
        main_screen_loop = True
        print("")
        input("Press ENTER to continue.")
        print("")
    elif chosen_action == '3':
        cls()
        cursor.execute("SELECT * FROM UserData WHERE CharacterName=?", [selected_character])
        print("")
        for row in cursor:
            print("CharacterName = ", row[1])
            print("Gold = ", row[2])
        cursor.execute("SELECT Inventory1, Inventory2, Inventory3, Inventory4, Inventory5, Inventory6, Inventory7 FROM UserData WHERE CharacterName=?", [selected_character])
        print("")
        for row in cursor:
            inventory_1_id = row[0]
            inventory_2_id = row[1]
            inventory_3_id = row[2]
            inventory_4_id = row[3]
            inventory_5_id = row[4]
            inventory_6_id = row[5]
            inventory_7_id = row[6]
        if inventory_1_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_1_id])
            for row in cursor:
                inventory_1_name = row[0]
                print("Inventory Slot 1 contains =", inventory_1_name)
        else:
            print("Inventory Slot 1 contains = - Nothing -")
        if inventory_2_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_2_id])
            for row in cursor:
                inventory_2_name = row[0]
                print("Inventory Slot 2 contains =", inventory_2_name)
        else:
            print("Inventory Slot 2 contains = - Nothing -")
        if inventory_3_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_3_id])
            for row in cursor:
                inventory_3_name = row[0]
                print("Inventory Slot 3 contains =", inventory_3_name)
        else:
            print("Inventory Slot 3 contains = - Nothing -")
        if inventory_4_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_4_id])
            for row in cursor:
                inventory_4_name = row[0]
                print("Inventory Slot 4 contains =", inventory_4_name)
        else:
            print("Inventory Slot 4 contains = - Nothing -")
        if inventory_5_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_5_id])
            for row in cursor:
                inventory_5_name = row[0]
                print("Inventory Slot 5 contains =", inventory_5_name)
        else:
            print("Inventory Slot 5 contains = - Nothing -")
        if inventory_6_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_6_id])
            for row in cursor:
                inventory_6_name = row[0]
                print("Inventory Slot 6 contains =", inventory_6_name)
        else:
            print("Inventory Slot 6 contains = - Nothing -")
        if inventory_7_id != 0:
            cursor.execute("SELECT ItemName FROM ItemData WHERE ItemID =?", [inventory_7_id])
            for row in cursor:
                inventory_7_name = row[0]
                print("Inventory Slot 7 contains =", inventory_7_name)
        else:
            print("Inventory Slot 7 contains = - Nothing -")
        print("")
        print("")
        item_to_sell = input("Please enter the number of the item you want to sell or enter 0 to go back to main menu: ")
        cls()
        print("")
        if item_to_sell == '1':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_1_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory1 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '2':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_2_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory2 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '3':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_3_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory3 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '4':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_4_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory4 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '5':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_5_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory5 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '6':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_6_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory6 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '7':
            cursor.execute("SELECT ItemDmg, ItemDurabilityMax, ItemDurabilityCur from ItemData WHERE ItemID=?", [inventory_7_id])
            for row in cursor:
                item_stat_1 = row[0]
                item_stat_2 = row[1]
                item_stat_3 = row[2]
            sold_item_gold = math.floor(item_stat_1 / 2 + item_stat_2 / 4 + item_stat_3 / 2)
            print("You sold this item for", sold_item_gold, "gold pieces")
            print("")
            cursor.execute("UPDATE UserData SET Inventory7 = 0 WHERE CharacterName=?", [selected_character])
            con.commit()
            cursor.execute("UPDATE UserData SET Gold = Gold + ? WHERE CharacterName=?", [sold_item_gold,selected_character])
            con.commit()
            input("Press ENTER to continue.")
            print("")
        elif item_to_sell == '0':
            print("Back to main menu")
        main_screen_loop = True
    elif chosen_action == '4':
        cls()
        print("")
        print("     Thanks for playing... whatever this is.")
        print("")
        print("     Have a nice day. :)")
        input()
        end()
else:


    # End of program message
    print("")
    print("")
    print("")
    print(" -- -- -- -- -- -- -- -- -- -- -- -- -- -- ")
    print("Reached end of program. Please hit ENTER to terminate.")
    print("")
    print("")
    input()

'''     AAR
Now that was one tough boy. Staring 3 hours at the screen and it was only a missing '. I did learn a lot of things, even more lessons.
First off i start to see why certain things get "outsourced" to a different module and i also get the idea of having something like a personal library for functions etc. I also learned
a lot about the different functions and got to use a few new ones.
The original target was more or less reached with this program. There is a character selection and creation, including saving to database. You can generate weapons and armor, all get
individual attributes from ranges. There is an inventory and you can sell the items for gold. I originally planned to add a function to block generating items when the inventory is full
but as the original target was reached and i found all lessons more or less to be learned i'm moving on. Also i think i would want to redo some of the code before adding this and at this
point i don't think i'd want to sink more time into this little starter project, especially since the next one will be basically building up on this one, expanding and refining it.

'''