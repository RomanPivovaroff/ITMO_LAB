package Moves;

import ru.ifmo.se.pokemon.*;

public class BulletSeed extends PhysicalMove {
    public BulletSeed() {
        super(Type.GRASS, 25, 100, 0, 5);
    }

    protected String describe() {
        return "is using BulletSeed";
    }
}