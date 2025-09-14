def search_dis(patients, disease):
    result = [p["Name"] for p in patients if p["Disease"] == disease]
    return result


n = int(input("Enter number of patients: "))
patients = []

for _ in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    disease = input("Enter disease: ")
    patients.append({"Name": name, "Age": age, "Disease": disease})

skey = input("Enter disease to search: ")
result = search_dis(patients, skey)

print(f"Patients with {skey}:", result)