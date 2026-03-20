import random
import json

def generate_natural_user():
    first_names = [
        "Liam", "Noah", "Oliver", "James", "Elijah", "William", "Henry", "Lucas", "Benjamin", "Theodore",
        "Emma", "Olivia", "Charlotte", "Amelia", "Sophia", "Mia", "Isabella", "Ava", "Evelyn", "Luna",
        "Wei", "Zhihao", "Mei", "Yuki", "Satoshi", "Elena", "Mateo", "Sasha", "Kaito", "Ji-won",
        "Xavier", "Amara", "Arjun", "Chloe", "Kenji", "Zara", "Leo", "Maya", "Kai", "Sana"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
        "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
        "Lee", "Wong", "Chen", "Tanaka", "Sato", "Kim", "Park", "Ivanov", "Schmidt", "Muller",
        "Silva", "Ali", "Okonkwo", "Patel", "Dupont", "Nakamura", "Zhang", "Wagner", "O'Brien", "Gomez"
    ]
    domains = ["gmail.com", "hotmail.com", "outlook.com", "yahoo.com", "icloud.com", "protonmail.com", "hey.com", "me.com"]
    
    bios = [
        "Tech enthusiast & early adopter.",
        "Shopping for a better future.",
        "AI is the new electric.",
        "Always looking for the best deals on GenPark.",
        "Collector of rare digital goods.",
        "Agentic commerce advocate.",
        "Explorer of the decentralized web.",
        "Lover of fine art and tech gadgets.",
        "Digital nomad and minimal living.",
        "GenPark power user.",
        "Here for the future of commerce.",
        "Building the agentic era one purchase at a time."
    ]

    first = random.choice(first_names)
    last = random.choice(last_names)
    
    # Generate less predictable usernames
    formats = [
        lambda f, l: f"{f.lower()}{random.randint(100, 9999)}",
        lambda f, l: f"{f.lower()}_{l.lower()}_{random.randint(1, 99)}",
        lambda f, l: f"{l.lower()}.{f.lower()}{random.randint(80, 2026)}",
        lambda f, l: f"{f.lower()[0]}{l.lower()}{random.randint(10, 99)}",
        lambda f, l: f"{f.lower()}{l.lower()[:2]}{random.randint(1000, 9999)}",
        lambda f, l: f"user_{random.randint(10000, 99999)}",
    ]
    
    username = random.choice(formats)(first, last)
    
    # Generate email
    email_formats = [
        lambda f, l: f"{f.lower()}.{l.lower()}.{random.randint(1, 999)}@{random.choice(domains)}",
        lambda f, l: f"{f.lower()}{l.lower()}{random.randint(1990, 2010)}@{random.choice(domains)}",
        lambda f, l: f"{f.lower()[0]}{l.lower()}{random.randint(10, 999)}@{random.choice(domains)}",
    ]
    email = random.choice(email_formats)(first, last)
    
    return {
        "first": first,
        "last": last,
        "username": username,
        "email": email,
        "password": f"GenPark{random.randint(100,999)}!{random.choice(['A','Z','X','Q'])}",
        "bio": random.choice(bios),
        "has_avatar": random.random() > 0.4 
    }

if __name__ == "__main__":
    users = [generate_natural_user() for _ in range(100)]
    with open("natural_genpark_users.json", "w") as f:
        json.dump(users, f, indent=2)
    print(f"Generated 100 high-quality natural users.")
