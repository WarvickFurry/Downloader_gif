import json
import requests
import os
from json_updater import JSONUpdater

class tag_sorting:
    def __init__(self):
        pass
        # Создаем экземпляр класса и сразу обновляем JSON файл.
        self.updater = JSONUpdater("config.json")
        self.updater.update_json_file(self.data)

        #config = self.load_data_from_json()
        #data = [v for key, v in config["category"]["mine_cat"].items() if key != "type"]
        #data2 = [v for key, v in config["category"]["only_one"].items() if key != "type"]
        #self.tag_filer(data, data2, self.download_link_gif("https://derpibooru.org/images/3393194"))



    def cat_table(self, inTable):
        return [tag.replace("@equestriagif", "").replace("#", "") for tag in inTable]

    def read_tags(self, tags):
        return [i.replace(" ", "_").replace('-', '') for i in tags]

    def download_link_gif(self, link):
        config = self.load_data_from_json()
        data = [v for key, v in config["category"]["mine_cat"].items() if key != "type"]
        data2 = [v for key, v in config["category"]["only_one"].items() if key != "type"]
        # self.tag_filer(data, data2, self.read_tags(requests.get("https://derpibooru.org/api/v1/json/images/" + link.replace("https://derpibooru.org/images/", "")).json()['image']['tags']))
        if not os.path.isdir('temp'):
            os.mkdir('temp')

        self.write_tags1(self.tag_filer(data, data2, self.read_tags(requests.get("https://derpibooru.org/api/v1/json/images/" + link.replace("https://derpibooru.org/images/", "")).json()['image']['tags'])), "temp/autTags")


    def write_tags1(self, autTags, filename):
        with open(f"{filename}.txt", 'w') as file:
            for tag in autTags:
                file.write(tag + '\n')


    def load_data_from_json(self):
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                return config
        except FileNotFoundError:
            print("Файл не найден.")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON: {e}")
        except Exception as e:
            print(f"Произошла другая ошибка: {e}")
        return {}



    def tag_filer(self, cat,only_one, gif_tags):
        aut = []
        a = 0
        a1 = 0
        eg = 0
        for d in range(len(only_one)):
            c = self.cat_table(only_one[d])
            for e in range(len(c)):
                if list(filter(lambda x: c[e] in x, gif_tags)):
                    if aut.count(only_one[d][0]) < 1:
                        a1 += 1
                if a1 != 0:
                    aut.insert(0, only_one[d][0])
                    a1 = 0
        for i in range(len(cat)):
            t = self.cat_table(cat[i])  #список категорий

            for j in range(len(t)):
                if bool(list(filter(lambda x: t[j] in x, gif_tags))):
                    if any("sunset_shimmer" in tag for tag in list(filter(lambda x: t[j] in x, gif_tags)))  and "#equestria_girls@equestriagif" == cat[i][0]:
                        j -= 1
                        if any("equestria_girls" in tag for tag in list(filter(lambda x: t[j] in x, gif_tags))):
                            eg += 1
                if bool(list(filter(lambda x: t[j] in x, gif_tags))):
                    if cat[i][0] == "#oc@equestriagif":
                        if any("oc" in tag for tag in list(filter(lambda x: t[j] in x, gif_tags))) and any("oc:" in tag for tag in list(filter(lambda x: t[j] in x, gif_tags))):
                            if cat[i][j] not in aut:
                                if j == 0 and cat[i][j] not in aut:
                                    a += 1
                                else:
                                    aut += [cat[i][j]]
                            if [cat[i][0]] != [cat[i][j]]:
                                a += 1
                        else:
                            i += 1
                    else:
                        if cat[i][j] not in aut:
                            if j == 0 and cat[i][j] not in aut:
                                a += 1
                            else:
                                aut += [cat[i][j]]
                        if [cat[i][0]] != [cat[i][j]]:
                            a += 1
            if a != 0:
                aut.insert(0, cat[i][0])
                a = 0

        if eg != 0:
            eg = 0
            aut.remove("#other_ponies@equestriagif")

        return aut

    data = {
        "category": {
            "mine_cat": {
                "type": 0,
                "M6": [
                    "#mane6@equestriagif",
                    "#applejack@equestriagif",
                    "#fluttershy@equestriagif",
                    "#rarity@equestriagif",
                    "#pinkie_pie@equestriagif",
                    "#twilight_sparkle@equestriagif",
                    "#rainbow_dash@equestriagif",
                    "#spike@equestriagif"
                ],
                "CMC": [
                    "#cmc@equestriagif",
                    "#apple_bloom@equestriagif",
                    "#babs_seed@equestriagif",
                    "#gabby@equestriagif",
                    "#scootaloo@equestriagif",
                    "#sweetie_belle@equestriagif"
                ],
                "R": [
                    "#royalty@equestriagif",
                    "#celestia@equestriagif",
                    "#luna@equestriagif",
                    "#cadance@equestriagif",
                    "#shining_armor@equestriagif",
                    "#flurry_heart@equestriagif",
                    "#ember@equestriagif",
                    "#thorax@equestriagif"
                ],
                "A": [
                    "#antagonists@equestriagif",
                    "#grogar@equestriagif",
                    "#king_sombra@equestriagif",
                    "#nightmare_moon@equestriagif",
                    "#daybreaker@equestriagif",
                    "#queen_chrysalis@equestriagif",
                    "#cozy_glow@equestriagif",
                    "#lord_tirek@equestriagif",
                    "#maneiac@equestriagif",
                ],
                "AF": [
                    "#apple_family@equestriagif",
                    "#granny_smith@equestriagif",
                    "#big_mcintosh@equestriagif",
                    "#bright_mac_and_pear_butter@equestriagif"
                ],
                "PF": [
                    "#pie_family@equestriagif",
                    "#limestone_pie@equestriagif",
                    "#marble_pie@equestriagif",
                    "#maud_pie@equestriagif",
                    "#igneous_rock_pie_and_cloudy_quartz@equestriagif"
                ],
                "O": [
                    "#other_ponies@equestriagif",
                    "#trixie@equestriagif",
                    "#sunset_shimmer@equestriagif",
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
                ],
                "B": [
                    "#background_ponies@equestriagif",
                    "#dj_pon3@equestriagif",
                    "#derpy@equestriagif",
                    "#octavia@equestriagif",
                    "#bon_bon@equestriagif",
                    "#lyra@equestriagif",
                    "#dr_hooves@equestriagif",
                    "#bulk_biceps@equestriagif"
                ],
                "MOV": [
                    "#the_movie@equestriagif",
                    "#tempest@equestriagif",
                    "#songbird_serenade@equestriagif",
                    "#grubber@equestriagif",
                    "#the_storm_king@equestriagif",
                    "#capper@equestriagif",
                    "#captain_caelano@equestriagif",
                    "#queen_novo@equestriagif",
                    "#skystar@equestriagif"
                ],
                "EG": [
                    "#equestria_girls@equestriagif",
                    "#sunset_shimmer@equestriagif",
                    "#adagio_dazzle@equestriagif",
                    "#aria_blaze@equestriagif",
                    "#sonata_dusk@equestriagif"
                ],
                "OC": [
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
                ],
                "G5": [
                    "#g5@equestriagif",
                    "#izzy_moonbow@equestriagif",
                    "#sunny_starscout@equestriagif",
                    "#pipp@equestriagif",
                    "#zipp@equestriagif",
                    "#hitch_trailblazer@equestriagif",
                    "#misty@equestriagif"
                ]

            },
            "only_one": {
                "type": 1,
                "old": [
                    "#old_generations@equestriagif",
                    "#g1",
                    "#g2",
                    "#g3",
                    "#g3.5"
                ],
                "young6": [
                    "#young6@equestriagif",
                    "#gallus",
                    "#sandbar",
                    "#yona",
                    "#silverstream",
                    "#ocellus",
                    "#smolder"
                ],
                "pets": [
                    "#pets@equestriagif",
                    "#angel_bunny",
                    "#gummy",
                    "#opalescence",
                    "#silverstream",
                    "#tank",
                    "#winona"
                ],
                "pony_life": [
                    "#pony_life@equestriagif",
                    "#pony_life@equestriagif"
                ]
            },
        }
    }


test = tag_sorting()

