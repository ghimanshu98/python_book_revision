class MyFirstClass:
    def reset(self) -> None:
        self.x = 0
        self.y = 0

a = MyFirstClass()

# creating attributes for object a, belonging to the above class directly

a.x = 5
a.y = 6
print('{}, {}'.format(a.x, a.y))

a.reset()
print('After resetting')
print('{}, {}'.format(a.x, a.y))