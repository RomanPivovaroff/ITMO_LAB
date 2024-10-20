package Moves;

import ru.ifmo.se.pokemon.*;

public class Growth  extends StatusMove {
    public Growth () {
        super(Type.NORMAL, 0, 0);
    }

    protected boolean checkAccuracy(Pokemon att, Pokemon def) {
        return true;
    }

    protected void applySelfEffects(Pokemon p) {
        p.setMod(Stat.SPECIAL_ATTACK, 1);
        p.setMod(Stat.ATTACK, 1);
    }

    protected String describe() {
        return "is using Growth";
    }
}