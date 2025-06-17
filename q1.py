import os
import sqlite3
import zipfile
import matplotlib.pyplot as plt

if not os.path.exists("data/github.db"):
    with zipfile.ZipFile("data/data.zip") as file:
        file.extractall("data")

class Point:
 x: float
 y: float

 def __init__(self, x: float, y: float):
  self.x = x
  self.y = y

class Line:
 label: str
 points: list[Point]

 def __init__(self, label: str, points: list[Point]):
  self.label = label
  self.points = points

class Bar:
 label: str
 value: int
 
 def __init__(self, label: str, value: int):
  self.label = label
  self.value = value

def create_line_graph(lines: list[Line], file_path: str):
 plt.clf()
 for line in lines:
  xs = [point.x for point in line.points]
  ys = [point.y for point in line.points]
  plt.plot(xs, ys, label = line.label)
 plt.legend(bbox_to_anchor=(0.5, -0.1), loc='upper center')
 plt.savefig(file_path, bbox_inches="tight")

def create_bar_graph(labels: tuple[str, str], bars: list[Bar], file_path: str):
 plt.clf()
 plt.bar(
  [
   bar.label 
   for bar in bars
  ],
  [
   bar.value
   for bar in bars
  ]
 )
 plt.xlabel(labels[0])
 plt.ylabel(labels[1])
 
 plt.savefig(file_path)

class QueryHandler:
 file_path: str
 connection: sqlite3.Connection

 def __init__(self, file_path: str):
  self.file_path = file_path
  self.connection = sqlite3.connect(file_path)

 def __del__(self):
  self.connection.close()
 
 def execute_atomic_query(self, query_template: str, *args) -> list[any]:
  query = query_template.format(*args)
  cursor = self.connection.cursor()
  result = cursor.execute(query)
  return result.fetchall()

class GithubRecord: #forward declaration
 pass
class GithubRecord:
 year: int
 years_of_experience: int
 main_branch: str
 country: str
 education_level: str
 languages_worked_with: str
 languages_interested_in: str
 dbms_worked_with: str
 dbms_interested_int: str
 age: int

 def __init__(self, year: int, years_of_experience: int, main_branch: str, country: str, education_level: str, languages_worked_with: str, languages_interested_in: str, dbms_worked_with: str, dbms_interested_in: str, age: str):
  self.year = year
  self.years_of_experience = years_of_experience
  self.main_branch = main_branch
  self.country = country
  self.education_level = education_level
  self.languages_worked_with = languages_worked_with
  self.languages_interested_in = languages_interested_in
  self.dbms_worked_with = dbms_worked_with
  self.dbms_interested_in = dbms_interested_in
  self.age = age

 def from_record(year: int, data: tuple) -> GithubRecord:
  return GithubRecord(year, *data)
 
 def validate(self) -> bool:
  return self.country is not None and self.main_branch != "None of these"
 def conform(self):
  #1.1.2 (4 marks)
  match self.country:
   case "Congo, Republic of the...":
    self.country = "Democratic Republic of the Congo"
   case "Democratic People's Republic of Korea":
    self.country = "North Korea"
   case "Republic of Korea":
    self.country = "South Korea"
   case "Saudi Arabia":
    self.country = "United Arab Emirates"
  #1.1.4 (3 marks)
  match self.main_branch:
   case "I am not primarily a developer, but I write code sometimes as part of my work":
    self.main_branch = "I am not primarily a developer, but I write code sometimes as part of my work/studies"
   case "I am a student who is learning to code":
    self.main_branch = "I am learning to code"

def get_countries(data: list[GithubRecord]) -> dict:
 countries = dict()
 for entry in data:
  if entry.country in countries:
   countries[entry.country] += 1
  else:
   countries[entry.country] = 1
 return countries

def get_education_level_by_years(data: list[GithubRecord]) -> list[dict]:
 education_levels: list[dict[str, int]] = [dict(), dict(), dict()]
 for entry in data:
  if entry.education_level in education_levels[entry.year - 2021]:
   education_levels[entry.year - 2021][entry.education_level] += 1
  else:
   education_levels[entry.year - 2021][entry.education_level] = 1
 return education_levels

def get_main_branches(data: list[GithubRecord], year: int) -> dict:
 main_branches = dict()
 for entry in (entry for entry in data if entry.year == year):
  if entry.main_branch in main_branches:
   main_branches[entry.main_branch] += 1
  else:
   main_branches[entry.main_branch] = 1
 return main_branches

def get_worked_with_programming_languages(data: list[GithubRecord], year: int=None) -> dict[str, int]:
 worked_with_programming_languages: dict[str, int] = dict()
 for entry in (entry for entry in data if (year is None or entry.year == year) and entry.languages_worked_with is not None):
  for programming_language in entry.languages_worked_with.split(";"):
   if programming_language in worked_with_programming_languages:
    worked_with_programming_languages[programming_language] += 1
   else:
    worked_with_programming_languages[programming_language] = 1
 return worked_with_programming_languages
def get_interested_in_programming_languages(data: list[GithubRecord], year: int=None) -> dict[str, int]:
 interested_in_programming_languages: dict[str, int] = dict()
 for entry in (entry for entry in data if (year is None or entry.year == year) and entry.languages_interested_in is not None):
  for programming_language in entry.languages_interested_in.split(";"):
   if programming_language in interested_in_programming_languages:
    interested_in_programming_languages[programming_language] += 1
   else:
    interested_in_programming_languages[programming_language] = 1
 return interested_in_programming_languages
def get_worked_with_dbms(data: list[GithubRecord], year: int=None) -> dict[str, int]:
 worked_with_dbms: dict[str, int] = dict()
 for entry in (entry for entry in data if (year is None or entry.year == year) and entry.dbms_worked_with is not None):
  for dbms in entry.dbms_worked_with.split(";"):
   if dbms in worked_with_dbms:
    worked_with_dbms[dbms] += 1
   else:
    worked_with_dbms[dbms] = 1
 return worked_with_dbms
def get_interested_in_dbms(data: list[GithubRecord], year: int=None) -> dict[str, int]:
 interested_in_dbms: dict[str, int] = dict()
 for entry in (entry for entry in data if (year is None or entry.year == year) and entry.dbms_interested_in is not None):
  for dbms in entry.dbms_interested_in.split(";"):
    if dbms in interested_in_dbms:
     interested_in_dbms[dbms] += 1
    else:
     interested_in_dbms[dbms] = 1
 return interested_in_dbms

def get_main_branch_representation_by_years(data: list[GithubRecord]):
 return [{k: v for k, v in sorted(get_main_branches(data, year).items(), key=lambda item: item[1])} for year in range(2021, 2024)]

query_handler = QueryHandler("data/Github.db")
#data = query_handler.execute_atomic_query("SELECT name, sql FROM sqlite_master WHERE type='table'")

query_format = "SELECT YearsCode, MainBranch, Country, EdLevel, LanguageHaveWorkedWith, LanguageWantToWorkWith, DatabaseHaveWorkedWith, DatabaseWantToWorkWith, Age FROM data_{}"
data_by_year: list[list[GithubRecord]] = [
 [GithubRecord.from_record(year, entry) for entry in query_handler.execute_atomic_query(query_format.format(year))]
 for year in range(2021, 2024)
]
data = data_by_year[0] + data_by_year[1] + data_by_year[2] #1.1.1 (4 marks)

#Sanitise (1.1.3)
valid_subset = [entry for entry in data if entry.validate()]
for entry in valid_subset:
 entry.conform()


"""
2.1.1.1 (5 Marks)
"""
main_branch_representation_by_years = get_main_branch_representation_by_years(valid_subset)
a = list(
 [year_data[key] for year_data in main_branch_representation_by_years]

 for key in set(
  key 
  for keys in (
   year_data.keys() 
   for year_data in 
    main_branch_representation_by_years
  )
  for key in keys
 )
)
#print(a)
# create_graph()


"""
2.1.2.1
"""

all_worked_with_programming_languages_2021 = [(k, v) for k, v in get_worked_with_programming_languages(valid_subset, 2021).items()]
all_interested_in_programming_languages_2021 = [(k, v) for k, v in get_interested_in_programming_languages(valid_subset, 2021).items()]
all_worked_with_dbms_2021 = [(k, v) for k, v in get_worked_with_dbms(valid_subset, 2021).items()]
all_interested_in_dbms_2021 = [(k, v) for k, v in get_interested_in_dbms(valid_subset, 2021).items()]
all_worked_with_programming_languages_2022 = [(k, v) for k, v in get_worked_with_programming_languages(valid_subset, 2022).items()]
all_interested_in_programming_languages_2022 = [(k, v) for k, v in get_interested_in_programming_languages(valid_subset, 2022).items()]
all_worked_with_dbms_2022 = [(k, v) for k, v in get_worked_with_dbms(valid_subset, 2022).items()]
all_interested_in_dbms_2022 = [(k, v) for k, v in get_interested_in_dbms(valid_subset, 2022).items()]
all_worked_with_programming_languages_2023 = [(k, v) for k, v in get_worked_with_programming_languages(valid_subset, 2023).items()]
all_interested_in_programming_languages_2023 = [(k, v) for k, v in get_interested_in_programming_languages(valid_subset, 2023).items()]
all_worked_with_dbms_2023 = [(k, v) for k, v in get_worked_with_dbms(valid_subset, 2023).items()]
all_interested_in_dbms_2023 = [(k, v) for k, v in get_interested_in_dbms(valid_subset, 2023).items()]

popular_worked_with_programming_languages_2021 = sorted(all_worked_with_programming_languages_2021, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_programming_languages_2021 = sorted(all_interested_in_programming_languages_2021, key=lambda x: x[1], reverse=True)[:5]
popular_worked_with_dbms_2021 = sorted(all_worked_with_dbms_2021, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_dbms_2021 = sorted(all_interested_in_dbms_2021, key=lambda x: x[1], reverse=True)[:5]
popular_worked_with_programming_languages_2022 = sorted(all_worked_with_programming_languages_2022, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_programming_languages_2022 = sorted(all_interested_in_programming_languages_2022, key=lambda x: x[1], reverse=True)[:5]
popular_worked_with_dbms_2022 = sorted(all_worked_with_dbms_2022, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_dbms_2022 = sorted(all_interested_in_dbms_2022, key=lambda x: x[1], reverse=True)[:5]
popular_worked_with_programming_languages_2023 = sorted(all_worked_with_programming_languages_2023, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_programming_languages_2023 = sorted(all_interested_in_programming_languages_2023, key=lambda x: x[1], reverse=True)[:5]
popular_worked_with_dbms_2023 = sorted(all_worked_with_dbms_2023, key=lambda x: x[1], reverse=True)[:5]
popular_interested_in_dbms_2023 = sorted(all_interested_in_dbms_2023, key=lambda x: x[1], reverse=True)[:5]

popular_worked_with_programming_languages = (
 popular_worked_with_programming_languages_2021, 
 popular_worked_with_programming_languages_2022, 
 popular_worked_with_programming_languages_2023
)
popular_interested_in_programming_languages = (
 popular_interested_in_programming_languages_2021, 
 popular_interested_in_programming_languages_2022, 
 popular_interested_in_programming_languages_2023
)
popular_worked_with_dbms = (
 popular_worked_with_dbms_2021, 
 popular_worked_with_dbms_2022, 
 popular_worked_with_dbms_2023
)
popular_interested_in_dbms = (
 popular_interested_in_dbms_2021, 
 popular_interested_in_dbms_2022, 
 popular_interested_in_dbms_2023
)

final_data = valid_subset

unique_countries = get_countries(final_data)
education_level_by_years = get_education_level_by_years(final_data) #1.1.5 (3 marks)
unique_main_branches2021 = get_main_branches(final_data, 2021)
unique_main_branches2022 = get_main_branches(final_data, 2022)
unique_main_branches2023 = get_main_branches(final_data, 2023)
main_branch_representation_by_years = get_main_branch_representation_by_years(final_data)

unique_main_branches = list(
 set(
  list(unique_main_branches2021.keys()) + 
  list(unique_main_branches2022.keys()) + 
  list(unique_main_branches2023.keys())
 )
)
create_line_graph(
 [
  Line(
   unique_main_branch,
   [
    Point(
     index, 
     main_branch_representation_by_year[unique_main_branch] if unique_main_branch in main_branch_representation_by_year else 0)
    for index, main_branch_representation_by_year in enumerate(main_branch_representation_by_years)
   ]
  )
  for unique_main_branch in unique_main_branches
 ],
 "graphs/2.1.1.1.png"
)

unique_education_levels = list(
 set(
  list(education_level_by_years[0].keys()) + 
  list(education_level_by_years[1].keys()) + 
  list(education_level_by_years[2].keys())
 )
)
create_line_graph(
 [
  Line(
   unique_education_level,
   [
    Point(
     index, 
     education_level_by_year[unique_education_level] if unique_education_level in education_level_by_year else 0)
    for index, education_level_by_year in enumerate(education_level_by_years)
   ]
  )
  for unique_education_level in unique_education_levels
 ],
 "graphs/2.1.1.2.png"
)

create_bar_graph(
 (
  "WW Programming Language", 
  "# Users"
 ), 
 [
  Bar(popular_worked_with_programming_language_2023[0], popular_worked_with_programming_language_2023[1]) 
  for popular_worked_with_programming_language_2023 in popular_worked_with_programming_languages_2023
 ],
 "graphs/2.1.2.1.1.png"
)

create_bar_graph(
 (
  "II Programming Language", 
  "# Users"
 ), 
 [
  Bar(popular_interested_in_programming_language_2023[0], popular_interested_in_programming_language_2023[1]) 
  for popular_interested_in_programming_language_2023 in popular_interested_in_programming_languages_2023
 ],
 "graphs/2.1.2.1.2.png"
)

create_bar_graph(
 (
  "WW DBMS", 
  "# Users"
 ), 
 [
  Bar(popular_worked_with_dbms_2023[0], popular_worked_with_dbms_2023[1]) 
  for popular_worked_with_dbms_2023 in popular_worked_with_dbms_2023
 ],
 "graphs/2.1.2.1.3.png"
)

create_bar_graph(
 (
  "II DBMS", 
  "# Users"
 ), 
 [
  Bar(popular_interested_in_dbms_2023[0], popular_interested_in_dbms_2023[1]) 
  for popular_interested_in_dbms_2023 in popular_interested_in_dbms_2023
 ],
 "graphs/2.1.2.1.4.png"
)