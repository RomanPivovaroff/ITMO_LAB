import Pokemons.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        Battle b = new Battle();
        b.addAlly(new Sunkern("Sunkern", 1));
        b.addAlly(new Happiny("Happiny", 1));
        b.addAlly(new Chansey("Chansey", 1));
        b.addFoe(new Sunflora("Sunflora", 1));
        b.addFoe(new Blissey("Blissey", 1));
        b.addFoe(new Registeel("Растигайчик", 1));
        b.go();
    }
}