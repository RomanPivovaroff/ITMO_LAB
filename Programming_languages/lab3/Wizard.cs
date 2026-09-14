public class Wizard : Hero
{
    public Wizard(string name, int attack, int hp, int defense, IArtifact artifact = null) :
        base(name, attack, hp, defense, artifact)
    {

    }

    public override void SpecialAbility(Hero target)
    {
        this.HP += 20;
    }
}