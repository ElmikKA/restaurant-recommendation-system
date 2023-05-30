
route_to_city = {
    "Tallinn": set(["Keila", "Rakvere", "Paide", "Haapsalu", "Pärnu"]),
    "Tartu": set(["Mustvee", "Võru", "Viljandi", "Paide"]),
    "Narva": set(["Jõhvi"]),
    "Keila": set(["Pärnu", "Tallinn"]),
    "Paide": set(["Tallinn", "Haapsalu", "Pärnu", "Viljandi", "Tapa", "Tartu"]),
    "Tapa": set(["Paide", "Rakvere"]),
    "Rakvere": set(["Tallinn", "Jõhvi"]),
    "Jõhvi": set(["Mustvee", "Rakvere", "Narva"]),
    "Mustvee": set(["Jõhvi", "Tartu"]),
    "Võru": set(["Tartu", "Valga"]),
    "Valga": set(["Võru", "Viljandi"]),
    "Viljandi": set(["Tartu", "Valga", "Paide", "Pärnu"]),
    "Pärnu": set(["Viljandi", "Paide", "Tallinn", "Keila", "Haapsalu"]),
    "Haapsalu": set(["Paide", "Tallinn", "Pärnu", "Kuresaare"]),
    "Kuresaare": set(["Haapsalu"])
}
