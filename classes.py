class Cell:
    def __init__(self, type, x, y) -> None:
        color = (0, 0, 0)
        match type:
            case 'street':
                color = (155, 155, 155)

            case 'building':
                color = (145, 78, 245)

            case _:
                raise ValueError('type specified doesn\'t exist')
        
        self.type = type
        self.x = x
        self.y = y
        self.color = color
