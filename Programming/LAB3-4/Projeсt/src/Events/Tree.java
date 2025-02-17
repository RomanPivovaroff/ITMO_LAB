package Events;

// Класс для Колодца
public class Tree extends Creature{
    public Tree(Location location) {
        super(location);
    }

    @Override
    public void interact(Character character) {
        if (character instanceof GiantDaughter) {
            System.out.println(character.name + " залезла на дерево, чтобы дождаться принца");
            character.location = this.location;
        }
    }
}