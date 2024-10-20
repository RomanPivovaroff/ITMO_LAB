package Moves;

import ru.ifmo.se.pokemon.*;

public class ThunderBolt extends SpecialMove {
    public ThunderBolt() {
        super(Type.ELECTRIC, 90, 100);
    }

    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.1) {
            Effect.paralyze(p);
        }
    }

    protected String describe() {
        return "is using ThunderBolt";
    }
}