from models import Node, Testimony

def load_turnabout_sisters():
    statements = [
        Node("S1", "statement", "DODGE_RIGHT", "Victim dodged first attack and ran to the right.", {"victim_ran_right": True}),
        Node("S2", "statement", "HIPPIE_HIT", "The girl in hippie clothes attacked the victim with The Thinker.", {"attacker_is_maya": True, "weapon_is_thinker": True}),
        Node("S3", "statement", "WEAPON_ID", "The weapon used was 'The Thinker' clock-statue.", {"weapon_is_thinker": True}),
        Node("S4", "statement", "APRIL_KNOWS", "April May knows that The Thinker is a clock.", {"april_knows_thinker_is_clock": True, "thinker_is_public_knowledge": True}),
        Node("S5", "statement", "HEARD_CLOCK", "April claims she heard it was a clock from somewhere.", {"april_knows_thinker_is_clock": True, "clockwork_is_functional": True}),
        Node("S5b", "statement", "SAW_STORE", "April claims she saw The Thinker at a department store.", {"april_knows_thinker_is_clock": True, "thinker_ever_sold": True}),
        Node("S6", "statement", "WHITE_SAW", "Redd White saw a man attack a woman from his hotel window.", {"white_witnessed_attack": True, "attacker_is_male": True}),
        Node("S7", "statement", "RAN_RIGHT_WHITE", "Redd White says the victim ran to the right (his perspective).", {"victim_ran_right": True}),
        Node("S8", "statement", "TWO_BLOWS", "Combined testimony implies the victim was struck at least twice.", {"victim_struck_once": False}),
        Node("S9", "statement", "SAW_STAND", "Redd White saw the glass light stand fall through the window.", {"light_stand_visible_from_window": True}),
        Node("S10", "statement", "STAND_THERE", "The light stand was already in the office before September 5th.", {"light_stand_in_office_before_sep5": True}),
    ]

    evidence = [
        Node("E1", "evidence", "AUTOPSY", "Autopsy report: death at 9PM, single blunt force trauma, instantaneous.", {"victim_struck_once": True, "time_of_death_9pm": True}),
        Node("E2", "evidence", "CELLPHONE", "Maya's cellphone: Mia asks Maya to hold The Thinker at 9:27 AM Sep 5.", {"mia_holds_thinker_sep5": True, "weapon_is_thinker": True}),
        Node("E3", "evidence", "THINKER", "The Thinker: made exclusively by Larry Butz, never sold publicly.", {"thinker_ever_sold": False, "thinker_is_public_knowledge": False, "clockwork_is_functional": False}),
        Node("E4", "evidence", "WIRETAP", "Wiretap found in April May's hotel room, listening to Fey & Co.", {"april_has_wiretap": True, "april_knows_thinker_is_clock": True}),
        Node("E5", "evidence", "BELLBOY", "Bellboy testimony: April ordered room service at exactly 9:00 PM.", {"april_in_room_9pm": True, "april_ordering_room_service_9pm": True}),
        Node("E6", "evidence", "GLASS_SHARDS", "Glass shards: light stand purchased September 4th.", {"light_stand_in_office_before_sep5": False, "light_stand_visible_from_window": False}),
    ]

    dep_edges = [
        ("S4",  "S5",  "REVISED TO"),   
        ("S5",  "S5b", "REVISED TO"),   
        ("S1",  "S2",  "DEPENDS ON"),   
        ("S3",  "S4",  "DEPENDS ON"),   
        ("S8",  "E1",  "CONSISTENT"),   
    ]

    return Testimony("Turnabout Sisters", statements, evidence, dep_edges)


def build_custom_case():
    statements = [
        Node("S1", "statement", "ALIVE_9PM", "The victim was alive at 9:00 PM.", {"victim_alive_9pm": True}),
        Node("S2", "statement", "SUSPECT_HOME", "The suspect was at home at 9:00 PM.", {"suspect_at_home_9pm": True}),
    ]

    evidence = [
        Node("E1", "evidence", "AUTOPSY", "Autopsy report: time of death was 8:30 PM.", {"victim_alive_9pm": False}),
        Node("E2", "evidence", "SECURITY_LOG", "Security log: suspect was seen leaving the building at 9:15 PM.", {"suspect_at_home_9pm": False}),
    ]

    return Testimony("Custom Case", statements, evidence, [])