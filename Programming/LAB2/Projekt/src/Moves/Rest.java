package Moves;

import ru.ifmo.se.pokemon.*;

public class Rest extends StatusMove {
    public Rest() {
        super(Type.PSYCHIC, 0, 0);
    }

    protected boolean checkAccuracy(Pokemon att, Pokemon def) {
        return true;
    }

    protected void applySelfEffects(Pokemon p) {
        p.restore();
        p.addEffect(new Effect().condition(Status.SLEEP).turns(2));
    }

    protected String describe() {
        return "is using Rest";
    }
}