package Pokemons;

import Moves.*;
import ru.ifmo.se.pokemon.*;

public class Sunkern extends Pokemon {
    public Sunkern(String name, int level) {
        super(name, level);
        setStats(30, 30, 30, 30, 30, 30);
        setType(Type.GRASS);
        setMove(new  DoubleTeam(), new  SludgeBomb(), new Growth());
    }
}