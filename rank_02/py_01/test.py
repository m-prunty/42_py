class Plant:
    '''Defines a Plant'''
    def __init__(self, name: str, height: int, days_old: int):
        '''creates a plant object with the given parameters'''
        self.name = name
        self.days_old = days_old
        self.height = height

    def get_info(self):
        '''prints the attributes of the object'''
        print(f'{self.name}: {self.height}cm, {self.days_old} days old')

    def grow(self):
        self.height += 1

    def age(self):
        self.days_old += 1

    def day(self):
        self.grow()
        self.age()


def grow_rose():
    '''makes a rose and lets it grow'''
    rose = Plant('Rose', 25, 30)
    original_height: int = rose.days_old
    print('=== Day 1 ===')
    rose.get_info()
    for day in range(6):
        rose.day()
    print('=== Day 7 ===')
    rose.get_info()
    print(f'Growth this week: +{rose.days_old - original_height}cm')


if __name__ == "__main__":
    grow_rose()
