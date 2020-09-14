from covid import Covid
covid = Covid(source="worldometers")
cases = covid.get_status_by_country_name("Bangladesh")
print(covid.list_countries())
for x in cases:
    print(x, ":", cases[x])
