stackable = [
    "mithril",
    "oric",
    "elder",
    "ancient",
    "silk",
    "gossamer",
    "thick",
    "hardened",
    "lucentmote",
    "reclaimedmetal",
    "spain",
    "senhancement",
    "scontrol",
    "cskill",
    "cpotence",
    "cbrilliance",
    "luck10",
    "luck50",
    "luck100",
    "luck200",
]
unstacked = [
    "amount",
    "rare",
    "exotic",
    "r_salvaged",
    "e_salvaged",
    "r_ecto",
    "e_ecto",
]

materials = stackable + unstacked


sum_expressions = ", ".join(
    [f"SUM({material}) as {material}" for material in materials]
)
