using System.Reflection.Metadata;

public interface IAttackable
{
    public void TakeDamage(int damage);
}

public interface IArtifact
{
    public void Use(Hero self, Hero target);
}

public abstract class Hero : IAttackable
{
    // field
    public IArtifact Artifact;
    // property
    public string Name { get; set; }
    public int HP { get; set; }
    public int Defense { get; set; }
    public int Attack { get; set; }

    public Hero(string name, int attack, int hp, int defense, IArtifact artifact = null)
    {
        Name = name;
        this.Attack = attack;
        HP = hp;
        Defense = defense;
        Artifact = artifact;
    }

    public void TakeDamage(int damage)
    {
        if (damage < 0)
            return;

        if (damage < Defense)
        {
            return;
        }

        HP -= damage - Defense;
    }

    public abstract void SpecialAbility(Hero target);

    public virtual void UseArtifact(Hero opponent)
    {
        if (Artifact != null) { Artifact.Use(this, opponent); }
    }

    public override string ToString()
    {
        return $"[Name = {Name}, HP = {HP}, Attack = {Attack}, Defense = {Defense}, ex = {2 * 2}]";
    }
}