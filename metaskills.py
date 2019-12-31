import json

def json_parser(skills_file):
    with open(skills_file) as skills_json:
        skill_data = json.load(skills_json)
    return skill_data

class Skill():
    def __init__(self, **kwargs):
        self.full_name = kwargs["full_name"]
        self.description = kwargs["description"]
        self.rank = kwargs["rank"]
        
class MetaSkill(Skill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.multipliers = dict()
        self.adders = dict()
        self.effects = kwargs.get("effects")
        if self.effects:
            self.set_effects()
        self.arg_effects = kwargs.get("arg_effects")
        if self.arg_effects:
            self.set_arg_effects()
    
    def set_effects(self):
        for effect in self.effects:
            change = effect["change"]
            base = effect["base"]
            per_rank = effect["per_rank"]
            total_change = base + self.rank * per_rank
            if base == 0:
                self.adders[change] = total_change
            elif base == 1:
                self.multipliers[change] = total_change
    
    def set_arg_effects(self):
        for effect in self.arg_effects:
            change = effect["change"]
            base = effect["base"]
            if base == 0:
                self.adders[change] = base
            elif base == 1:
                self.multipliers[change] = base

class AuraSynergy(MetaSkill):
    def __init__(self, synergy, **kwargs):
        super().__init__(**kwargs)
        # Synergy is the sum of all aura ranks
        self.synergy = synergy
        self.adders["intensity"] *= self.synergy
        self.adders["range"] *= self.synergy

class AuraCompression(MetaSkill):
    def __init__(self, compress, **kwargs):
        super().__init__(**kwargs)
        # Compress is a number of meters
        self.compress = compress
        self.adders["intensity"] *= self.compress
        # This is a direct range addition, not a percentage added
        self.adders["range"] -= self.compress

class ChannelMastery(MetaSkill):
    def __init__(self, channel, **kwargs):
        super().__init__(**kwargs)
        # Channel is a multiplier, 0 to 2
        self.channel = channel
        self.multipliers["intensity"] *= self.channel
        self.multipliers["cost"] *= self.channel

class Aura(Skill):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_cost = kwargs["base_cost"]
        self.cost = self.rank * base_cost
        self.cost_unit = kwargs["cost_unit"]
        base_range = kwargs["base_range"]
        self.range = self.rank * base_range  

class OffensiveAura(Aura):
    def __init__(self, focus, **kwargs):
        super().__init__(**kwargs)
        base_intensity = kwargs["base_intensity"]
        self.intensity = self.rank * base_intensity
        per_focus_intensity = kwargs["per_focus_intensity"]
        self.intensity += focus * per_focus_intensity

class DefensiveAura(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_intensity = kwargs["base_intensity"]
        self.intensity = self.rank * base_intensity

class Purify(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Detection(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_resolution = kwargs["base_resolution"]
        self.resolution = self.rank * base_resolution
        self.resolution_unit = kwargs["resolution_unit"]

class EssenceWell(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # The transfer rate here is represented by cost.
        # Actual mana transferred is modulated by efficiency.
        base_efficiency = kwargs["base_efficiency"]
        self.efficiency = self.rank * base_efficiency

class Velocity(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_speed_boost = kwargs["base_speed_boost"]
        self.speed_boost = self.rank * base_speed_boost

class ManaManipulation(Skill):
    def __init__(self, focus, **kwargs):
        super().__init__(**kwargs)
        base_transfer_rate = kwargs["base_transfer_rate"]
        per_focus_transfer_rate = kwargs["per_focus_transfer_rate"]
        self.transfer_rate = self.rank * base_transfer_rate + focus * per_focus_transfer_rate
        self.transfer_rate_unit = kwargs["transfer_rate_unit"]

class Winter(Aura):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        base_regen_boost = kwargs["base_regen_boost"]
        self.regen_boost = self.rank * base_regen_boost

def test():
    skills = json_parser("skills.json")
    focus = 10

    meta_skills = skills["meta_skills"]
    amplify_info = meta_skills["amplify"]
    amplify = MetaSkill(**amplify_info)
    print(f"Amplify adders: {amplify.adders}")
    print(f"Amplify multipliers: {amplify.multipliers}")

    aura_synergy_info = meta_skills["aura_synergy"]
    synergy = 80
    aura_synergy = AuraSynergy(synergy, **aura_synergy_info)
    print(f"Aura Synergy adders: {aura_synergy.adders}")

    compression_info = meta_skills["aura_compression"]
    compress = 5
    compression = AuraCompression(compress, **compression_info)
    print(f"Compression adders: {compression.adders}")

    channel_info = meta_skills["channel_mastery"]
    channel = 1.5
    channel_mastery = ChannelMastery(channel, **channel_info)
    print(f"Channel multipliers: {channel_mastery.multipliers}")

    offensive_auras = skills["offensive_auras"]
    immolate_info = offensive_auras["immolate"]
    immolate = OffensiveAura(focus, **immolate_info)
    print(f"Immolate intensity: {immolate.intensity}")
    print(f"Immolate cost: {immolate.cost}/{immolate.cost_unit}")
    print(f"Immolate range: {immolate.range}")

    defensive_auras = skills["defensive_auras"]
    force_ward_info = defensive_auras["force_ward"]
    force_ward = DefensiveAura(**force_ward_info)
    print(f"Force Ward intensity: {100*force_ward.intensity}%")
    print(f"Force Ward cost: {force_ward.cost}/{force_ward.cost_unit}")
    print(f"Force Ward range: {force_ward.range}")

    utility_auras = skills["utility_auras"]
    purify_info = utility_auras["purify"]
    purify = Purify(**purify_info)
    print(f"Purify cost: {purify.cost}/{purify.cost_unit}")
    print(f"Purify range: {purify.range}")

    detection_info = utility_auras["detection"]
    detection = Detection(**detection_info)
    print(f"Detection cost: {detection.cost}")
    print(f"Detection range: {detection.range}")
    print(f"Detection resolution: {detection.resolution}/{detection.resolution_unit}")

    essence_well_info = utility_auras["essence_well"]
    essence_well = EssenceWell(**essence_well_info)
    print(f"Essence Well transfer rate: {essence_well.cost}mp/{essence_well.cost_unit}")
    print(f"Essence Well efficiency: {essence_well.efficiency}")
    print(f"Essence Well range: {essence_well.range}")

    winter_info = utility_auras["winter"]
    winter = Winter(**winter_info)
    print(f"Winter boost: {winter.regen_boost}")
    print(f"Winter range: {winter.range}")
    print(f"Winter cost: {winter.cost}/{winter.cost_unit}")

    utilities = skills["utilities"]
    mana_manipulation_info = utilities["mana_manipulation"]
    mana_manipulation = ManaManipulation(focus, **mana_manipulation_info)
    print(f"Mana Manipulation transfer rate: {mana_manipulation.transfer_rate}/{mana_manipulation.transfer_rate_unit}")

test()