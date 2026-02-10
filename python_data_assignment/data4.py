
def calculate_average(users):
    averages = []

    for user in users:
        scores = user["scores"]
        avg = sum(scores) / len(scores)
        averages.append(avg)

    return averages

def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Samarth",
            "scores": [60, 70, 80],
            "roles": {"admin", "editor"}
        },
        {
            "name": "Amit",
            "scores": [40, 45, 50],
            "roles": {"viewer"}
        }
    ]

    averages = calculate_average(users)

    for i in range(len(users)):
        print("Name:", users[i]["name"])
        print("Average Score:", averages[i])

        if has_admin_access(users[i]["roles"]):
            print("Admin Access: Yes")
        else:
            print("Admin Access: No")
main()