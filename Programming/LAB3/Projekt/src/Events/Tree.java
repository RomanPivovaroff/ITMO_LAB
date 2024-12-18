// Класс для Дерева
class Tree {
    private Location location;

    public Tree(Location location) {
        this.location = location;
    }

    public void interact(Character character) {
        if (character instanceof GiantDaughter) {
            System.out.println(character.name + " забралась на дерево, чтобы подождать.");
        }
    }
}