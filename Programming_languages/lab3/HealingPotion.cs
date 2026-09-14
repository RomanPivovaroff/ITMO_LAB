public class HealingPotion : IArtifact
{
    int Strenght;
    public HealingPotion(int strenght)
    {
        Strenght = strenght;
    }

   public void Use(Hero self, Hero target)
    {
        self.HP += Strenght;
    }

}