package Pokemons;

import Moves.*;
import ru.ifmo.se.pokemon.*;

public class Registeel extends Pokemon {
    public Registeel(String name, int level) {
        super(name, level);
        setStats(80, 75, 150, 75, 150, 50);
        setType(Type.STEEL);
        setMove(new Thunder(), new  Rest(), new ThunderBolt(), new Stomp());
    }
}