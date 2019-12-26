from skills import Stats

stat_levels = {
    "strength": 10,
    "recovery": 10,
    "endurance": 10,
    "vigor": 10,
    "focus": 10,
    "clarity": 140,
    }

skill_ranks = {
    "intrinsic_clarity": 10,
    "intrinsic_focus": 10,
    "magical_synergy": 10,
    "amplify": 10,
    "extend": 10,
    "aura_focus": 10,
    "aura_synergy": 10,
    "compression": 10,
    "channel_mastery": 10,
    }

skill_options = {
    "amplify": {"active": True},
    "extend": {"active": True},
    "aura_focus": {"active": True},
    "aura_synergy": {"active": True},
    # Compression min: 0, max: TBD. Reduces range to increase intensity.
    "compression": {"active": True, "compression": 0},
    # Mastery min: 0, max: 2. Modifies intensity with corresponding cost.
    "channel_mastery": {"active": True, "mastery": 1},
    }

statsheet = Stats(stat_levels, skill_ranks)
print(statsheet.mana)
print(statsheet.mana_regen/24/60)