package Events;

// Класс для Колодца
class Tree {
    private Location location;

    public Tree(Location location) {
        this.location = location;
    }
    //нафиг не надо
    public Location interact(Character character) {
        if (character instanceof GiantDaughter) retrun this.location;
    }
}