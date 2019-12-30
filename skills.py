import json


class Skill():
    def __init__(self, skill_ranks, skill_info, skill_options):
        self.intensity = skill_info["intensity"]
        self.cost = skill_info["cost"]
        self.skill_range = skill_info["skill_range"]
        # Aura synergy is a constant passive boost
        self.aura_synergy(skill_ranks["aura_synergy"])

        if skill_options["amplify"]["active"]:
            self.amplify(skill_ranks["amplify"])
        if skill_options["extend"]["active"]:
            self.extend(skill_ranks["extend"])
        if skill_options["aura_focus"]["active"]:
            self.aura_focus(skill_ranks["aura_focus"])
        if skill_options["aura_synergy"]["active"]:
            self.aura_synergy(skill_ranks["aura_synergy"])
        if skill_options["compression"]["active"]:
            self.compression(
                skill_ranks["compression"], skill_options["compression"]["compress"])
        if skill_options["channel_mastery"]["active"]:
            self.channel_mastery(skill_options["channel_mastery"]["mastery"])

    def amplify(self, rank):
        self.intensity *= 0.2 * rank
        self.cost *= 0.3 * rank

    def extend(self, rank):
        self.cost *= 0.3 * rank
        self.skill_range += rank

    def aura_focus(self, rank):
        self.intensity *= 0.3 * rank
        self.cost *= 0.3 * rank
        self.skill_range *= 0.3 * rank

    def aura_synergy(self, rank):
        # TODO: make multiplier equal to sum of all ranks
        self.intensity += 0.08 * rank
        self.skill_range += 0.08 * rank

    def compression(self, rank, compress):
        # Unique; can trade off skill_range (compress, in meters) for intensity
        # "Increase" instead of multiply. Might be additive?
        self.intensity += 0.002 * rank * compress
        self.skill_range -= compress

    def channel_mastery(self, mastery):
        # Can control intensity (and by extension, cost). Intensity reprented as % from 0 to 2
        # rank = 10
        # Rank only affects upper/lower bounds (0 to 200)
        self.intensity *= mastery
        self.cost *= mastery

class Stats():
    def __init__(self, stat_levels, skill_ranks):
        self.strength = stat_levels["strength"]
        self.recovery = stat_levels["recovery"]
        self.endurance = stat_levels["endurance"]
        self.vigor = stat_levels["vigor"]
        self.focus = stat_levels["focus"]
        self.clarity = stat_levels["clarity"]

        # day_to_second = 1/24/60/60
        # 10 per day is the base mana regen from 1 clarity
        self.regen_per_clarity = 10
        # Class bonus (boost effect of clarity by 200%, effective x3 multiplier)
        self.regen_per_clarity *= 3
        self.mana_regen = self.regen_per_clarity * self.clarity

        # 20 base mana per focus
        self.mana_per_focus = 20
        self.mana = self.mana_per_focus * self.focus
        self.base_mana = self.mana

        # Skill ranks
        self.skill_ranks = skill_ranks

        # Intrinsics
        self.intrinsic_clarity(self.skill_ranks["intrinsic_clarity"])
        self.intrinsic_focus(self.skill_ranks["intrinsic_focus"])
        # Magical synergy works on *boosted* focus and clarity
        self.magical_synergy(self.skill_ranks["magical_synergy"])
    
    def intrinsic_clarity(self, rank):
        self.mana_regen *= 0.3 * rank
    
    def intrinsic_focus(self, rank):
        self.mana *= 0.3 * rank
    
    def magical_synergy(self, rank):
        self.mana += self.mana_regen * 0.025 * rank
        self.mana_regen += self.mana * 0.025 * rank

    def use_winter(self, skill_info, skill_options):
        # Boosts (additive) mana regen by 10% per rank
        winter = Skill(self.skill_ranks, skill_info, skill_options)
        print(winter.intensity)
        print(winter.skill_range)
        print(winter.cost)


