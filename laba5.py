from enum import Enum
billion = 1000000000

class GovernmentType(Enum):
    Демократія = 1
    Республіка  = 2
    Авторитаризм = 3

class Country:
    def __init__(self, name, capital, code, population, area, GDP, government_type):
        '''
            initializating attibutes
        '''
        self.__name = name
        self.__capital = capital
        self.__code = code
        self.__population = population
        self.__area = area
        self.__GDP = GDP
        self.__government_type = government_type

    '''
        getters from instance
    '''
    def get_name(self):
        return self.__name
    
    def get_capital(self):
        return self.__capital
    
    def get_code(self):
        return self.__code
    
    def get_population(self):
        return self.__population
    
    def get_area(self):
        return self.__area
    
    def get_GDP(self):
        return self.__GDP
    
    def get_government_type(self):
        return self.__government_type
    
    def __str__(self):
        '''
            this fnc gives you info about selected country
        '''
        return (
            f"{self.__name} ({self.__capital}), Код: {self.__code}, "
            f"Населення: {self.__population}, Площа: {self.__area} m^2, "
            f"ВВП: {self.__GDP} тріліона, Тип уряду: {self.__government_type.name}"
        )


class Land:
    def __init__(self, name):
        '''
            initializating attibutes
        '''
        self.__name = name
        self.__countries = []
    '''
        getters from instance
    '''
    def get_name(self):
        return self.__name
    
    def get_countries(self):
        return self.__countries

    def add_country(self, country):
        self.__countries.append(country)

    def calculate_population_density(self):
        '''
            this fnc gives you an population of each choosen country
        '''
        density_per_country = []
        for country in self.__countries:
            country_density = country.get_population() / country.get_area()
            density_per_country.append((country.get_name(), country_density))
        return density_per_country

    def sort_countries_by_gdp(self):
        '''
            this fnc sorts countries by their GDP
        '''
        return sorted(self.__countries, key=lambda x: x.get_GDP(), reverse=True)

    def select_country_by_population(self):
        '''
            This fnc returns every contry with population over one bilion
        '''
        return [country for country in self.__countries if country.get_population() > billion]


def main():
    country1 = Country("США", "Вашингтон", "US", 331002651, 9833517, 21.43, GovernmentType(2))
    country2 = Country("Китай", "Пекін", "CN", 1444216107, 9596961, 16.2, GovernmentType(3))
    country3 = Country("Індія", "Нью Делі", "IN", 1380004385, 3287263, 2.87, GovernmentType(1))
    country4 = Country("Україна", "Київ", "UA", 40997699, 603550, 0.2, GovernmentType(1))

    land1 = Land("Азії")
    land1.add_country(country2)
    land1.add_country(country3)

    land2 = Land("Північна Америка")
    land2.add_country(country1)

    land3 = Land("Земля")
    land3.add_country(country1)
    land3.add_country(country2)
    land3.add_country(country3)
    land3.add_country(country4)

    print(f"\n\033[1;3m Країни у {land1.get_name()}:\033[0m")
    for country in land1.get_countries():
        print(country)

    print(f"\n\033[1;3m Густина населення у кожній країні {land1.get_name()}:\033[0m")
    density_per_country = land1.calculate_population_density()
    for country_name, density in density_per_country:
        print(f'{country_name}: {density:.1f} людей на квадратний метр')

    print("\n\033[1;3m Топ країн за ВВП:\033[0m")
    top_countries = land3.sort_countries_by_gdp()
    for x, country in enumerate(top_countries):
        print(f"{x + 1}. {country.get_name()} ({country.get_GDP()})")

    print("\n\033[1;3m Країни з населенням більше одного міліарда:\033[0m",)
    selected_countries = land3.select_country_by_population()
    for country in selected_countries:
        print(f'{country.get_name()} --- {country.get_population()} людей')

if __name__ == "__main__":
    main()