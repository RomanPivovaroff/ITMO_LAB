package Moves;

import ru.ifmo.se.pokemon.*;

public class Stomp extends PhysicalMove {
    public Stomp() {
        super(Type.NORMAL, 65, 100);
    }

    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.3) {
            Effect.flinch(p);
        }
    }

    protected String describe() {
        return "is using Stomp";
    }
}