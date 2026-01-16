# Задание 1
objects = [
    ("Containment Cell A", 4),
    ("Archive Vault", 1),
    ("Bio Lab Sector", 3),
    ("Observation Wing", 2)
]

sorted_objects = sorted(objects, key=lambda x: x[1])
for obj in sorted_objects:
    print(f"  {obj[0]}: {obj[1]}")

# Задание 2
staff_shifts = [
    {"name": "Dr. Shaw", "shifts": 15, "rate": 120},
    {"name": "Agent Torres", "shifts": 20, "rate": 100},
    {"name": "Researcher H", "shifts": 12, "rate": 150}
]

total_costs = list(map(lambda emp: {
    "name": emp["name"],
    "total_cost": emp["shifts"] * emp["rate"]
}, staff_shifts))

max_cost = max(total_costs, key=lambda x: x["total_cost"])

for cost in total_costs:
    print(f"  {cost['name']}: ${cost['total_cost']}")
print(f"  Максимальная: {max_cost['name']} - ${max_cost['total_cost']}")

# Задание 3
personnel = [
    {"name": "Dr. Klein", "level": 4},
    {"name": "Agent Brooks", "level": 2},
    {"name": "Technician R", "level": 1}
]

personnel_with_category = list(map(lambda p: {
    "name": p["name"],
    "level": p["level"],
    "category": "Top Secret" if p["level"] >= 4 else 
               "Confidential" if p["level"] >= 2 else 
               "Restricted"
}, personnel))

for p in personnel_with_category:
    print(f"  {p['name']}: уровень {p['level']} - {p['category']}")

# Задание 4
zones = [
    {"zone": "Sector-12", "start": 8, "end": 18},
    {"zone": "Deep Storage", "start": 22, "end": 6},
    {"zone": "Research Wing", "start": 9, "end": 17}
]

daytime_zones = list(filter(lambda z: z["start"] >= 8 and z["end"] <= 18, zones))

for z in daytime_zones:
    print(f"  {z['zone']}: {z['start']}:00-{z['end']}:00")

# Задание 5
reports = [
    {"author": "Dr. Moss", "content": "Report with http link"},
    {"author": "Agent Lee", "content": "Regular report"},
    {"author": "Dr. Patel", "content": "Data https://example.com"},
    {"author": "Supervisor", "content": "Summary report"}
]

http_reports = list(filter(lambda r: "http" in r["content"], reports))
cleaned_reports = list(map(lambda r: {
    "author": r["author"],
    "content": r["content"].replace("http", "[ДАННЫЕ УДАЛЕНЫ]").replace("https", "[ДАННЫЕ УДАЛЕНЫ]")
}, http_reports))

for r in cleaned_reports:
    print(f"  {r['author']}: {r['content']}")

# Задание 6
scp_objects = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]

enhanced_scp = list(filter(lambda s: s["class"] != "Safe", scp_objects))

for scp in enhanced_scp:
    print(f"  {scp['scp']}: класс {scp['class']}")

# Задание 7
incidents = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 25}
]

sorted_incidents = sorted(incidents, key=lambda x: x["staff"], reverse=True)
top_three = sorted_incidents[:3]

for inc in top_three:
    print(f"  Инцидент {inc['id']}: {inc['staff']} персонала")

# Задание 8
protocols = [
    ("Lockdown", 5),
    ("Evacuation", 4),
    ("Data Wipe", 3),
    ("Routine Scan", 1)
]

protocol_strings = list(map(lambda p: f"Protocol {p[0]} - Criticality {p[1]}", protocols))

for proto in protocol_strings:
    print(f"  {proto}")

# Задание 9
shifts = [6, 12, 8, 24, 10]
filtered_shifts = list(filter(lambda x: x >= 8 and x <= 12, shifts))

print(f"  {filtered_shifts}")

# Задание 10
evaluations = [
    {"name": "Agent Cole", "score": 85},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician M", "score": 78},
    {"name": "Researcher L", "score": 95}
]

best_employee = max(evaluations, key=lambda x: x["score"])

print(f"  {best_employee['name']}: {best_employee['score']} баллов")