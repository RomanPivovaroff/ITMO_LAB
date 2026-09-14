public class Warrior : Hero
{
    public Warrior(string name, int attack, int hp, int defense, IArtifact artifact = null) :
        base(name, attack, hp, defense, artifact)
    {

    }

    public override void SpecialAbility(Hero target)
    {
        target.TakeDamage(Attack * 2);
    }
}