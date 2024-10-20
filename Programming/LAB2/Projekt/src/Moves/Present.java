package Moves;
import ru.ifmo.se.pokemon.*;

public class Present extends PhysicalMove{
    private boolean isDamage;
    private int Attack_Damage;
    public Present() {
        super(Type.NORMAL, 0, 90);
        double chance = Math.random();
        this.isDamage = true;
        if (chance <= 0.4) {this.Attack_Damage = 40;}
        else if (chance <= 0.7) {this.Attack_Damage = 80;}
        else if (chance <= 0.8) {this.Attack_Damage = 120;}
        else {this.isDamage = false;};
    }

    protected void applyOppDamage(Pokemon def, double damage) {
        if (isDamage) def.setMod(Stat.HP, Attack_Damage);
        else def.setMod(Stat.HP, -(int)Math.ceil((def.getStat(Stat.HP)) / 4));
    }

    protected String describe(){
        return "is using Present";
    }
}