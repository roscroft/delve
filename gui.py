from tkinter import *
from tkinter import ttk
from skills import Stats
from skills import Skill

root = Tk()
root.title("Character Stats")

def calculate(*args):
    str_attr = float(strength.get())
    rec_attr = float(recovery.get())
    end_attr = float(endurance.get())
    vig_attr = float(vigor.get())
    foc_attr = float(focus.get())
    cla_attr = float(clarity.get())

    stat_levels = {
    "strength": str_attr,
    "recovery": rec_attr,
    "endurance": end_attr,
    "vigor": vig_attr,
    "focus": foc_attr,
    "clarity": cla_attr,
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
    mana_base.set(statsheet.mana)
    mana_regen_base.set(statsheet.mana_regen/24/60/60)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

strength = StringVar(value=10)
recovery = StringVar(value=10)
endurance = StringVar(value=10)
vigor = StringVar(value=10)
focus = StringVar(value=10)
clarity = StringVar(value=200)

strength_entry = ttk.Entry(mainframe, width=7, textvariable=strength)
recovery_entry = ttk.Entry(mainframe, width=7, textvariable=recovery)
endurance_entry = ttk.Entry(mainframe, width=7, textvariable=endurance)
vigor_entry = ttk.Entry(mainframe, width=7, textvariable=vigor)
focus_entry = ttk.Entry(mainframe, width=7, textvariable=focus)
clarity_entry = ttk.Entry(mainframe, width=7, textvariable=clarity)

ttk.Label(mainframe, text="Strength").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Recovery").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Endurance").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Vigor").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="Focus").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, text="Clarity").grid(column=1, row=6, sticky=W)

strength_entry.grid(column=2, row=1, sticky=(W, E))
recovery_entry.grid(column=2, row=2, sticky=(W, E))
endurance_entry.grid(column=2, row=3, sticky=(W, E))
vigor_entry.grid(column=2, row=4, sticky=(W, E))
focus_entry.grid(column=2, row=5, sticky=(W, E))
clarity_entry.grid(column=2, row=6, sticky=(W, E))

health_total = StringVar()
health_base = StringVar()
health_modifier = StringVar()
health_regen_total = StringVar()
health_regen_base = StringVar()
health_regen_modifier = StringVar()
stamina_total = StringVar()
stamina_base = StringVar()
stamina_modifier = StringVar()
stamina_regen_total = StringVar()
stamina_regen_base = StringVar()
stamina_regen_modifier = StringVar()
mana_total = StringVar()
mana_base = StringVar()
mana_modifier = StringVar()
mana_regen_total = StringVar()
mana_regen_base = StringVar()
mana_regen_modifier = StringVar()

ttk.Label(mainframe, text="Health").grid(column=1, row=8, sticky=W)
ttk.Label(mainframe, text="Health Regen").grid(column=1, row=9, sticky=W)
ttk.Label(mainframe, text="Stamina").grid(column=1, row=10, sticky=W)
ttk.Label(mainframe, text="Stamina Regen").grid(column=1, row=11, sticky=W)
ttk.Label(mainframe, text="Mana").grid(column=1, row=12, sticky=W)
ttk.Label(mainframe, text="Mana Regen").grid(column=1, row=13, sticky=W)

ttk.Label(mainframe, text="Total").grid(column=2, row=7, sticky=W)
ttk.Label(mainframe, text="Base").grid(column=3, row=7, sticky=W)
ttk.Label(mainframe, text="Modifier").grid(column=4, row=7, sticky=W)

ttk.Label(mainframe, textvariable=health_total).grid(column=2, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=health_base).grid(column=3, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=health_modifier).grid(column=4, row=8, sticky=(W, E))
ttk.Label(mainframe, textvariable=health_regen_total).grid(column=2, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=health_regen_base).grid(column=3, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=health_regen_modifier).grid(column=4, row=9, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_total).grid(column=2, row=10, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_base).grid(column=3, row=10, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_modifier).grid(column=4, row=10, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_regen_total).grid(column=2, row=11, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_regen_base).grid(column=3, row=11, sticky=(W, E))
ttk.Label(mainframe, textvariable=stamina_regen_modifier).grid(column=4, row=11, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_total).grid(column=2, row=12, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_base).grid(column=3, row=12, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_modifier).grid(column=4, row=12, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_regen_total).grid(column=2, row=13, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_regen_base).grid(column=3, row=13, sticky=(W, E))
ttk.Label(mainframe, textvariable=mana_regen_modifier).grid(column=4, row=13, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=7, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

strength_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()