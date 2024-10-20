package Pokemons;

import Moves.*;
import ru.ifmo.se.pokemon.*;

public class Blissey extends  Chansey {
    public Blissey(String name, int level) {
        super(name, level);
        setStats(255, 10, 10, 75, 135, 55);
        addMove(new IceBeam());
    }
}
