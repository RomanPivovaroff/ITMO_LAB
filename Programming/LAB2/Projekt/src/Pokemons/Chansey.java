package Pokemons;

import Moves.*;
import ru.ifmo.se.pokemon.*;

public class Chansey extends  Happiny{
    public Chansey(String name, int level) {
        super(name, level);
        setStats(250, 5, 5, 35, 105, 50);
        addMove(new Present());
    }
}
