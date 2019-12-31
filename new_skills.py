import json

def json_parser(skills_file):
    with open(skills_file) as skills_json:
        skill_data = json.load(skills_json)
    return skill_data
        
class MetaSkill():
    def __init__(self, **kwargs):
        self.full_name = kwargs["full_name"]
        self.description = kwargs["description"]
        self.name = kwargs["name"]
        self.rank = kwargs["rank"]

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
        # Synergy is the sum of all aura ranks
        self.synergy = synergy
        super().__init__(**kwargs)
        self.adders["intensity"] *= self.synergy
        self.adders["range"] *= self.synergy

class AuraCompression(MetaSkill):
    def __init__(self, compress, **kwargs):
        # Compress is a number of meters
        self.compress = compress
        super().__init__(**kwargs)
        self.adders["intensity"] *= self.compress
        # This is a direct range addition, not a percentage added
        self.adders["range"] -= self.compress

class ChannelMastery(MetaSkill):
    def __init__(self, channel, **kwargs):
        # Channel is a multiplier, 0 to 2
        self.channel = channel
        super().__init__(**kwargs)
        self.multipliers["intensity"] *= self.channel
        self.multipliers["cost"] *= self.channel

def main():
    skill_data = json_parser("skills.json")
    
    meta_skills = skill_data["meta_skills"]
    amplify_info = meta_skills[0]
    amplify = MetaSkill(**amplify_info)
    print(f"Amplify adders: {amplify.adders}")
    print(f"Amplify multipliers: {amplify.multipliers}")

    aura_synergy_info = meta_skills[3]
    synergy = 80
    aura_synergy = AuraSynergy(synergy, **aura_synergy_info)
    print(f"Aura Synergy adders: {aura_synergy.adders}")

    compression_info = meta_skills[4]
    compress = 5
    compression = AuraCompression(compress, **compression_info)
    print(f"Compression adders: {compression.adders}")

    channel_info = meta_skills[5]
    channel = 1.5
    channel_mastery = ChannelMastery(channel, **channel_info)
    print(f"Channel multipliers: {channel_mastery.multipliers}")

main()