package Pokemons;

import Moves.*;
import ru.ifmo.se.pokemon.*;

public class Sunflora extends Sunkern {
    public Sunflora(String name, int level) {
        super(name, level);
        setStats(75, 75, 55, 105, 85, 30);
        setType(Type.GRASS);
        addMove(new BulletSeed());
    }
}