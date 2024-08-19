
import os.path
import requests



# def read_tags(infilename):
#     with open(f"{infilename}.txt", 'r') as file:
#         return [tag.replace(" ", "_") for tag in file.read().split(", ")]



def read_tags(tags):
    for i in tags:
        return [i.replace(" ", "_").replace('-', '') for i in tags]



def cat_table(inTable):
    return [tag[1:].replace("@equestriagif", "") for tag in inTable[1:]]


# def tags_sort(inTable, cat):  # проверка и изменение тегов списка
#     aut = []
#     a = 0
#     for i in range(len(cat)):
#         t = cat_table(cat[i])  # список категорий
#         for j in range(len(t)):
#             if list(filter(lambda x: t[j] in x, inTable)):
#                 aut += [cat[i][j + 1]]
#                 a += 1
#         if a != 0:
#             aut.insert(0, cat[i][0])
#             a = 0
#     return aut


def tags_sort(inTable, cat, exclusions, only_one):  # проверка и изменение тегов списка
    aut = []
    a = 0
    a1 = 0

    for d in range(len(only_one)):
        c = cat_table(only_one[d])
        for e in range(len(c)):
            if list(filter(lambda x: c[e] in x, inTable)):
                if aut.count(only_one[d][0]) < 1:
                    a1 += 1

            if a1 != 0:
                aut.insert(0, only_one[d][0])
                a1 = 0

    for i in range(len(cat)):
        t = cat_table(cat[i])  # список категорий
        for j in range(len(t)):

            if list(filter(lambda x: t[j] in x and x not in exclusions and not any(non_tag in x for non_tag in if_non_list), inTable)):
                if cat[i][j + 1] not in aut and [cat[i][0]] != [cat[i][j + 1]]:
                    print("tag", cat[i][j + 1])
                    aut += [cat[i][j + 1]]
                if [cat[i][0]] != [cat[i][j + 1]]:
                    a += 1

        if a != 0:
            aut.insert(0, cat[i][0])
            print("category",cat[i][0])
            a = 0

    return aut








def write_tags1(autTags,filename):
    with open(f"{filename}.txt", 'w') as file:
        for tag in autTags:
            file.write(tag + '\n')


def download_link_gif(link):
    tags = read_tags(requests.get(f"{BASE_DERPIBOORU_URL}/" + link.replace("https://derpibooru.org/images/", "")).json()['image']['tags'])
    if not os.path.isdir('temp'):
        os.mkdir('temp')
    write_tags1(tags_sort(tags, category, if_non_list, only_one), "temp/autTags")


BASE_DERPIBOORU_URL = "https://derpibooru.org/api/v1/json/images/"
path_gif = os.path.join("temp", "equestria.gif")
path_tags = os.path.join("temp", "tags.txt")


category = []

M6 = [
    "#mane6@equestriagif",
    "#applejack@equestriagif",
    "#fluttershy@equestriagif",
    "#rarity@equestriagif",
    "#pinkie_pie@equestriagif",
    "#twilight_sparkle@equestriagif",
    "#rainbow_dash@equestriagif",
    "#spike@equestriagif"
]
category.insert(0,M6)
CMC = [
    "#cmc@equestriagif",
    "#apple_bloom@equestriagif",
    "#babs_seed@equestriagif",
    "#gabby@equestriagif",
    "#scootaloo@equestriagif",
    "#sweetie_belle@equestriagif"
]
category.insert(0,CMC)
R = [
    "#royalty@equestriagif",
    "#celestia@equestriagif",
    "#luna@equestriagif",
    "#cadance@equestriagif",
    "#shining_armor@equestriagif",
    "#flurry_heart@equestriagif",
    "#ember@equestriagif",
    "#thorax@equestriagif"
]
category.insert(0,R)
A = [
    "#antagonists@equestriagif",
    "#grogar@equestriagif",
    "#king_sombra@equestriagif",
    "#nightmare_moon@equestriagif",
    "#daybreaker@equestriagif",
    "#queen_chrysalis@equestriagif",
    "#cozy_glow@equestriagif",
    "#lord_tirek@equestriagif",
    "#maneiac@equestriagif",
]
category.insert(0,A)
AF = [
    "#apple_family@equestriagif",
    "#granny_smith@equestriagif",
    "#big_mcintosh@equestriagif",
    "#bright_mac_and_pear_butter@equestriagif"
]
category.insert(0,AF)
PF = [
    "#pie_family@equestriagif",
    "#limestone_pie@equestriagif",
    "#marble_pie@equestriagif",
    "#maud_pie@equestriagif",
    "#igneous_rock_pie_and_cloudy_quartz@equestriagif"
]
category.insert(0,PF)
O = [
    "#other_ponies@equestriagif",
    "#trixie@equestriagif",
    "#discord@equestriagif",
    "#starlight_glimmer@equestriagif",
    "#cheerilee@equestriagif",
    "#diamond_tiara@equestriagif",
    "#silver_spoon@equestriagif",
    "#spitfire@equestriagif",
    "#gilda@equestriagif",
    "#mayor_mare@equestriagif",
    "#flim_and_flam@equestriagif",
    "#daring_do@equestriagif",
    "#cheese_sandwich@equestriagif",
    "#tree_hugger@equestriagif",
    "#zecora@equestriagif",
    "#snails@equestriagif",
    "#snips@equestriagif",
    "#sunburst@equestriagif",
    "#photo_finish@equestriagif",
    "#redheart@equestriagif",
    "#coco_pommel@equestriagif",
    "#twilight_velvet_and_night_light@equestriagif",
    "#bow_hothoof_and_windy_whistles@equestriagif",
    "#braeburn@equestriagif",
    "#soarin@equestriagif",
    "#sugar_belle@equestriagif",
    "#cranky_doodle_donkey@equestriagif",
    "#moondancer@equestriagif",
    "#autumn_blaze@equestriagif",
    "#summer_flare@equestriagif"
]
category.insert(0,O)
B = [
    "#background_ponies@equestriagif",
    "#dj_pon3@equestriagif",
    "#derpy@equestriagif",
    "#octavia@equestriagif",
    "#bon_bon@equestriagif",
    "#lyra@equestriagif",
    "#dr_hooves@equestriagif",
    "#bulk_biceps@equestriagif"
]
category.insert(0,B)
MOV = [
    "#the_movie@equestriagif",
    "#tempest@equestriagif",
    "#songbird_serenade@equestriagif",
    "#grubber@equestriagif",
    "#the_storm_king@equestriagif",
    "#capper@equestriagif",
    "#captain_caelano@equestriagif",
    "#queen_novo@equestriagif",
    "#skystar@equestriagif"
]
category.insert(0,MOV)
EG = [
    "#equestria_girls@equestriagif",
    "#equestria_girls@equestriagif",
    "#sunset_shimmer@equestriagif",
    "#adagio_dazzle@equestriagif",
    "#aria_blaze@equestriagif",
    "#sonata_dusk@equestriagif"
]
category.insert(0,EG)
OC = [
    "#oc@equestriagif",
    "#oc@equestriagif",
    "#apogee@equestriagif",
    "#anon@equestriagif",
    "#filly_anon@equestriagif",
    "#echo@equestriagif",
    "#fausticorn@equestriagif",
    "#littlepip@equestriagif",
    "#blackjack@equestriagif",
    "#horse_wife@equestriagif",
    "#non_toxic@equestriagif",
    "#nootaz@equestriagif",
    "#paper_bag@equestriagif",
    "#delta_vee@equestriagif",
    "#celery@equestriagif",
    "#sugar_morning@equestriagif",
    "#purple_flix@equestriagif",
    "#bizarre_song@equestriagif",
    "#evo@equestriagif",
    "#nyx@equestriagif",
    "#snowdrop@equestriagif",
    "#cream_heart@equestriagif",
    "#fluffle_puff@equestriagif",
    "#athena@equestriagif"
]
category.insert(0,OC)
G5 = [
    "#g5@equestriagif",
    "#izzy_moonbow@equestriagif",
    "#sunny_starscout@equestriagif",
    "#pipp@equestriagif",
    "#zipp@equestriagif",
    "#hitch_trailblazer@equestriagif",
    "#misty@equestriagif"
]
category.insert(0,G5)

only_one = []
old = [
    "#old_generations@equestriagif",
    "#g1",
    "#g2",
    "#g3",
    "#g3.5"
]
only_one.insert(0,old)
young6 = [
    "#young6@equestriagif",
    "#gallus",
    "#sandbar",
    "#yona",
    "#silverstream",
    "#ocellus",
    "#smolder"
]
only_one.insert(0,young6)
pets = [
    "#pets@equestriagif",
    "#angel_bunny",
    "#gummy",
    "#opalescence",
    "#silverstream",
    "#tank",
    "#winona"
]
only_one.insert(0,pets)
pony_life = [
    "#pony_life@equestriagif",
    "#pony_life@equestriagif"
]
only_one.insert(0,pony_life)

if_non_list = [
    "not",
    "ocellus",
    "artist:",
    "trying",
    "murder",
    "try"
]


#print(download_link_gif("https://derpibooru.org/images/3402556"))