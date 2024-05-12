from Adapter import AdapterImpl
from WeightMachine import WeightMachineForBabies

def main():

    adapter = AdapterImpl(WeightMachineForBabies())
    print(adapter.get_weight_in_kg())

if __name__ == "__main__":
    main()