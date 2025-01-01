from Abstraction import FishLivingThings, TreeLivingThings, BirdLivingThings
from Implementor import FishBreatheImplementor, TreeBreatheImplementor, BirdBreatheImplementor

class Client:

    fish_implementor = FishBreatheImplementor()
    bird_implementor = BirdBreatheImplementor()
    tree_implementor = TreeBreatheImplementor()

    fish_living_things = FishLivingThings(fish_implementor)
    bird_living_things = BirdLivingThings(bird_implementor)
    tree_living_things = TreeLivingThings(tree_implementor)

    fish_living_things.breathe_process()
    bird_living_things.breathe_process()
    tree_living_things.breathe_process()