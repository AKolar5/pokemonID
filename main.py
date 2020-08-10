import csv
import pokeclass


def search(name):
    with open("pokes.csv", "r") as csv_file:
        fieldnames = ['Name', 'Type 1', 'Type 2']
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter='\t')

        for line in csv_reader:
            if line['Name'].lower() == name.lower():
                if line['Type 2'] != '':
                    t1 = pokeclass.makePoke(line['Type 1'])
                    t2 = pokeclass.makePoke(line['Type 2'])
                    weaks = pokeclass.compare(t1.getWeak(), t1.getResist(), t2.getWeak(), t2.getResist())
                    resists = pokeclass.compare(t1.getResist(), t1.getWeak(), t2.getResist(), t2.getWeak())
                    supereffs = pokeclass.compare(t1.getSupeff(), t1.getNoteff(), t2.getSupeff(), t2.getNoteff())
                    noteffs = pokeclass.compare(t1.getNoteff(), t1.getSupeff(), t2.getNoteff(), t2.getSupeff())
                    counters = pokeclass.findCounter(weaks, noteffs)
                    immune = pokeclass.combine(t1.getImmune(), t2.getImmune())
                    print('\nWeak:', *weaks)
                    print('Resists:', *resists)
                    print('Immune to:', *immune)
                    print('Super Effective Against:', *supereffs)
                    print('Not Effective Against:', *noteffs)
                    print('Counter With:', *counters)

                else:
                    t = pokeclass.makePoke(line['Type 1'])
                    print('\nWeak:', *t.getWeak())
                    print('Resists:', *t.getResist())
                    if pokeclass.isListEmpty(t.getImmune()):
                        print('Immune to: None')
                    else:
                        print('Immune to:', *t.getImmune())
                    print('Super Effective Against:', *t.getSupeff())
                    print('Not Effective Against:', *t.getNoteff())
                    print('Counter With:', *t.getCounter())


    print('\n')
    main()




def main():
    n = input("Enter the name of a Pokemon: ")
    search(n)


if __name__ == '__main__':
    main()




